class Error_message(Exception):
    statment = ('\n'
                '！！！！！！！！！！！！！！！！！！！！ \n'
                '不正な値が入力されました。処理を終了します。\n'
                '！！！！！！！！！！！！！！！！！！！！\n')

class Thanks_message:
    statment = ("\n" 
               "ご利用、ありがとうございました。\n"
                "またのご利用をお待ちしております。 \n")

class Thanks_exit:
    statment = ('またのご利用をお待ちしております。 \n')

class Exit_message(Exception):
    statment = ('終了します。'
                '\n')

class Name_error_message(Exception):
    statment = ('！！！！！！！！！！！！！！！！！！！\n'
                '名前の入力がなかったため、処理を終了します。\n'
                '！！！！！！！！！！！！！！！！！！！\n')