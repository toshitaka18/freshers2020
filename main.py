from message import Error_message, Thanks_message, Exit_message
from calc_number import Calc_sort

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
        if app2_string == 'y':
            names = ['じいちゃん', 'ばあちゃん', 'とうちゃん', 'かあちゃん', 'おれ', 'いもうと']
            ages = []
            for i in range(len(names)):
                demo_age = int(input(names[i] + 'の年齢==>'))
                ages.append(demo_age)
                if demo_age > 100:
                    exit()

            total_beans = 0
            for name, age in zip(names, ages):
                print('*** {0}は豆を{1}個食べた ***'.format(name, str(age)))
                total_beans += age
            if total_beans < 100:
                print('100粒目の豆を食べたひとはいません。')

            print('合計は{0}個です'.format(total_beans))
            print(Thanks_message.statment)
        elif app2_string == 'n':
            print(Exit_message.statment)
        else:
            print(Error_message.statment)
    elif app_number == 3:
        print('今日の運勢プログラム')
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