

# routes/users.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from backends.services.wth.app.utils.mysql_connect import get_connection

order_bp = Blueprint('order', __name__)

@order_bp.route('/getOrder',methods=["POST"])
def get_order():
    try:
        # 获取请求体中的 userId
        data = request.get_json()
        user_id = data.get('userId')

        if not user_id:
            return jsonify({"error": "用户ID不能为空"}), 400

        # 查询订单数据
        query = """
                SELECT o.order_ID, o.user_ID, o.item_ID, o.state, o.price, o.count, 
                       i.title, i.pic_url ,i.shop_name
                FROM orders o
                JOIN item i ON o.item_ID = i.item_ID
                WHERE o.user_ID = %s
            """

        with get_connection() as conn:  # 获取数据库连接
            with conn.cursor(dictionary=True) as cursor:  # 使用字典格式返回数据
                cursor.execute(query, (user_id,))
                results = cursor.fetchall()

        # 返回订单数据
        return jsonify({"orders": results})

    except Exception as e:
        print(f"查询订单失败: {e}")
        return jsonify({"error": "服务器内部错误"}), 500