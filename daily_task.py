"""
POLITICO 每日任务入口脚本
用于 GitHub Actions 环境
"""
import os
import sys
import glob
from datetime import datetime
import pytz

# Step 1: 抓取新闻
print("Step 1: 抓取新闻...")
import rss_parser
rss_parser.main()

# Step 2: 仅翻译今日的文章（EST 时区）
print("Step 2: 仅翻译今日文章...")
tz_est = pytz.timezone('America/New_York')
today = datetime.now(tz_est).strftime("%Y%m%d")
dailynews_file = os.path.join("dailynews", f"{today}.md")

if os.path.exists(dailynews_file):
    print(f"Found today's file: {dailynews_file}")
    import translate_news
    translate_news.translate_file(dailynews_file)
else:
    print(f"No today's news file: {dailynews_file}")
    # 显示可用的文件
    files = glob.glob("dailynews/*.md")
    print(f"Available files: {sorted(files)[-5:]}")

# Step 3: 仅发送今日的翻译邮件
print("Step 3: 发送今日邮件...")
translate_file_path = os.path.join("translate", f"{today}.md")
if os.path.exists(translate_file_path):
    print(f"Found translated file: {translate_file_path}")
    import send_email
    send_email.main(translate_file_path)
else:
    print(f"No translated file for today, skipping: {translate_file_path}")

print("每日任务执行完毕")
