from flask import jsonify, request
from backends.services.lzr.app import app, get_db
import random

@app.route('/', methods=['POST'])
def home():
    """进入首页随机展示 18 个商品"""
    conn = get_db()
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
    """根据类别展示商品"""
    data = request.get_json()
    category = data['category']
    conn = get_db()
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
    items = data.get('items')  # items 是一个包含商品ID和数量的列表

    conn = get_db()
    cursor = conn.cursor()

    # 获取用户ID
    cursor.execute('SELECT user_ID FROM users WHERE userName=%s', (user_name,))
    user_id = cursor.fetchone()[0]

    # 插入订单记录
    for item in items:
        item_id = item['item_id']
        item_num = item['item_num']

        # 获取商品价格
        cursor.execute('SELECT price FROM item WHERE item_ID=%s', (item_id,))
        price = cursor.fetchone()[0]

        # 计算总价格
        total_price = price * item_num

        # 插入订单记录
        cursor.execute('''
            INSERT INTO orders (user_ID, item_ID, state, price, count)
            VALUES (%s, %s, %s, %s, %s)
        ''', (user_id, item_id, 0, total_price, item_num))

    conn.commit()
    conn.close()

    return jsonify({'message': '订单已生成'})


@app.route('/BackupDatabase', methods=['GET'])
def backup():
    """备份数据库"""
    conn = get_db()
    cursor = conn.cursor()

    # 备份数据库
    cursor.execute('BACKUP DATABASE supersupermarket TO DISK = "C:/supersupermarket.bak"')
    conn.commit()
    conn.close()

    return jsonify({'message': '数据库已备份'})


@app.route('/recovery', methods=['GET'])
def recovery():
    """恢复数据库"""
    conn = get_db()
    cursor = conn.cursor()

    # 恢复数据库
    cursor.execute('RESTORE DATABASE supersupermarket FROM DISK = "C:/supersupermarket.bak"')
    conn.commit()
    conn.close()

    return jsonify({'message': '数据库已恢复'})