# routes/users.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from backends.services.wth.app.utils.mysql_connect import get_connection

users_bp = Blueprint('users', __name__)

@users_bp.route('/login',methods=['POST'])
def get_users():
    # 获取请求中的用户名和密码
    data = request.json
    username = data.get('username')
    password = data.get('password')
    print(username)
    print(password)
    # 检查是否有传递用户名和密码
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    try:
        with get_connection() as conn:  # 连接池获取连接
            with conn.cursor() as cursor:
                # 查询数据库，查找对应的用户名和密码
                cursor.execute("SELECT * FROM users WHERE userName = %s", (username,))
                user = cursor.fetchone()

                # 如果没有找到用户
                if not user:
                    return jsonify({"message": "User not found"}), 404

                # 检查密码是否匹配
                # 这里假设数据库中的密码是明文存储的，实际应用中应该使用哈希存储和验证
                if user[2] != password:  # 假设用户密码在第三列
                    return jsonify({"message": "Invalid password"}), 401

                # 如果用户名和密码匹配，返回成功
                return jsonify({"message": "Login successful", "userID": user[0]}), 200

    except Exception as e:
        # 处理错误
        print(f"Error occurred: {e}")
        return jsonify({"message": "An error occurred while processing your request"}), 500


