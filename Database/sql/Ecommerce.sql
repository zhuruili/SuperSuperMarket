create database ecommerce default character set gbk collate gbk_chinese_ci;
use ecommerce;

-- 用户表
create table users(
	user_ID int primary key,			/*用户ID*/
	userName varchar(500) not null,		/*用户名*/
	passwords varchar(12) not null,		/*密码*/
	state int		/*用户状态*/
);

-- 商品表
create table item(
	item_ID int primary key,	/*商品ID*/
	title varchar(500),			/*商品名称*/
	pic_url varchar(200),		/*商品图片*/
	price float,				/*商品价格*/
	sale varchar(50),			/*上坪销量*/
	shop_name varchar(100),		/*店铺名称*/
	store int,					/*库存数量*/
	kind int,					/*商品种类*/
	url varchar(500)			/*商品详情链接*/
);

-- 订单表
create table orders(
	order_ID int primary key,	/*订单ID*/
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
	ticket_ID int primary key,	/*优惠券ID*/
	kind int,					/*商品种类*/
	store int,					/*库存数量*/
	info varchar(200),			/*描述信息*/
	discount float,				/*折扣*/
	create_time date,			/*生效时间*/
	due_time date,				/*过期时间*/
	foreign key (kind) references item(kind)
);

-- 用户-券表
create table userTicket(
	userTicket_ID int primary key,		/*用户券ID*/
	user_ID int,			/*用户ID*/
    ticket_ID int,			/*优惠券ID*/
	foreign key (user_ID) references users(user_ID),
	foreign key (ticket_ID) references ticket(ticket_ID)
);

-- 购物车表
create table cart(
	cartID int primary key,		/*购物车ID*/
	user_ID int,		/*用户ID*/
    item_ID int,		/*商品ID*/
    count int,			/*要购买商品数量*/
	foreign key (user_ID) references users(user_ID),
	foreign key (item_ID) references item(item_ID)
);

-- 店铺商品表
create table merchandise(
    merchandiseID int primary key,		/*店铺商品ID*/
	user_ID int,		/*用户ID*/
    item_ID int,		/*商品ID*/
    foreign key (user_ID) references users(user_ID),
    foreign key (item_id) references item(item_ID)
);