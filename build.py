import os
from jinja2 import Environment, FileSystemLoader

# --- 1. 資料設定區 (食材) ---

# 共用設定
site_title = "劍潭・山河新生"

# 首頁資料
index_context = {
    "site_title": site_title,
    "hero_title": "劍潭，緩慢森活。",
    "hero_subtitle": "在喧囂邊緣，尋找一片會呼吸的土地。<br>老屋、山徑、與那些被遺忘的時光。",
    "bus_data": [
        {"route": "203", "time": "即將抵達", "status": "arriving"},
        {"route": "紅3", "time": "約 5 分", "status": "normal"},
    ],
    "aqi": {"value": 35, "status": "優良", "desc": "空氣清澈，適合散步。"},
    "spots": [
        {"name": "劍潭山步道", "tag": "山林"},
        {"name": "神農宮", "tag": "信仰"},
    ]
}

# 歷史頁面資料 (時光顯影)
history_context = {
    "site_title": f"時光顯影 | {site_title}",
    "title": "時光顯影",
    "desc": "每一張泛黃的照片，都是劍潭未曾說完的故事。",
    "photos": [
        {"title": "基隆河畔的擺渡人", "desc": "1960年代，橫越基隆河的日常風景。", "img": "static/圖片1.jpg"}, # 記得放對應圖片
        {"title": "舊士林市場", "desc": "人聲鼎沸的老市場記憶。", "img": "static/圖片1.jpg"},
        {"title": "消失的鐵道", "desc": "淡水線鐵路行經劍潭站的最後身影。", "img": "static/圖片1.jpg"},
    ]
}

# 店家頁面資料 (在地店家 - 原看不見的風景)
shops_context = {
    "site_title": f"在地店家 | {site_title}",
    "title": "在地職人",
    "desc": "走進巷弄，探訪堅持手作溫度的在地好店。",
    "shops": [
        {"name": "山腳咖啡", "tag": "手沖咖啡", "desc": "隱身山邊的老宅咖啡，使用自家烘焙豆。", "img": "static/圖片1.jpg"},
        {"name": "阿婆草仔粿", "tag": "傳統點心", "desc": "每日現做的客家美味，限量供應。", "img": "static/圖片1.jpg"},
        {"name": "劍潭書房", "tag": "獨立書店", "desc": "只賣關於土地與記憶的書。", "img": "static/圖片1.jpg"},
    ]
}

# --- 2. 生成邏輯 (大廚做菜) ---

def build():
    # 設定模板環境
    env = Environment(loader=FileSystemLoader('templates'))
    
    # 定義要生成的頁面清單： (模板檔名, 輸出檔名, 資料)
    pages = [
        ('index.html', 'index.html', index_context),
        ('history.html', 'history.html', history_context),
        ('shops.html', 'shops.html', shops_context),
    ]

    for template_name, output_name, context in pages:
        template = env.get_template(template_name)
        html_output = template.render(context)
        
        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        print(f"✅ {output_name} 生成成功！")

if __name__ == "__main__":
    build()