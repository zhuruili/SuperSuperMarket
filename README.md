# SuperSupermarket

![language](https://img.shields.io/badge/Language-Python-blue)
![license](https://img.shields.io/badge/License-MIT-red)
![database](https://img.shields.io/badge/Database-MySQL-green)

一款简易的购物Web应用

A simple shopping web application

---

## Todo List

>项目开发期临时交流的公告栏

### Phase-1

项目初期的准备与分工。

1. 爬取的具体数据项汇总/得分点对应（√）
2. 数据库设计（L+W+C）
3. 图形绘制（Z）
4. 数据爬取[.backends/crawler]并写入数据库（L）
5. 前端设计与实现（W+C）

### Phase-2

前后端的结合与细节功能实现。

## 数据爬取

商品信息来源为某宝，数据写入csv文件以便后续建立数据库，含有以下数据项：

1. id--商品ID，根据商品条目数累加
2. title--商品名/显示标题
3. piclink--图片URL
4. price--售价
5. sold--购买人数
6. shopname--店铺名
7. shopid--店铺id
8. storage--库存
9. category--类别
10. pluslink--详情链接
