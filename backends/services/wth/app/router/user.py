# routes/users.py
import hashlib

from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from backends.services.wth.app.utils.mysql_connect import get_connection

users_bp = Blueprint('users', __name__)


# MD5 加密函数
def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


@users_bp.route('/login', methods=['POST'])
def get_users():
    # 获取请求中的用户名和密码
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print(f"Username: {username}")
    print(f"Password: {password}")

    # 检查是否有传递用户名和密码
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    try:
        with get_connection() as conn:  # 连接池获取连接
            with conn.cursor() as cursor:
                # 查询数据库，查找对应的用户名
                cursor.execute("SELECT * FROM users WHERE userName = %s", (username,))
                user = cursor.fetchone()

                # 如果没有找到用户
                if not user:
                    return jsonify({"message": "User not found"}), 404

                # 获取数据库中存储的密码哈希
                stored_password_hash = user[2]  # 假设数据库中的密码哈希在第三列
                print(f"hash+{stored_password_hash}")
                # 使用 MD5 对传入的密码进行加密
                password_hash = hash_password(password)

                # 检查密码是否匹配
                if stored_password_hash != password_hash:
                    return jsonify({"message": "Invalid password"}), 401

                # 如果用户名和密码匹配，返回成功
                return jsonify({"message": "Login successful", "userID": user[0]}), 200

    except Exception as e:
        # 处理错误
        print(f"Error occurred: {e}")
        return jsonify({"message": "An error occurred while processing your request"}), 500

@users_bp.route('/getPower',methods=['POST'])
def get_power():
    try:
        # 获取请求中的 userId
        data = request.get_json()
        user_id = data.get("userId")

        if not user_id:
            return jsonify({"error": "userId is required"}), 400

        with get_connection() as conn:  # 使用连接池获取数据库连接
            with conn.cursor() as cursor:
                # 查询用户状态
                cursor.execute("SELECT state FROM users WHERE user_ID = %s", (user_id,))
                result = cursor.fetchone()

                if result is None:
                    return jsonify({"error": "User not found"}), 404

                # 获取状态值
                state = result[0]

                return jsonify({"power": state}), 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({"error": str(e)}), 500