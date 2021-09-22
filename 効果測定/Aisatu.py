import datetime

def aisatu():
    now = datetime.datetime.now()
    nowWeek = now.weekday()
    nowWeek_name = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    print('こんにちは。', '今日は', now.month, now.day, nowWeek, 'です。')

aisatu()