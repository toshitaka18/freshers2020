from message import Error_message, Thanks_message

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
        if app1_string == "y" and app1_amount >= 2 and app1_amount <= 5:
            app1_list = []
            for i in range(1, app1_amount + 1):
                app1_list.append(int(input(str(i) + "つ目")))  # app1_listに対して、appendで要素を一つずつ追加
            print('昇順に並び替えます')
            app1_list.sort()  # sortで昇順に並び替える。返される値はNone、なので結果を表示するにはprint(list名)
            print(app1_list)
            print(Thanks_message.statment)
        elif app1_string != "y" and app1_amount >= 2 and app1_amount <= 5:
            app1_list = []
            for i in range(1, app1_amount + 1):
                app1_list.append(int(input(str(i) + "つ目")))
            print('降順に並び替えます')
            app1_list.sort(reverse=True)  # reverseキーワードをTrueとすると降順が可能
            print(app1_list)
            print(Thanks_message.statment)
        else:
            print(Error_message.statment)
    elif app_number == 2:
        print('節分豆まきプログラム')
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