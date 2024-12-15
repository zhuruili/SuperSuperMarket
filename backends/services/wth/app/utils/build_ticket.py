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
#ALTER TABLE item
#ADD UNIQUE (kind);


        # 创建用户表
        cursor.execute('''
create table ticket(
	ticket_ID int primary key,	
	kind int,					
	store int,					
	info varchar(200),			
	discount float,				
	create_time date,			
	due_time date				
	
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
    create_database()
    #insert_product()