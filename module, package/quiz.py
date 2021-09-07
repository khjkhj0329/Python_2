# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math
bill = 59827
result_f = round(bill, -2)
print(result_f)
print(bill//100*100)
print(bill-bill%100)
print(math.floor(bill/100)*100)

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
print('-'*20)
score = 56
result = round(score, -1)
print(round(score/10)*10)
print(result)
# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
print('-'*20)
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)
# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
print('-'*20)
import random
list_r = random.sample(range(1, 9 + 1), 3)
print("".join(str(n)for n in list_r))
print("".join(map(str, list_r)))
string = ''
for n in list_r:
    string += str(n)
print(string)
# 5. 내가 태어난 날로부터 며칠이 지났는지?
print('-'*20)
import datetime
now = datetime.datetime.now()
birthday = datetime.datetime(2015, 3, 2, 14, 0)
print(birthday)
print(now - birthday)
# 6. 올해 크리스마스까지 며칠이 남았는지?
print('-'*20)
now1 = datetime.date.today()
christmas_time = datetime.date(2021, 12, 25)
remain_time = christmas_time - now1
print(remain_time)
# 7. 내 생일이 며칠 남았는지?
print('-'*20)
now2 = datetime.date.today()
birthday2 = datetime.date(2022, 3, 29)
remain_time2 = birthday2 - now2
print(remain_time2)
if birthday2 < now2:
    birthday2 = birthday2.replace(year=birthday2.year + 1)
    # birthday2.year = birthday2.year + 1 # not writable
# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
# 마지막 버노가 몇 번인지 묻자

last_number = input("마지막 번호는?")
# 1~마지막번호까지 리스트 만들자
list_class = list(range(1, last_number + 1))
# 무한반복
while True:
#   나간 친구 묻자
    exclude_number = input("뺄 번호는?(그냥 enter치면 끝내자)")
#   리스트에서 빼자
    if exclude_number == '':
        break
    list_class.remove(int(exclude_number))
# 그냥 enter면 반복 끝내자


# 랜덤으로 섞자
# 촐력하자
