from flask import jsonify
from app import app, get_db
import random

@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    # 生成 18 个随机的 itemID
    random_ids = random.sample(range(1, 12001), 18)
    format_strings = ','.join(['%s'] * len(random_ids))

    # 查询这些随机 itemID 对应的记录
    cursor.execute(f'SELECT * FROM item WHERE item_ID IN ({format_strings})', tuple(random_ids))
    selected_items = cursor.fetchall()
    conn.close()

    return jsonify(selected_items)