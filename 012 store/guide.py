import parent
import student
import store


class Guide:

    def __init__(self):
        self.exam = 1
        self.num = 0

    def set_people(self, people, sensei):
        for i in range(people):
            self.oya = parent.Parent('name', 0, 'none')
            self.oya.set_name('parent_' + str(i))
            seito = student.Student('none', 'none', 0, 0, 'none', 'none')
            seito.set_sid(str(i))
            seito.set_name('student_' + str(i))
            seito.set_parent_name(self.oya.get_name())
            sensei.add_student(seito)

    def set_score_judge(self, people, sensei):
        for i in range(people):
            sensei.set_score()
            sensei.students[i].set_score(sensei.get_score())
            self.oya.set_judge(sensei.students[i].get_score())
            sensei.students[i].set_total_point(self.oya.get_point())
            sensei.students[i].set_result_judge(self.oya.get_judge())

    def serch_and_nextexm(self, sensei, omise):
        while self.num == 0:
            print('検索する場合は、[1]を押して下さい')
            print('終了する場合は、[2]を押して下さい')
            print('お店に行く場合は、[3]を押して下さい')
            print('テストを続行する場合は、[4]以上を押して下さい')

            self.num = input()
            self.num = int(self.num)

            if self.num == 1:
                number = input('検索したい生徒の番号を入力→')
                number = int(number)

                if number < len(sensei.students):
                    print('\n生徒ID：{0}'.format(sensei.students[number].sid))
                    print('氏名：{0}'.format(sensei.students[number].name))
                    print('今回の採点結果は{0}点'.format(sensei.students[number].score))
                    print('{0}さんの評価「{1}」でした'.format(sensei.students[number].parents, sensei.students[number].result_judge))
                    print('合計ポイントは{0}pt'.format(sensei.students[number].total_point))
                    print('持ち物は{0}\n'.format(sensei.students[number].bags))
                    self.num = 0

                else:
                    print('該当のIDは見つかりませんでした')
                    self.num = 0

            if self.num == 2:
                loop = 1
                return loop

            elif self.num == 3:
                print("{0}です。こんにちは。".format(omise.name))
                print("だれが買い物をしますか？")
                number = input('生徒の番号を入力→')
                number = int(number)

                if number < len(sensei.students):
                    print('\n生徒ID：{0}'.format(sensei.students[number].sid))
                    print('氏名：{0}'.format(sensei.students[number].name))
                    print('所持アイテム：{0}'.format(sensei.students[number].bags))
                    print('合計ポイントは{0}pt\n'.format(sensei.students[number].total_point))

                else:
                    print('該当のIDは見つかりませんでした')
                    self.num = 0
                    continue

                while self.num == 3:
                    print("0.買わないで店を出る")
                    print("1.{0} 価格{1}pt 在庫{2}個".format(omise.item1[1], omise.item1["価格"], omise.item1["在庫"]))
                    print("2.{0} 価格{1}pt 在庫{2}個".format(omise.item2[2], omise.item2["価格"], omise.item2["在庫"]))
                    print("3.{0} 価格{1}pt 在庫{2}個".format(omise.item3[3], omise.item3["価格"], omise.item3["在庫"]))
                    buyno = input('購入する商品番号を入力→')
                    buyno = int(buyno)

                    if buyno == 0:
                        self.num = 0

                    elif buyno == 1:
                        omise.buy_item1(sensei, number)
                        continue

                    elif buyno == 2:
                        omise.buy_item2(sensei, number)
                        continue

                    elif buyno == 3:
                        omise.buy_item3(sensei, number)
                        continue

            elif self.num >= 4:
                print('テストを実施します')
                sensei.clear_list()
                self.exam += 1
                self.num = 0
                loop = 0
                return loop


