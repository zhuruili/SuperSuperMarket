import mysql.connector
from mysql.connector import errorcode
import pandas as pd

def create_database():
    try:
        # 连接到 MySQL 服务器
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
        )
        cursor = conn.cursor()

        # 创建数据库
        cursor.execute("CREATE DATABASE IF NOT EXISTS super_supermarket")

        # 选择数据库
        cursor.execute("USE super_supermarket")

        # 创建商品表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(500) NOT NULL,
                pic_url VARCHAR(200) NOT NULL,
                price FLOAT NOT NULL,
                sale VARCHAR(50),
                shop_name VARCHAR(500),
                storage INT,
                kind INT,
                url VARCHAR(500)
            )
        ''')

        conn.commit()
        cursor.close()
        conn.close()
        print("Database and table created successfully.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def insert_product():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='super_supermarket'
        )
        cursor = conn.cursor()

        # 读取数据
        path = 'backends\\dataset\\itemsInfo.csv'
        df = pd.read_csv(path, header=None, names=['id', 'title', 'pic_url', 'price', 'sale', 'shop_name', 'storage', 'kind', 'url'])

        # 填充空值
        df = df.fillna('')

        # 插入数据到数据库
        for _, row in df.iterrows():
            cursor.execute('''
                INSERT IGNORE INTO products (id, title, pic_url, price, sale, shop_name, storage, kind, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        print(err)

if __name__ == "__main__":
    # create_database()
    insert_product()