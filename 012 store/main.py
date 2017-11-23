import teacher
import guide
import store

loop = 0

people = input('人数を入力→\n')
people = int(people)

sensei = teacher.Teacher('たろう', 0)
annai = guide.Guide()
omise = store.Store("OK STORE")

annai.set_people(people, sensei)

while loop == 0:
    annai.set_score_judge(people, sensei)
    sensei.maxcalc()
    sensei.mincalc()
    sensei.to_string_scoring_result(annai.exam)
    sensei.to_string_maxmin()
    loop = annai.serch_and_nextexm(sensei, omise)

print('\n-------END--------')
