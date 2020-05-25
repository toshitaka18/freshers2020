# 提供用ソース　※このまま使ってください。

class MenuDto:
    __my = None
    menuno = ""
    itemnm = ""
    category = ""
    categorynm = ""
    price = 0
    itemdesc = ""

    # コンストラクタ
    def __init__(self, menuno, itemnm, category, price, itemdesc, categorynm):
        self.menuno = menuno
        self.itemnm = itemnm
        self.category = category
        self.price = price
        self.itemdesc = itemdesc
        self.categorynm = categorynm

    def getMenuno(self):
        return self.menuno

    def getItemnm(self):
        return self.itemnm

    def getCategory(self):
        return self.category

    def getCategorynm(self):
        return self.categorynm

    def getPrice(self):
        return self.price

    def getItemdesc(self):
        return self.itemdesc
