# routes/users.py
import datetime

from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from backends.services.wth.app.utils.mysql_connect import get_connection

ticket_bp = Blueprint('ticket', __name__)


@ticket_bp.route('/addticket',methods=["POST"])
def get_ticket():
    try:
        print("ticket")
        # 从请求中获取优惠券 ID 和用户 ID
        data = request.get_json()
        ticket_id = data.get('coupon_id')
        user_id = data.get('user_id')

        # 检查参数
        if not ticket_id or not user_id:
            return jsonify({"status": 400, "message": "优惠券ID和用户ID不能为空"})

        # 执行插入操作，这将触发数据库中的触发器
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                        INSERT INTO userTicket (user_ID, ticket_ID)
                        VALUES (%s, %s)
                    """, (user_id, ticket_id))
                conn.commit()

        # 返回成功信息
        return jsonify({"status": 200, "message": "领取成功"})
    except Exception as e:
        # 如果库存不足，捕获触发器抛出的错误
        if "库存不足" in str(e):
            return jsonify({"status": 400, "message": "库存不足"})
        # 其他错误
        print(f"Error while claiming ticket: {e}")
        return jsonify({"status": 500, "message": "领取失败，服务器内部错误"})



@ticket_bp.route('/get_ticket',methods=["POST"])
def show_ticket():
    print("get_ticket")
    """
        查询优惠券信息并返回前端
        """
    try:


        with get_connection() as conn:  # 获取数据库连接
            with conn.cursor(dictionary=True) as cursor:  # 使用字典游标返回列名对应值
                # SQL 查询语句
                sql_query = "SELECT * FROM ticket WHERE due_time >= %s"
                params = [datetime.date.today()]  # 查询未过期的优惠券

                cursor.execute(sql_query, params)  # 执行查询
                tickets = cursor.fetchall()  # 获取所有结果

        return jsonify({'status': 'success', 'data': tickets}), 200

    except Exception as e:
        print(f"Error fetching tickets: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to fetch tickets'}), 500