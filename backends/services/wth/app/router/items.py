import random

# routes/users.py
# routes/users.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from backends.services.wth.app.utils.mysql_connect import get_connection

item_bp = Blueprint('item', __name__)


@item_bp.route('/addItem', methods=["POST"])
def add_item():
    data = request.get_json()  # 获取前端传来的 JSON 数据

    # 从数据中提取各个字段
    title = data.get('title')
    pic_url = data.get('pic_url')
    price = data.get('price')
    sale = data.get('sale')
    shop_name = data.get('shop_name')
    store = data.get('store')
    kind = data.get('kind')
    url = data.get('url')
    user_id = data.get('user_id')  # 假设前端传递了用户ID
    item_id = random.randint(20000, 1000000)  # 随机生成 item_ID

    try:
        with get_connection() as conn:  # 获取数据库连接
            with conn.cursor() as cursor:
                # 调用存储过程
                cursor.callproc('AddItemAndMerchandise', [
                    item_id, title, pic_url, price, sale, shop_name, store, kind, url, user_id
                ])
                conn.commit()  # 提交事务

        # 返回成功响应
        return jsonify({"success": True, "message": "商品添加成功"})

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "商品添加失败"})