

class Store:
    def __init__(self, name):
        self.name = name
        self.item1 = {1: 'item1', "価格": 10, "在庫": 15}
        self.item2 = {2: "item2", "価格": 20, "在庫": 10}
        self.item3 = {3: "item3", "価格": 30, "在庫": 5}

# ここから下のまとめ方が思いつきません。
    def buy_item1(self, sensei, number):
        if sensei.students[number].total_point >= self.item1["価格"] and self.item1["在庫"] > 0:
            sensei.students[number].total_point = sensei.students[number].total_point - self.item1["価格"]
            self.item1["在庫"] -= 1
            sensei.students[number].bags.append(self.item1[1])
            print("残りのポイント{0}pt".format(sensei.students[number].total_point))
            print("持ち物は{0}\n".format(sensei.students[number].bags))

        elif sensei.students[number].total_point < self.item1["価格"]:
            print("ポイントが足りません\n")

        elif self.item1["在庫"] <= 0:
            print("在庫がありません\n")

        else:
            print('該当の商品は見つかりませんでした')

    def buy_item2(self, sensei, number):
        if sensei.students[number].total_point >= self.item2["価格"] and self.item2["在庫"] > 0:
            sensei.students[number].total_point = sensei.students[number].total_point - self.item2["価格"]
            self.item2["在庫"] -= 1
            sensei.students[number].bags.append(self.item2[2])
            print("残りのポイント{0}pt".format(sensei.students[number].total_point))
            print("持ち物は{0}\n".format(sensei.students[number].bags))

        elif sensei.students[number].total_point < self.item2["価格"]:
            print("ポイントが足りません\n")

        elif self.item2["在庫"] <= 0:
            print("在庫がありません\n")

        else:
            print('該当の商品は見つかりませんでした')

    def buy_item3(self, sensei, number):
        if sensei.students[number].total_point >= self.item3["価格"] and self.item3["在庫"] > 0:
            sensei.students[number].total_point = sensei.students[number].total_point - self.item3["価格"]
            self.item3["在庫"] -= 1
            sensei.students[number].bags.append(self.item3[3])
            print("残りのポイント{0}pt".format(sensei.students[number].total_point))
            print("持ち物は{0}\n".format(sensei.students[number].bags))

        elif sensei.students[number].total_point < self.item3["価格"]:
            print("ポイントが足りません\n")

        elif self.item3["在庫"] <= 0:
            print("在庫がありません\n")

        else:
            print('該当の商品は見つかりませんでした')
