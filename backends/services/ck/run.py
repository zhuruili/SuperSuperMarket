from flask import Flask, request, jsonify
from flask_cors import CORS
import random


from utils import get_db_connection

# 后端服务器启动
app = Flask(__name__)
CORS(app, resources=r'/*')

kind = {
  '电脑': 1,
  '手机': 2,
  '女装': 3,
  '食品': 4,
  '宠物': 5,
  '美妆': 6,
  '鲜花': 7,
  '图书': 8
}

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    print(data)
    category = data.get('category')
    query = data.get('query')
    print('category' + category)
    print('query' + query)
    id = kind.get(category)

    # 连接到 MySQL 服务器
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM item_kind{id} WHERE title LIKE '%{query}%'")
    result = cursor.fetchall()
    return jsonify({'data': result})

@app.route('/register', methods=['POST'])
def register():
    conn = get_db_connection()
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')
    print('username' + username)
    print('password' + password)
    
    cursor = conn.cursor()
    cursor.execute('insert into users(userName, passwords, state) values(%s, %s, %s)', [username, password, 0])
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'data': '注册成功'})

@app.route('/purchase', methods=['POST'])
def purchase():
    data = request.get_json()
    user_name = data.get('user_name')
    item_id = data.get('item_id')
    state = data.get('state')
    price = data.get('price')
    count = data.get('count')

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 显式地开始事务：一起成功一起失败：
        cursor.execute("START TRANSACTION;")
        cursor.execute('select user_ID from users where userName=%s', [user_name])
        user_id = cursor.fetchone()[0]
        cursor.execute('update item set store = store - %s where item_ID = %s', [count, item_id])
        cursor.execute('insert into orders(user_id, item_id, state, price, count) values(%s, %s, %s, %s, %s)', [user_id, item_id, state, price, count])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("创建订单失败")
        conn.rollback()
        return jsonify({'data': '购买失败'})
    
    return jsonify({'data': '购买成功'})

@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_name = data.get('user_name')
    item_id = data.get('item_id')
    count = data.get('count')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select user_ID from users where userName=%s', [user_name])
    user_id = cursor.fetchone()[0]
    cursor.execute('insert into cart(user_id, item_id, count) values(%s, %s, %s)', [user_id, item_id, count])
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'data': '添加成功'})

@app.route('/getCart', methods=['POST'])
def get_cart():
    data = request.get_json()
    user_name = data.get('user_name')
    print('用户名' + user_name)

    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''
        SELECT * FROM cart 
        WHERE user_id = (SELECT user_ID FROM users WHERE userName = %s)
    '''
    cursor.execute(query, [user_name])

    Cart = cursor.fetchall()
    result = []
    for cart in Cart:
        cart_dict = {
            'cart_id': cart[0],
            'user_id': cart[1],
            'item_id': cart[2],
            'state': '0',
            'count': cart[3]
        }
        cursor.execute('SELECT title, pic_url, shop_name, price FROM item WHERE item_ID = %s', [cart_dict['item_id']])
        item = cursor.fetchone()
        if item:
            cart_dict['title'] = item[0]
            cart_dict['pic_url'] = item[1]
            cart_dict['shop_name'] = item[2]
            cart_dict['price'] = item[3]
        result.append(cart_dict)
    return jsonify({'data': result})

@app.route('/getOrder', methods=['POST'])
def get_Order():
    data = request.get_json()
    user_name = data.get('user_name')
    print('用户名' + user_name)

    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''
        SELECT * FROM orders 
        WHERE user_id = (SELECT user_ID FROM users WHERE userName = %s)
    '''
    cursor.execute(query, [user_name])
    orders = cursor.fetchall()
    
    result = []
    for order in orders:
        order_dict = {
            'order_id': order[0],
            'user_id': order[1],
            'item_id': order[2],
            'state': order[3],
            'price': order[4],
            'count': order[5]
        }
        cursor.execute('SELECT title, pic_url, shop_name FROM item WHERE item_ID = %s', [order_dict['item_id']])
        item = cursor.fetchone()
        if item:
            order_dict['title'] = item[0]
            order_dict['pic_url'] = item[1]
            order_dict['shop_name'] = item[2]
        result.append(order_dict)
    
    cursor.close()
    conn.close()

    return jsonify({'data': result})

@app.route('/', methods=['POST'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # 生成 18 个随机的 itemID
    random_ids = random.sample(range(1, 12001), 18)
    format_strings = ','.join(['%s'] * len(random_ids))

    # 查询这些随机 itemID 对应的记录
    cursor.execute(f'SELECT * FROM item WHERE item_ID IN ({format_strings})', tuple(random_ids))
    selected_items = cursor.fetchall()
    conn.close()

    return jsonify(selected_items)

@app.route('/category', methods=['POST'])
def category():
    data = request.get_json()
    category = data.get('category')
    print('category' + category)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    kind = {
        '电脑': 1,
        '手机': 2,
        '女装': 3,
        '食品': 4,
        '宠物': 5,
        '美妆': 6,
        '鲜花': 7,
        '图书': 8
        }

    # 根据类别构建视图名称
    view_name = f'item_kind{kind[category]}'

    # 查询指定 category 的记录
    cursor.execute(f'SELECT * FROM {view_name} LIMIT 90')
    selected_items = cursor.fetchall()
    conn.close()

    return jsonify(selected_items)

@app.route('/Cart/checkout', methods=['POST'])
def checkout():
    """
    结算购物车，将购物车中的商品生成订单  
    ```python
    {
        "user_name": "example_user",
        "items": [
            {"item_id": 1, "item_num": 2},
            {"item_id": 2, "item_num": 1}
        ]
    }
    ```
    """
    data = request.get_json()
    user_name = data.get('user_name')
    items = data.get('items')

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 显式地开始事务
        cursor.execute("START TRANSACTION;")

        # 获取用户ID
        cursor.execute('SELECT user_ID FROM users WHERE userName=%s', (user_name,))
        user_result = cursor.fetchone()
        if user_result is None:
            return jsonify({'error': 'User not found'}), 404
        user_id = user_result[0]

        # 插入订单记录
        for item in items:
            item_id = item['item_id']
            item_num = item['item_num']

            # 获取商品价格
            cursor.execute('SELECT price FROM item WHERE item_ID=%s', (item_id,))
            price_result = cursor.fetchone()
            if price_result is None:
                return jsonify({'error': f'Item with ID {item_id} not found'}), 404
            price = price_result[0]

            # 计算总价格
            total_price = price * item_num

            # 插入订单记录
            cursor.execute('''
                INSERT INTO orders (user_ID, item_ID, state, price, count)
                VALUES (%s, %s, %s, %s, %s)
            ''', (user_id, item_id, 0, total_price, item_num))

            # 删除购物车中的商品
            cursor.execute('''
                DELETE FROM cart
                WHERE user_ID=%s AND item_ID=%s
            ''', (user_id, item_id))

        # 提交事务
        conn.commit()
        return jsonify({"message": "结算成功"}), 200
    except Exception as e:
        # 回滚事务
        conn.rollback()
        print('Error:', e)
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)
    print('服务器关闭')