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
            print(' ')
            total_beans = 0
            for name, age in zip(names, ages):
                print('*** {0}は豆を{1}粒食べました。 ***'.format(name, str(age)))
                total_beans += age
            print(' ')
            if total_beans < 100:
                print('100粒目の豆を食べたひとはいません。')
            else:
                count_beans = 0
                for name1, age1 in zip(names, ages):
                    count_beans += age1
                    if count_beans >= 100:
                        print('100粒目の豆を食べたひとは、{0}です。 '.format(name1))
                        break
                    else:
                        continue

                count_beans1 = 0
                for name2, age2 in zip(names, ages):
                    count_beans1 += age2
                    if count_beans1 >= 200:
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