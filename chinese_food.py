import datetime
from menuDao import MenuDao


print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
      '中華料理注文プログラム\n'
      '＊＊＊＊＊＊＊＊＊＊＊＊＊')
today = datetime.date.today().weekday()
days = ["月", "火", "水", "木", "金", "土", "日"]
print('いらっしゃいませ。 ==== メニューリスト ==== ')
app_5 = MenuDao()
result_5a = app_5.getAllMenus()

for i in range(len(result_5a)):
    print('メニューNo.{0}[{1}]： {2} … {3}円 【{4}】'
          .format(result_5a[i].menuno, result_5a[i].categorynm, result_5a[i].itemnm.ljust(8), result_5a[i].price, result_5a[i].itemdesc))

print(' ')
result_5b = app_5.recommandedCategory()
print('==== 本日（{0}曜日）のおすすめは「{1}」です。===='.format(days[today], result_5b.categorynm))


app5_menu = input('ご注文はお決まりですか？メニュー番号を入力してください。==>')
if app5_menu == '11':
    app5_menu = 0
elif app5_menu == '21':
    app5_menu = 1
elif app5_menu == '31':
    app5_menu = 2
elif app5_menu == '41':
    app5_menu = 3
elif app5_menu == '51':
    app5_menu = 4
elif app5_menu == '61':
    app5_menu = 5
elif app5_menu == '71':
    app5_menu = 6
else:
    print('！！！！！！！！！！！！！！！！！！！！！！！！\n'
          '入力されたメニュー番号は存在しません。メニュー番号＝{0}'.format(str(app5_menu)))
    print('！！！！！！！！！！！！！！！！！！！！！！！！')
    exit()

if app5_menu == today:
    print('\n==== ご注文内容は以下の通りです。 ==== \n'
          'メニュー番号：{0}\n注文名：{1}\n価格：{2}円'
          .format(result_5a[app5_menu].menuno, result_5a[app5_menu].itemnm, round(result_5a[app5_menu].price * 0.9)))
    print('※本日おすすめは1割引きです！ \n''==== ご注文を承りました。 ====')
else:
    print('==== ご注文内容は以下の通りです。 ==== \n'
          'メニュー番号：{0}\n注文名：{1}\n価格：{2}円'
          .format(result_5a[app5_menu].menuno, result_5a[app5_menu].itemnm, result_5a[app5_menu].price))