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

def create_table():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='super_supermarket'
    )
    cursor = conn.cursor()

    # 创建商品表
    cursor.execute('''
        create table item(
            item_ID int primary key,	/*商品ID*/
            title varchar(500),			/*商品名称*/
            pic_url varchar(200),		/*商品图片*/
            sale varchar(50),			/*上坪销量*/
            price float,				/*商品价格*/
            shop_name varchar(100),		/*店铺名称*/
            store int,					/*库存数量*/
            kind int unique,			/*商品种类*/
            url varchar(500)			/*商品详情链接*/
        );
    ''')

    # 创建用户表
    cursor.execute('''
        create table IF NOT EXISTS users(
            user_ID int primary key,			/*用户ID*/
            userName varchar(500) not null,		/*用户名*/
            passwords varchar(12) not null,		/*密码*/
            state int		/*用户状态*/
        );
    ''')

    # 创建订单表
    cursor.execute('''
        create table IF NOT EXISTS orders(
            order_ID int primary key,	/*订单ID*/
            user_ID int,		        /*用户ID*/
            item_ID int,		        /*商品ID*/
            state int,			        /*订单状态*/
            price float,		        /*总价格*/
            count int,			        /*订单数量*/
            foreign key (user_ID) references users(user_ID),
            foreign key (item_ID) references item(item_ID)
        );
    ''')

    # 创建券表
    cursor.execute('''
        create table IF NOT EXISTS ticket(
            ticket_ID int primary key,	/*优惠券ID*/
            kind int,					/*商品种类*/
            store int,					/*库存数量*/
            info varchar(200),			/*描述信息*/
            discount float,				/*折扣*/
            create_time date,			/*生效时间*/
            due_time date,				/*过期时间*/
            foreign key (kind) references item(kind)
        );
    ''')
    
    # 创建用户券表
    cursor.execute('''
        create table IF NOT EXISTS userTicket(
            userTicket_ID int primary key,		/*用户券ID*/
            user_ID int,			            /*用户ID*/
            ticket_ID int,			            /*优惠券ID*/
            foreign key (user_ID) references users(user_ID),
            foreign key (ticket_ID) references ticket(ticket_ID)
        );
    ''')

    # 创建购物车表
    cursor.execute('''
        create table IF NOT EXISTS cart(
            cartID int primary key,		/*购物车ID*/
            user_ID int,		        /*用户ID*/
            item_ID int,		        /*商品ID*/
            count int,			        /*要购买商品数量*/
            foreign key (user_ID) references users(user_ID),
            foreign key (item_ID) references item(item_ID)
        );
    ''')

    # 创建店铺表
    cursor.execute('''
        create table IF NOT EXISTS merchandise(
            merchandiseID int primary key,		/*店铺商品ID*/
            user_ID int,		                /*用户ID*/
            item_ID int,		                /*商品ID*/
            foreign key (user_ID) references users(user_ID),
            foreign key (item_id) references item(item_ID)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully.")

if __name__ == "__main__":
    # create_database()
    # insert_product()
    create_table()