import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='super_supermarket'
    )
    return conn