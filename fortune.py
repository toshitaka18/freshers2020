import random
from message import Thanks_message, Name_error_message, Thanks_exit

class Fortune():
    def lucky(self, user_name):
        if user_name:  # user_nameが存在するかどうかで条件分け
            lucky_number = random.randint(1, 11)  # 1~10の間でランダムの数を生成し変数に代入。
            if lucky_number == 1:
                print('{0}さんの今日の運勢は、大吉です。おめでとうございます！'.format(user_name))
            elif lucky_number == 2 or lucky_number == 3:
                print('{0}さんの今日の運勢は、吉です。'.format(user_name))
            elif lucky_number == 4 or lucky_number == 5:
                print('{0}さんの今日の運勢は、小吉です。'.format(user_name))
            elif lucky_number == 6:
                print('{0}さんの今日の運勢は、凶です。ファイト！！'.format(user_name))
            else:
                print('{0}さんの運勢は、中吉です。'.format(user_name))
            print(Thanks_message.statment)
        else:
            print(Name_error_message.statment)
            print(Thanks_exit.statment)