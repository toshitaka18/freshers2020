from message import Error_message, Thanks_message

class Calc_sort:
    def sort_number(self, app1_string, app1_amount):
        if app1_amount >= 2 and app1_amount <= 5:  # 数字の個数が2~5の場合とそれ以外で場合分け
            app1_list = []
            for i in range(1, app1_amount + 1):
                sort_number = int(input(str(i) + "つ目"))
                if sort_number <= 100:
                    app1_list.append(sort_number)  # app1_listに対して、appendで要素を一つずつ追加
                else:
                    return Error_message.statment

            if app1_string == 'y':  # 昇順か降順かで場合わけ
                print('昇順に並び替えます')
                app1_list.sort()  # sortで昇順に並び替える。返される値はNone、なので結果を表示するにはprint(list名)
                return app1_list, Thanks_message.statment  # 並び替え結果とメッセージを戻り値として返す。

            elif app1_string != 'y':
                print('降順に並び替えます')
                app1_list.sort(reverse=True)  # reverseキーワードをTrueとすると降順が可能。
                return app1_list, Thanks_message.statment  # 並び替え結果とメッセージを戻り値として返す。
        else:
            return Error_message.statment  # メッセージのみ返す。


