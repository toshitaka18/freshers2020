from message import Error_message, Thanks_message, Exit_message

class Beans():
    def beans_sum(self, app2_string):
        if app2_string == 'y':
            names = ['じいちゃん', 'ばあちゃん', 'とうちゃん', 'かあちゃん', 'おれ', 'いもうと']
            ages = []  # 年齢を入れる空リスト作成
            for i in range(len(names)):  # namesリストの要素の数だけfor文を回す
                demo_age = int(input(names[i] + 'の年齢==>'))  # 101歳以上の入力を拒否するために、1度変数に代入。
                ages.append(demo_age)  # appendで要素を順に追加。
                if demo_age > 100:  # 101歳以上の入力がされた場合プログラムが終了する。
                    exit()
            print(' ')  # 空行追加
            total_beans = 0
            for name, age in zip(names, ages):  # 二つのリストから二つの変数に順に代入。
                print('*** {0}は豆を{1}粒食べました。 ***'.format(name, str(age)))
                total_beans += age  # 粒数合計をカウント
            print(' ')  # 空行追加
            if total_beans < 100:  # 粒数合計が100未満の場合のメッセージを表示。
                print('100粒目の豆を食べたひとはいません。')
            else:
                #  100粒の判定のために、再度forを回す。
                count_beans = 0
                for name1, age1 in zip(names, ages):
                    count_beans += age1
                    if count_beans >= 100:  # 合計が100粒を超えた時点でループを抜ける。
                        print('100粒目の豆を食べたひとは、{0}です。 '.format(name1))
                        break
                    else:
                        continue
                #  200粒の判定のために、再度forを回す。
                count_beans1 = 0
                for name2, age2 in zip(names, ages):
                    count_beans1 += age2
                    if count_beans1 >= 200:  # 合計が200粒を超えた時点でループを抜ける。
                        print('200粒目の豆を食べたひとは、{0}です。 '.format(name2))
                        break
                    else:
                        continue

            print('家族全員で食べた豆の数は{0}粒です。'.format(total_beans))
            print(Thanks_message.statment)
        elif app2_string == 'n':
            print(Exit_message.statment)
        else:
            print(Error_message.statment)