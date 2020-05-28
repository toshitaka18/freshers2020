from message import Thanks_message
import datetime


today = datetime.date.today().weekday()  # 本日は何曜日か取得
days = ["月", "火", "水", "木", "金", "土", "日"]  # 曜日リスト

class Chinese_food:
    def __init__(self, result_5a, result_5b):  # コンストラクタ
        self.result_5a = result_5a
        self.result_5b = result_5b
        print('  いらっしゃいませ。 ==== メニューリスト ==== ')
        # for文を使用し、メニューリストを順に表示。メニュー名の縦列を揃えるために、iの数値によって空白の数を変更している。改善の余地あり。
        for i in range(len(self.result_5a)):
            if i == 6:
                print('メニューNo.%s[%s]： %s … %s円 【%s】' % (self.result_5a[i].menuno, self.result_5a[i].categorynm, self.result_5a[i].itemnm,self.result_5a[i].price, self.result_5a[i].itemdesc))
            elif i == 1 or i == 5:
                print('メニューNo.%s[%s]：  %s … %s円 【%s】' % (self.result_5a[i].menuno, self.result_5a[i].categorynm, self.result_5a[i].itemnm,self.result_5a[i].price, self.result_5a[i].itemdesc))
            else:
                print('メニューNo.%s[%s]：    %s … %s円 【%s】' % (self.result_5a[i].menuno, self.result_5a[i].categorynm, self.result_5a[i].itemnm,self.result_5a[i].price, self.result_5a[i].itemdesc))

        print(' ')
        print('==== 本日（{0}曜日）のおすすめは「{1}」です。===='.format(days[today], self.result_5b.categorynm))

    def order(self, app5_menu):  # メニューの受付
        #  入力されたメニュー番号を整数の0~6に直す。それ以外はエラー処理
        #  扱いやすい数字に直す以外現時点では方法が思いつかず。修正の余地あり。
        if app5_menu == '11' or app5_menu == '21' or app5_menu == '31' or app5_menu == '41' or app5_menu == '51' or app5_menu == '61' or app5_menu == '71':
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
                  '入力されたメニュー番号は存在しません。メニュー番号＝{0}\n'
                  '！！！！！！！！！！！！！！！！！！！！！！！！'.format(app5_menu))
        # 入力されたメニュー番号（0~6に直したもの）と曜日の数値が一致すれば1割引きを行う。
        if app5_menu == today:
            print(' ')
            print('\n==== ご注文内容は以下の通りです。 ==== \n'
                  'メニュー番号：{0}\n注文名：{1}\n価格：{2}円'
                  .format(self.result_5a[app5_menu].menuno, self.result_5a[app5_menu].itemnm,
                          round(self.result_5a[app5_menu].price * 0.9)))
            print('※本日おすすめは1割引きです！ \n''==== ご注文を承りました。 ====')
            print(Thanks_message.statment)
        else:
            print(' ')
            print('==== ご注文内容は以下の通りです。 ==== \n'
                  'メニュー番号：{0}\n注文名：{1}\n価格：{2}円'
                  .format(self.result_5a[app5_menu].menuno, self.result_5a[app5_menu].itemnm,
                          self.result_5a[app5_menu].price))
            print('==== ご注文を承りました。 ====')
            print(Thanks_message.statment)
