from flask import Flask, request, jsonify
from flask_cors import CORS

#后端服务器启动
app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    print(data)
    return jsonify({'data': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)
    print('服务器关闭')