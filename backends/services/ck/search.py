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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)
    print('服务器关闭')