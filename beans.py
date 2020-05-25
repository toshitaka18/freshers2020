from message import Error_message, Thanks_message, Exit_message

class Beans():
    def beans_sum(self, app2_string):
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