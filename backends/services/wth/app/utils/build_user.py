import mysql.connector
from mysql.connector import errorcode
import pandas as pd

def create_database():
    try:
        # 连接到 MySQL 服务器
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
        )
        cursor = conn.cursor()

        # 创建数据库
        #cursor.execute("create database ecommerce default character set gbk collate gbk_chinese_ci ")

        # 选择数据库
        cursor.execute("USE ecommerce")

        cursor.execute("""
        ALTER TABLE users MODIFY COLUMN user_ID INT AUTO_INCREMENT;

        """)
        cursor.execute("""
                ALTER TABLE orders MODIFY COLUMN order_ID INT AUTO_INCREMENT;

                """)
        cursor.execute("""
                ALTER TABLE ticket MODIFY COLUMN ticket_ID INT AUTO_INCREMENT;

                """)
        cursor.execute("""
                ALTER TABLE userTicket MODIFY COLUMN userTicket_ID INT AUTO_INCREMENT;

                """)

        # 创建用户表
#         cursor.execute('''
#             create table users(
# 	user_ID int primary key,
# 	userName varchar(500) not null,
# 	passwords varchar(12) not null,
# 	state int
# )
#         ''')

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
            password='1234',
            database='ecommerce'
        )
        cursor = conn.cursor()

        # 读取数据
        path = r"backends\dataset\itemsInfo.csv"
        # cursor.execute('''
        #     LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\itemsInfo.csv' replace
        #     INTO TABLE item
        #     CHARACTER SET gbk
        #     FIELDS TERMINATED BY ','
        #     LINES TERMINATED BY '\r\n';
        # ''')
        df = pd.read_csv(path, header=None, names=['id', 'title', 'pic_url', 'price', 'sale', 'shop_name', 'storage', 'kind', 'url'])
        # 插入数据到数据库
        for _, row in df.iterrows():
            cursor.execute('''
                INSERT IGNORE INTO item (item_Id, title, pic_url, price, sale, shop_name, store, kind, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        print(err)


if __name__ == "__main__":
    create_database()
    #insert_product()