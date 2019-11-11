from aip import AipSpeech
import requests

"""
本文原创：pk哥
公众号：Python知识圈（id：PythonCircle）
「Python知识圈」公众号定时分享大量有趣有料的 Python 爬虫和实战项目，值得你的关注。
关注后回复1024免费领取学习资料！
"""

def get_msg():
    url = 'http://open.iciba.com/dsapi/'   # 金山词霸每日一句 api 链接
    html = requests.get(url)
    content = html.json()['content']   # 获取每日一句英文语句
    note = html.json()['note']   # 获取每日一句英文的翻译语句
    return content, note


APP_ID = '输入你的APP_ID'
API_KEY = '输入你的API_KEY'
SECRET_KEY = '输入你的SECRET_KEY'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 中文：zh 英文：en

content, note = get_msg()
print(content)
print(note)

result = client.synthesis(note, 'zh', 1, {
    'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio6.mp3', 'wb') as f:
        f.write(result)

