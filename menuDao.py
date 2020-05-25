# 提供用ソース　※このまま使ってください。
import mysql.connector as my
from menuDto import MenuDto
from categoryDto import CategoryDto

class MenuDao:
    __conn = None
    __cursor = None
    __records = None

    # コンストラクタ
    def __init__(self):

        # MySQL接続
        self.__conn = my.connect(user='root', password='freshers@2020', database='freshers_schema', use_unicode=True, charset="utf8")

    # メニューリストを取得する
    # MenuDtoクラスのリストを返却
    def  getAllMenus(self):
        self.__cursor = self.__conn.cursor()
        statement = "select I.*, C.categorynm from item As I inner join category As C on I.category = C.category;"
        self.__cursor.execute(statement)
        self.__records = self.__cursor.fetchall()

        menulist = []
        for record in self.__records:
            menulist.append(MenuDto(record[0], record[1], record[2], int(record[3]), record[4], record[5]))
        self.__cursor.close
        return menulist

    # 本日のおすすめカテゴリを取得する
    # CategoryDtoクラスを返却する
    def recommandedCategory(self):
        statement = None
        self.__cursor = self.__conn.cursor()
        statement = "select * from category where weekday(now()) = catflg;"
        self.__cursor.execute(statement)
        self.__records = self.__cursor.fetchall()
        self.__cursor.close
        for record in self.__records:
            return CategoryDto(record[0], record[1], record[2],  record[3])


