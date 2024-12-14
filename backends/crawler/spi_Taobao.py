"""
淘宝商品信息爬取，以csv暂存，数据后续将存入数据库
商品预计条目数：1w+
商品类别数：8
Chrome remote port：9222
类别条目及链接：
    1. [电脑](https://s.taobao.com/search?page=1&q=%E7%94%B5%E8%84%91&tab=all)
    2. [手机](https://s.taobao.com/search?page=1&q=%E6%89%8B%E6%9C%BA&tab=all)
    3. [女装](https://s.taobao.com/search?page=1&q=%E5%A5%B3%E8%A3%85&tab=all)
    4. [食品](https://s.taobao.com/search?page=1&q=%E9%A3%9F%E5%93%81&tab=all)
    5. [宠物](https://s.taobao.com/search?page=1&q=%E5%AE%A0%E7%89%A9&tab=all)
    6. [美妆](https://s.taobao.com/search?page=1&q=%E7%BE%8E%E5%A6%86&tab=all)
    7. [鲜花](https://s.taobao.com/search?page=1&q=%E9%B2%9C%E8%8A%B1&tab=all)
    8. [图书](https://s.taobao.com/search?page=1&q=%E5%9B%BE%E4%B9%A6&tab=all)
"""

from DrissionPage import ChromiumPage
import time
import random
import re
import json
from DataRecorder import Recorder

# 链接容器
linkDict = {
    '电脑':'https://s.taobao.com/search?page=1&q=%E7%94%B5%E8%84%91&tab=all',
    '手机':'https://s.taobao.com/search?page=1&q=%E6%89%8B%E6%9C%BA&tab=all',
    '女装':'https://s.taobao.com/search?page=1&q=%E5%A5%B3%E8%A3%85&tab=all',
    '食品':'https://s.taobao.com/search?page=1&q=%E9%A3%9F%E5%93%81&tab=all',
    '宠物':'https://s.taobao.com/search?page=1&q=%E5%AE%A0%E7%89%A9&tab=all',
    '美妆':'https://s.taobao.com/search?page=1&q=%E7%BE%8E%E5%A6%86&tab=all',
    '鲜花':'https://s.taobao.com/search?page=1&q=%E9%B2%9C%E8%8A%B1&tab=all',
    '图书':'https://s.taobao.com/search?page=1&q=%E5%9B%BE%E4%B9%A6&tab=all'
}

# 参数设置
port = 9222 # Chrome remote port
SearchItem = "电脑"  # 搜索内容
listener = 'h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0'  # 监听器
itemLink = linkDict[SearchItem]  # 商品链接
nextPageBtn = 'css:button.next-btn.next-medium.next-btn-normal.next-pagination-item.next-next'
json_data = {}  # 存放数据
SaveOrNot = False  # 是否保存数据,如果不保存就填False
SAVEPATH = "backends\dataset"  # 数据保存路径
data_list = []  # 存放待保存数据
Pages = 10  # 爬取页数

# 功能函数
def random_sleep():
    """小睡一下"""
    time.sleep(random.randint(1, 3))  # 随机等待

def get_data(resp):
    """提取数据,返回json数据"""
    try:
        resp_re = re.findall(pattern=' mtopjsonp\d+\((.*)\)',string=resp)[0]  # 使用正则提取json数据
        # print(resp_re) 
    except:
        print("正则匹配失败，网站或已更新，请手动调整正则表达式")
        resp_re = resp
    

    json_data = json.loads(resp_re)  # 转换json数据
    return json_data

def get_items(json_data):
    """解析json数据"""
    data_list.clear()  # 清空数据,防止重复
    itemArr = json_data['data']['itemsArray']
    for item in itemArr:
        title = item['title']
        price = item['price']
        nick = item['nick']
        sale = item['realSales']
        # 还可以增加更多数据，这里我懒得写了
        print(f'商品名称：{title}，价格：{price}，店铺：{nick},销量：{sale}')
        data_list.append([title,price,nick,sale])

def save_data(data_list,page):
    """保存数据"""
    if SaveOrNot:
        FilePath = SAVEPATH + "\\" + SearchItem + ".xlsx"  
        r = Recorder(FilePath)
        if page == 0:
            r.add_data(['商品名称','价格','店铺','销量'])
        r.add_data(data_list)
        r.record()
        print("数据已保存")
    else:
        print("数据未保存")

if __name__ == "__main__":
    cp = ChromiumPage(addr_or_opts=port)  # 接管浏览器

    cp.listen.start(listener)  # 启动监听

    cp.get(itemLink)
    
    for p in range(Pages):
        if p == 0:
            resp = cp.listen.wait()  # 等待监听响应
            cp.ele(locator=nextPageBtn, timeout=1).click() # page+=1
            print("------**第一页数据跳过**------")
            continue # skip first page
        print(f"------**正在爬取第{p+1}页数据**------")
        resp = cp.listen.wait()  # 等待监听响应
        # print(resp._raw_body)  # 输出响应，观察结构方便后续数据提取
        resp = resp._raw_body  
        json_data = get_data(resp)  # 提取数据
        # print(json_data)
        get_items(json_data)  # 解析数据

        # save_data(data_list,p)  # 保存数据
        random_sleep()
        cp.ele(locator=nextPageBtn, timeout=1).click()
        
        print(f"------**第{p+1}页数据爬取完毕**------")

    print("------**Spider Done**------")