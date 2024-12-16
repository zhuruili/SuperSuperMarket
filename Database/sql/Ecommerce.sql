create database ecommerce default character set gbk collate gbk_chinese_ci;
use ecommerce;

-- 用户表
create table users(
	user_ID int AUTO_INCREMENT primary key,			/*用户ID*/
	userName varchar(500) not null,		/*用户名*/
	passwords varchar(12) not null,		/*密码*/
	state int		/*用户状态*/
);

-- 商品表
create table item(
	item_ID int primary key,	/*商品ID*/
	title varchar(500),			/*商品名称*/
	pic_url varchar(500),		/*商品图片*/
	price float,				/*商品价格*/
	sale varchar(50),			/*上坪销量*/
	shop_name varchar(100),		/*店铺名称*/
	store int,					/*库存数量*/
	kind int,					/*商品种类*/
	url varchar(500)			/*商品详情链接*/
);

LOAD DATA INFILE 'D:\\Tools\\MySql\\Data\\MySQL Server 8.0\\Uploads\\itemsInfo.csv' INTO TABLE item
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'; 

-- 订单表
create table orders(
	order_ID int AUTO_INCREMENT primary key,	/*订单ID*/
	user_ID int,		/*用户ID*/
	item_ID int,		/*商品ID*/
	state int,			/*订单状态*/
	price float,		/*总价格*/
	count int,			/*订单数量*/
	foreign key (user_ID) references users(user_ID),
    foreign key (item_ID) references item(item_ID)
);

-- 优惠券表
create table ticket(
	ticket_ID int AUTO_INCREMENT primary key,	/*优惠券ID*/
	kind int,					/*商品种类*/
	store int,					/*库存数量*/
	info varchar(200),			/*描述信息*/
	discount float,				/*折扣*/
	create_time date,			/*生效时间*/
	due_time date				/*过期时间*/
);

-- 用户-券表
create table userTicket(
	userTicket_ID int AUTO_INCREMENT primary key,		/*用户券ID*/
	user_ID int,			/*用户ID*/
    ticket_ID int,			/*优惠券ID*/
	foreign key (user_ID) references users(user_ID),
	foreign key (ticket_ID) references ticket(ticket_ID)
);

-- 购物车表
create table cart(
	cartID int AUTO_INCREMENT primary key,		/*购物车ID*/
	user_ID int,		/*用户ID*/
    item_ID int,		/*商品ID*/
    count int,			/*要购买商品数量*/
	foreign key (user_ID) references users(user_ID),
	foreign key (item_ID) references item(item_ID)
);

-- 店铺商品表
create table merchandise(
    merchandiseID int AUTO_INCREMENT primary key,		/*店铺商品ID*/
	user_ID int,		/*用户ID*/
    item_ID int,		/*商品ID*/
    foreign key (user_ID) references users(user_ID),
    foreign key (item_id) references item(item_ID)
);


-- 触发器：
DELIMITER $$

CREATE TRIGGER before_insert_userTicket
BEFORE INSERT ON userTicket
FOR EACH ROW
BEGIN
    -- 检查库存是否足够
    DECLARE available_stock INT;

    SELECT store INTO available_stock
    FROM ticket
    WHERE ticket_ID = NEW.ticket_ID;

    IF available_stock <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '库存不足';
    END IF;

    -- 扣减库存
    UPDATE ticket
    SET store = store - 1
    WHERE ticket_ID = NEW.ticket_ID;
END$$

DELIMITER ;


-- view
-- 为 kind = 1 创建视图
CREATE VIEW item_kind1 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 1;

-- 为 kind = 2 创建视图
CREATE VIEW item_kind2 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 2;

-- 为 kind = 3 创建视图
CREATE VIEW item_kind3 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 3;

-- 为 kind = 4 创建视图
CREATE VIEW item_kind4 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 4;

-- 为 kind = 5 创建视图
CREATE VIEW item_kind5 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 5;

-- 为 kind = 6 创建视图
CREATE VIEW item_kind6 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 6;

-- 为 kind = 7 创建视图
CREATE VIEW item_kind7 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 7;

-- 为 kind = 8 创建视图
CREATE VIEW item_kind8 AS
SELECT *
FROM supersupermarket.item
WHERE kind = 8;

-- 权限
grant INSERT, Delete, Select, Update
on ecommerce.item
to 'lzr'@'localhost';

-- 并发控制
use ecommerce;
set session transaction ISOLATION level read committed;
set @@autocommit=0;
select @@tx_isolation;



-- 过程函数：
DELIMITER $$

CREATE PROCEDURE AddItemAndMerchandise(
    IN p_item_id INT,
    IN p_title VARCHAR(255),
    IN p_pic_url VARCHAR(255),
    IN p_price DECIMAL(10, 2),
    IN p_sale INT,
    IN p_shop_name VARCHAR(255),
    IN p_store INT,
    IN p_kind VARCHAR(255),
    IN p_url VARCHAR(255),
    IN p_user_id INT
)
BEGIN
    -- 插入数据到 item 表
    INSERT INTO item (item_ID, title, pic_url, price, sale, shop_name, store, kind, url)
    VALUES (p_item_id, p_title, p_pic_url, p_price, p_sale, p_shop_name, p_store, p_kind, p_url);

    -- 插入数据到 merchandise 表
    INSERT INTO merchandise (user_ID, item_ID)
    VALUES (p_user_id, p_item_id);
END$$

DELIMITER ;