# routes/users.py
from flask import Blueprint, render_template, request, redirect, url_for

from backends.services.wth.app.utils.mysql_connect import get_connection

users_bp = Blueprint('users', __name__)

@users_bp.route('/')
def get_users():
    try:
        with get_connection() as conn:#,它会从连接池中获取一个可用的连接。当 with 块结束时,连接会自动返回到连接池中,等待下次使用。
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
        return render_template('users.html', users=users)
    except Exception as e:
        # 处理错误
        print(f"Error getting users: {e}")
        return "Error occurred while fetching users", 500

@users_bp.route('/create', methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        with get_connection() as conn:#,它会从连接池中获取一个可用的连接。当 with 块结束时,连接会自动返回到连接池中,等待下次使用。
            with conn.cursor() as cursor:
                cursor.execute(query)
        return redirect(url_for('users.get_users'))
    except Exception as e:
        # 处理错误
        print(f"Error creating user: {e}")
        return "Error occurred while creating user", 500