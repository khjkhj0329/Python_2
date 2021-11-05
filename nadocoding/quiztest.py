# Quiz1-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# id_number = 020316 일 때
# <출력 예시>
# 02
# 0316
# 632
# id_number = '020316'
# year = id_number[0:2]
# month_day = id_number[2:6]
# print(year)
# print(month_day)
# print("둘의 곱:" + str(int(year)) * str(int(month_day)))
#
# print("-------------------")

# Quiz1-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# phone_number = 02-1234-5678 또는 032-9876-4321
# <출력 예시>
# 02 또는 032
# 5678 또는 4321
# phone_number = "02-1234-5678"
# phone_number2 = "032-9876-4321"
# x = phone_number2.find('?') #index() 없으면, valueError   , find() 없으면 -1
# print(phone_number[0:x])
# print(phone_number[-4:])
# print(phone_number2[0:3])
# print(phone_number2[-4:])
#
# print("------------")

#전화번호 입력시, -가 있든, -가 없든, 찰떡같이 알아먹기
phone_number1 = '010-1234-5678'
phone_number2 = '01098765432'
phone_number3 = '010 1111 2222'

phone_number = phone_number3
result = phone_number1.replace('-','').replace(' ', '')
print(result)

studnet_number = "2302"
number = studnet_number[1]
number = int(number)
# if number==1:
#     print("{number}반 뉴미디어소프트웨어과")
# elif number == 2:
#     print("{number}반 뉴미디어소프트웨어과")
# elif number == 3:
#     print("{number}반 뉴미디어웹솔루션과")
# elif number == 4:
#     print("{number}반 뉴미디어웹솔루션과")
# elif number ==5:
#     print("{number}반 뉴미디어디자인과")
# elif number ==6:
#     print("{number}반 뉴미디어디자인과")
# else:
#     print("잘못 입력하셨습니다")
# majors = ['뉴미디어소프트웨어과', '뉴미디어스프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f'{number}반 {majors[number-1]}')
majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
if 1 <= number <= 6:
    print(f'{number}반 {majors[(number-1) // 2]}')
else:
    print("잘못입력했습니다.")

def get_major(student_number):
    global majors
    grade = student_number[0]
    if student_number[1] == '1' or student_number[1] == '2':  #student_number[1] == '3'
        major = "뉴미디어소프트웨어과"                            # '4' == True
    elif student_number[1] == '3' or student_number[1] =='4':
        major = "뉴미디어웹솔루션과"
    elif student_number[1] == '5' or student_number[1] =='6':
        major = "뉴미디어디자인과"
    return grade, major
grade, major = get_major("2100")
print(major,grade)
'''
인수에 개수에 상관없이 인수를 숫자로 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
print(averate(10, 20,30))
print(averate(4, 24))
'''
# 평균 = 더한만큼 / 나누면 되잖아요 = 총합 / 개수
def average(*numbers):
    sum_value = 0
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
        return  sum_value / count

print(average(10, 20, 30)) #(10,20,30) ==> numbers
print(average(4, 23))  #(4, 23) ==> numbers

def avarage2(*numbers):
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))   #(10,20,30) ==> numbers
print(average(4, 23))   #(4, 23) ==> numbers

# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # (소수 첫째자리까지 반올림)
# # * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# # 18.5 미만: 저체중
# # 18.5 이상 23 미만: 보통
# # 23 이상 25 미만: 과체중
# # 25 이상: 비만
def get_bmi(height, weight):
    weight /= 100
    return round((weight / height ** 2), 1)

bmi = get_bmi(176, 69)
# print(bmi)
if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('표준')
elif bmi < 25:
    print('비만')
elif 25 <= bmi:
    print('비만')
# 구구단 7단 출력하기
# i : 1~9
for i in range(1, 9 + 1): # i : 1~9
    print(f'7 x {i} = {7 * i}')


#구구단 2~9단 출력하기
for dan in range(2, 10):
    for i in range(1, 9 + 1): # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
# 구구단 2~7단까지 출력하기
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1): # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break
# 구구단 2~7단 출력하되, x1, x3 , x5, x9만 출력하기
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1): # i : 1~9
         if i % 2 == 0:#== 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)