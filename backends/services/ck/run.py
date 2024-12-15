from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

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
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='super_supermarket'
    )
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM item WHERE title LIKE '%{query}%' AND kind={id}")
    result = cursor.fetchall()
    return jsonify({'data': result})

@app.route('/register', methods=['POST'])
def register():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password = '123456',
        database='super_supermarket'
    )
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

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password = '123456',
        database='super_supermarket'
    )
    cursor = conn.cursor()
    cursor.execute('select user_ID from users where userName=%s', [user_name])
    user_id = cursor.fetchone()[0]
    cursor.execute('insert into orders(user_id, item_id, state, price, count) values(%s, %s, %s, %s, %s)', [user_id, item_id, state, price, count])
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'data': '购买成功'})

@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_name = data.get('user_name')
    item_id = data.get('item_id')
    count = data.get('count')

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password = '123456',
        database='super_supermarket'
    )
    cursor = conn.cursor()
    cursor.execute('select user_ID from users where userName=%s', [user_name])
    user_id = cursor.fetchone()[0]
    cursor.execute('insert into cart(user_id, item_id, count) values(%s, %s, %s)', [user_id, item_id, count])
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'data': '添加成功'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)
    print('服务器关闭')