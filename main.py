from message import Error_message, Thanks_exit, Exit_message, Thanks_message
from calc_number import Calc_sort
from beans import Beans
from fortune import Fortune
from ev_bike import Ev_bike
from chinese_food import Chinese_food
from menuDao import MenuDao
from script import *

try:
    app_number = int(input('＊＊＊ プログラミング体験アプリへ ようこそ！＊＊＊ \n'
                           '1 : 数字並べ替えプログラム \n'
                           '2 : 節分豆まきプログラム \n'
                           '3 : 今日の運勢プログラム\n'
                           '4 : 電気自転車充電プログラム \n'
                           '5 : 中華料理注文プログラム \n'
                           '6 : モンスタープログラム \n'
                           '9 : 処理終了 \n'
                           '実行したいプログラム番号を選択してください。(1-6,9)：'))
    if app_number == 1:
        print('＊＊＊＊＊＊＊＊＊＊＊\n'
              '数字並べ替えプログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊')
        app1_string = input('昇順に並べ替えますか？ (y/n) ==>')
        app1_amount = int(input('並べ替えしたい数字の数はいくつですか？(2-5)==> '))

        app1 = Calc_sort()  # インスタンスの生成し変数に代入
        app1.sort_number(app1_string, app1_amount)    # インスタンスに対してインスタンスメソッドを使用。

    elif app_number == 2:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '節分豆まきプログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')
        app2_string = input('今日は節分ですか？(y/n)==>')

        app2 = Beans()  # インスタンスの生成し変数に代入
        app2.beans_sum(app2_string)  # インスタンスに対してインスタンスメソッドを使用。

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
        app3.lucky(user_name)  # インスタンスに対してインスタンスメソッドを使用。

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
                app_4 = Ev_bike(ev_wat)  # インスタンス生成。今回は生成時に引数を渡す。
                app_4.ev_charge()  # インスタンスに対してインスタンスメソッドを使用。
            else:
                print(Error_message.statment)
                print(Thanks_exit.statment)
        else:
            print('')
            print(Exit_message.statment)
            print(Thanks_exit.statment)


    elif app_number == 5:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              '中華料理注文プログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')

        app_5 = MenuDao()  # MenuDaoのインスタンス生成
        result_5a = app_5.getAllMenus()  # getAllMenus()でメニューリスト、recommandedCategory()で本日のおすすめを取得。取得内容を変数へ代入。
        result_5b = app_5.recommandedCategory()
        main_chinese = Chinese_food(result_5a, result_5b)  # Chinese_foodのインスタンスを生成。生成時、上記取得内容を引数として設定。

        main_chinese.order()  # インスタンスに対してインスタンスメソッドを使用。

    elif app_number == 6:
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊\n'
              'モンスタープログラム\n'
              '＊＊＊＊＊＊＊＊＊＊＊＊＊')
        start_flag = int(input("冒険を始めますか?:[1:始める/0:やめる]:"))
        if start_flag != 1:
            print('')
            print(Exit_message.statment)
            print(Thanks_exit.statment)
        else:
            # プレイヤー情報生成
            player_info = set_player()
            # プレイヤー情報取得
            ply_hp = player_info[0]
            ply_atk = player_info[1]
            ply_spd = player_info[2]
            ply_name = player_info[3]


            # 敵情報生成
            enemy_info = set_enemy()
            # 敵情報の取得
            ene_name = enemy_info[0]
            ene_hp = enemy_info[1]
            ene_atk = enemy_info[2]
            ene_spd = enemy_info[3]
            ene_ev = enemy_info[4]

            while True:
                select_mode = int(input("[1:冒険に出かける/2:モンスターの状態を知る/0:休息を取る]:"))
                if select_mode == 0:
                    print('')
                    print(Exit_message.statment)
                    print(Thanks_exit.statment)
                    break
                if select_mode == 2:
                    show_player(player_info)
                else:
                    # 攻撃の順番
                    print("野生の{0}があらわれた!".format(ene_name))
                    # 戦闘開始
                    while ply_hp > 0 and ene_hp > 0:
                        if ply_spd > ene_spd:  # スピードの早いほうが先に攻撃
                            #  主人公のモンスターの攻撃
                            total_atk = calc_dmg(ply_atk, ply_name, ene_name)
                            ene_hp -= total_atk
                            sleep(1)  # 1秒待って戦闘ログを出力
                            #  敵のモンスターの攻撃
                            total_atk = calc_dmg(ene_atk, ene_name, ply_name)
                            ply_hp -= total_atk
                        else:
                            #  敵のモンスターの攻撃
                            total_atk = calc_dmg(ene_atk, ene_name, ply_name)
                            ply_hp -= total_atk
                            sleep(1)  # 1秒待って戦闘ログを出力
                            #  主人公のモンスターの攻撃
                            total_atk = calc_dmg(ply_atk, ply_name, ene_name)
                            ene_hp -= total_atk

                        # 1秒待って戦闘ログを出力
                        sleep(1)
                    player_win_flag = judge(ply_hp, ene_hp)
                    # ゲーム判定
                    if player_win_flag:
                        print("{0}を倒した！おめでとう!{1}は経験値を{2}得た！".format(ene_name,ply_name, ene_ev))
                        print(Thanks_message.statment)
                        break
                    else:
                        print("主人公の{0}は倒れた、、目の前が真っ暗になった、、".format(ply_name))
                        print(Thanks_message.statment)
                        break


    elif app_number == 9:
        print('')
        print(Thanks_exit.statment)

    else:  # 数字の入力ではあるが1~5,9以外の処理
        print(Error_message.statment)
        print(Thanks_exit.statment)
except:
    print(Error_message.statment)
    print(Thanks_exit.statment)