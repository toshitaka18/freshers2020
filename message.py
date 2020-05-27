class Error_message(Exception):
    statment = ('\n'
                '！！！！！！！！！！！！！！！！！！！！ \n'
                '不正な値が入力されました。処理を終了します。\n'
                '！！！！！！！！！！！！！！！！！！！！ \n')

class Thanks_message:
    statment = ("\n" 
               "ご利用ありがとうございました。")

class Exit_message(Exception):
    statment = ('\n'
                '終了します。'
                '\n')

class Name_error_message(Exception):
    statment = ('！！！！！！！！！！！！！！！！！！！\n'
                '名前の入力がなかったため、処理を終了します。\n'
                '！！！！！！！！！！！！！！！！！！！\n')