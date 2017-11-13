import teacher
import student
import parent

num = 0
loop = 0

people = input('人数を入力→\n')
people = int(people)

sensei = teacher.Teacher('たろう', 0)

for i in range(people):
    oya = parent.Parent('name', 0, 'none')
    oya.set_name('parent_' + str(i))
    seito = student.Student('none', 'none', 0, 0, 'none', 'none')
    seito.set_sid(str(i))
    seito.set_name('student_' + str(i))
    sensei.set_score()
    seito.set_score(sensei.get_score())
    oya.set_judge(seito.get_score())
    seito.set_parent_name(oya.get_name())
    seito.set_total_point(oya.get_point())
    seito.set_result_judge(oya.get_judge())
    sensei.add_student(seito)

exam = 1
print('-----第{0}回目のテスト結果-----'.format(exam))
print('-----{0}先生の採点-----\n'.format(sensei.name))
print('全体の人数は：{0}人'.format(len(sensei.students)))
print('全体の平均は：{0}点\n'.format(sensei.avecal()))

sensei.maxcalc()
sensei.mincalc()

print('最高得点は：{0}点'.format(max(sensei.scores)))

for i in sensei.max_students:

    print('{0}'.format(i.name))

print('\n---------------\n')

print('最低得点は：{0}点'.format(min(sensei.scores)))

for i in sensei.min_students:

    print('{0}'.format(i.name))

print('\n---------------\n')

while num == 0:

    number = input('検索したい生徒の番号を入力→')
    number = int(number)

    if number < len(sensei.students):
        print('\n生徒ID.{0}'.format(sensei.students[number].sid))
        print('名前は{0}'.format(sensei.students[number].name))
        print('テストの点数は{0}点'.format(sensei.students[number].score))
        print('{0}さんの評価は{1}'.format(sensei.students[number].parents, sensei.students[number].result_judge))
        print('取得したポイントは{0}pt\n'.format(sensei.students[number].total_point))
        print('検索を続ける場合は、[0]を押して下さい')
        print('終了する場合は、[1]を押して下さい')
        print('テストを続行する場合は、[2]以上を押して下さい')

    else:
        print('該当のIDは見つかりませんでした')
        continue

    num = input()
    num = int(num)

    if num == 1:
        loop = 1
        break

    elif num >= 2:
        print('テストを実施')
        sensei.clear_list()
        exam += 1
        continue

while loop == 0:
    num = 0
    for i in range(people):
        sensei.set_score()
        sensei.students[i].set_score(sensei.get_score())
        oya.set_judge(sensei.students[i].get_score())
        sensei.students[i].set_total_point(oya.get_point())
        sensei.students[i].set_result_judge(oya.get_judge())

    sensei.maxcalc()
    sensei.mincalc()

    print('-----第{0}回目のテスト結果-----'.format(exam))
    print('-----{0}先生の採点-----\n'.format(sensei.name))
    print('全体の人数は：{0}人'.format(len(sensei.students)))
    print('全体の平均は：{0}点\n'.format(sensei.avecal()))

    print('最高得点は：{0}点'.format(max(sensei.scores)))

    for i in sensei.max_students:

        print('{0}'.format(i.name))

    print('\n---------------\n')

    print('最低得点は：{0}点'.format(min(sensei.scores)))

    for i in sensei.min_students:

        print('{0}'.format(i.name))

    print('\n---------------\n')
    while num == 0:
        number = input('検索したい生徒の番号を入力→')
        number = int(number)

        if number < len(sensei.students):
            print('\n生徒ID.{0}'.format(sensei.students[number].sid))
            print('名前は{0}'.format(sensei.students[number].name))
            print('テストの点数は{0}点'.format(sensei.students[number].score))
            print('{0}さんの評価は{1}'.format(sensei.students[number].parents, sensei.students[number].result_judge))
            print('取得したポイントは{0}pt\n'.format(sensei.students[number].total_point))
            print('検索を続ける場合は、[0]を押して下さい')
            print('終了する場合は、[1]を押して下さい')
            print('テストを続行する場合は、[2]以上を押して下さい')

        else:
            print('該当のIDは見つかりませんでした')
            continue

        num = input()
        num = int(num)

        if num == 1:
            loop = 1
            break

        elif num >= 2:
            print('テストを実施')
            sensei.clear_list()
            loop = 0
            exam += 1
            continue

print('\n-------END--------')
