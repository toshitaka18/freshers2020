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
        print('数字並べ替えプログラム')
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
    print(Thanks_message.statment)