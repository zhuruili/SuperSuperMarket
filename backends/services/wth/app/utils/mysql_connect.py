import mysql.connector
from mysql.connector import pooling

# 数据库连接配置
db_config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'shopping'
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
