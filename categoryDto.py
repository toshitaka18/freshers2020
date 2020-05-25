# 提供用ソース　※このまま使ってください。
class CategoryDto:
    __my = None
    category = ""
    categorynm = ""
    catflg = 0
    memo = ""

    # コンストラクタ
    def __init__(self, category, categorynm, catflg, memo):
        self.category = category
        self.categorynm = categorynm
        self.catflg = catflg
        self.memo = memo

    def getCategory(self):
        return self.category

    def getCategorynm(self):
        return self.categorynm

    def getCatflg(self):
        return self.catflg

    def getMemo(self):
        return self.memo
