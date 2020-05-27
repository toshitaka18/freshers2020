from message import Error_message, Thanks_message, Exit_message, Name_error_message
from calc_number import Calc_sort
from beans import Beans
from fortune import Fortune
from ev_car import Ev_car
from chinese_food import Chinese_food
import datetime

from menuDao import MenuDao
from menuDto import MenuDto
from categoryDto import CategoryDto

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
              '＊＊＊＊＊＊＊＊＊＊＊')
        app1_string = input('昇順に並べ替えますか？ (y/n) ==>')
        app1_amount = int(input('並べ替えしたい数字の数はいくつですか？(2-5)==> '))

        app1 = Calc_sort()  # インスタンスの生成し変数に代入
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

        app2 = Beans()  # インスタンスの生成し変数に代入
        result_2 = app2.beans_sum(app2_string)  # インスタンスメソッドによって得た戻り値をresult_2に代入

    elif app_number == 3:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '今日の運勢プログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')

        count_name = 0
        while count_name < 3:  # while文を最大三回回す。
            user_name = input('あなたの名前を入力してください。==> ')
            if user_name:  # 三回以内に名前が入力されたら（user_nameが存在したら）while文を抜ける。
                break
            else:
                count_name += 1  # 名前が入力されない場合はカウントを１増やす

        app3 = Fortune()  # インスタンスの生成し変数に代入
        result_3 = app3.lucky(user_name)  # インスタンスメソッドによって得た戻り値をresult_3に代入

    elif app_number == 4:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '電気自動車充電プログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('電気自転車「J-chary」は、1kwあたり1.5km走ることができます。 ')
        app4_string = input('充電しますか？(y/n)==>')
        # 'y'が入力された場合、'n'が入力された場合とそれ以外で場合分け
        if app4_string == 'y':
            ev_wat = int(input('何キロワット充電しますか？==>'))
            #  201kw以上入力された場合はエラーメッセージを出力しプログラム終了
            if ev_wat <= 200:
                app_4 = Ev_car(ev_wat)  # インスタンス生成。今回は生成時に引数を渡す。
                result_4 = app_4.ev_charge()  # インスタンスメソッドによって得た戻り値をresult_4に代入。
            else:
                print(Error_message.statment)
        elif app4_string == 'n':
            print(Exit_message.statment)
        else:
            print(Error_message.statment)


    elif app_number == 5:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '中華料理注文プログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')

        app_5 = MenuDao()
        result_5a = app_5.getAllMenus()
        result_5b = app_5.recommandedCategory()
        main_chinese = Chinese_food(result_5a, result_5b)

        app5_menu = input('ご注文はお決まりですか？メニュー番号を入力してください。==>')
        result_5 = main_chinese.order(app5_menu)


    elif app_number == 9:
        print('プログラムを終了します')
    else:
        print(Error_message.statment)
except:
    print(Error_message.statment)
finally:
    print('またのご利用お待ちしております。\n')