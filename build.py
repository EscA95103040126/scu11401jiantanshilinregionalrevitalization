import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# 1. 準備資料 (模擬從資料庫或 API 抓取的數據)
context = {
    "site_title": "劍潭・山河日誌",  # 改個比較文青的名字
    "hero_title": "劍潭，緩慢森活。",
    "hero_subtitle": "在喧囂邊緣，尋找一片會呼吸的土地。<br>老屋、山徑、與那些被遺忘的時光。",
    "bus_data": [
        {"route": "203", "time": "即將抵達", "status": "arriving"},
        {"route": "紅3", "time": "約 5 分", "status": "normal"},
        {"route": "304", "time": "約 12 分", "status": "normal"},
    ],
    "aqi": {
        "value": 35,
        "status": "優良",
        "desc": "今日空氣清澈，適合沿著中山北路散步，或登上劍潭山遠眺。"
    },
    "spots": [
        {"name": "劍潭山步道", "tag": "山林"},
        {"name": "神農宮", "tag": "信仰"},
        {"name": "雙溪河畔", "tag": "水岸"},
        {"name": "士林紙廠", "tag": "記憶"},
    ]
}

def build():
    # 設定模板環境
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    # 渲染 HTML
    html_output = template.render(context)

    # 輸出成 index.html (GitHub Pages 的入口)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"✅ 網頁生成成功！時間：{datetime.now()}")

if __name__ == "__main__":
    build()