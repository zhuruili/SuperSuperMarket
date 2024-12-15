import mysql.connector
from mysql.connector import pooling

# 数据库连接配置

db_config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'super_supermarket'
}

# 创建连接池
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    **db_config
)

# 获取连接
def get_connection():
    return connection_pool.get_connection()

# 关闭连接
def close_connection(conn):
    conn.close()

# if __name__ == "__main__":
#     try:
#         with get_connection() as conn:  # 连接池获取连接
#             with conn.cursor() as cursor:
#                 # 删除指定用户
#                 delete_query = """
#                 DELETE FROM users WHERE user_ID = %s
#                 """
#                 # 要删除的用户ID
#                 user_id = 1
#                 cursor.execute(delete_query, (user_id,))  # 执行删除操作
#                 conn.commit()  # 提交事务，确保删除操作生效
#
#                 print(f"User with ID {user_id} deleted successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
#
# if __name__ == "__main__":
#     try:
#         with get_connection() as conn:  # 连接池获取连接
#             with conn.cursor() as cursor:
#                 # 插入新用户，去掉 user_ID 自增字段
#                 insert_query = """
#                 INSERT INTO users (userName, passwords, state)
#                 VALUES (%s, %s, %s)
#                 """
#                 # 插入的用户数据
#                 user_data = ('jack', '123456', 0)
#                 cursor.execute(insert_query, user_data)  # 执行插入操作
#                 conn.commit()  # 提交事务，确保数据被保存
#
#                 print(f"User inserted successfully: {user_data}")
#     except Exception as e:
#         print(f"Error: {e}")

if __name__ == "__main__":
    try:
        with get_connection() as conn:  # 连接池获取连接
            with conn.cursor() as cursor:
                # 插入订单数据
                insert_query = """
                INSERT INTO orders (user_ID, item_ID, state, price, count)
                VALUES (%s, %s, %s, %s, %s)
                """
                # 插入的订单数据
                order_data = [
                    (1, 417, 0, 2499, 1),
                    (1, 39, 0, 6199, 1),
                    (1, 3858, 0, 112.9, 1),
                    (1, 4177, 0, 57, 1)
                ]

                # 执行插入操作
                for data in order_data:
                    cursor.execute(insert_query, data)

                conn.commit()  # 提交事务，确保数据被保存

                print("Orders inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")








"""
# 在路由中获取前端参数
name = request.form['name']
email = request.form['email']

# 构建SQL查询语句,使用%s占位符
query = "INSERT INTO users (name, email) VALUES (%s, %s)"
users=execute_update(query, (name, email))



# 在路由中执行SQL查询


# 处理查询结果
for user in users:
    user_id, user_name, user_email = user
    # 使用查询结果中的数据
    print(f"User ID: {user_id}, Name: {user_name}, Email: {user_email}")
    
try except拦截
try:
        name = request.form['name']
        email = request.form['email']
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        execute_update(query, (name, email))
        return redirect(url_for('get_users'))
    except Error as e:
        # 处理错误
        print(f"Error creating user: {e}")
        return "Error occurred while creating user", 500
"""
