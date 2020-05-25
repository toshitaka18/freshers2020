from message import Error_message, Thanks_message, Exit_message, Name_error_message
from calc_number import Calc_sort
from beans import Beans
import random

try:
    app_number = int(input('＊＊＊ プログラミング体験アプリへ ようこそ！＊＊＊ \n'
                           '1 : 数字並べ替えプログラム \n'
                           '2 : 節分豆まきプログラム \n'
                           '3 : 今日の運勢プログラム\n'
                           '4 : 電気自転車充電プログラム \n'
                           '5 : 中華料理注文プログラム \n'
                           '9 : 処理終了 \n'
                           '実行したいプログラム番号を選択してください。(1-5,9)：'))
    if app_number == 1:
        print('＊＊＊＊＊＊＊＊＊＊＊\n'
              '数字並べ替えプログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊\n')
        app1_string = input('昇順に並べ替えますか？ (y/n) ==>')
        app1_amount = int(input('並べ替えしたい数字の数はいくつですか？(2-5)==> '))

        app1 = Calc_sort()  # インスタンスの生成しxに代入
        result_1 = app1.sort_number(app1_string, app1_amount)  # インスタンスメソッドによって得た戻り値をresult_1に代入
        if len(result_1) == 2:  # 戻り値の中身が二つあれば、それぞれ表示。そうでなければ1つだけ表示
            print(result_1[0])
            print(result_1[1])
        else:
            print(result_1)

    elif app_number == 2:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '節分豆まきプログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')
        app2_string = input('今日は節分ですか？(y/n)==>')

        app2 = Beans()
        result_2 = app2.beans_sum(app2_string)

    elif app_number == 3:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '今日の運勢プログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')

        count_name = 0
        while count_name < 3:
            user_name = input('あなたの名前を入力してください。==> ')
            if user_name:
                break
            else:
                count_name += 1
        if user_name:
            lucky_number = random.randint(1, 11)
            if lucky_number == 1:
                print('{0}さんの運勢は、大吉です。おめでとうございます！'.format(user_name))
            elif lucky_number == 2 or lucky_number == 3:
                print('{0}さんの運勢は、吉です。'.format(user_name))
            elif lucky_number == 4 or lucky_number == 5:
                print('{0}さんの運勢は、小吉です。'.format(user_name))
            elif lucky_number == 6:
                print('{0}さんの運勢は、凶です。ファイト！'.format(user_name))
            else:
                print('{0}さんの運勢は、中吉です。'.format(user_name))
            print(Thanks_message.statment)
        else:
            print(Name_error_message.statment)
    elif app_number == 4:
        print('電気自転車充電プログラム')
    elif app_number == 5:
        print('中華料理注文プログラム')
    elif app_number == 9:
        print('プログラムを終了します')
    else:
        print(Error_message.statment)
except:
    print(Error_message.statment)
finally:
    print('またのご利用お待ちしております。\n')