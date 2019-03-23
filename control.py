'''
인덴테이션!!!!!!!!!!!!

if 조건문:
    실행문1
    실행문2
else:
    실행문1
    실행문2
'''

number = 1

if number == 1:
    print('참입니다')
else:
    print('거짓입니다')

#비교연산자
'''
a > b: 크다
a < b: 작다
a == b: 같다
a >= b: 크거나 같다
a <= b: 작거나 같다
a != b: 같지 않다
'''

#논리연산자 (and, or, not)
'''
and: a and b --> True 나오는 경우: a와 b가 모두 참일 경우
or: a or b --> True가 나오는 경우: a 또는 b가 True일 경우, 둘 다 False일 경우 False.
not: not a --> a가 True면 false되고, a가 False이면 True
'''

number1 = 100
number2 = 200
number3 = 300
number4 = 400

a = number1 > number2 #이거슨 거짓
b = number3 < number4 #이거슨 참

if a:
    print('True')
else:
    print('False')

if a and b: #둘 중 하나라도 거짓이면 False
    print('True')
else:
    print('False')

'''
다중 if 문
if <조건문>:
    실행문:
else:
    if <조건문>:
        실행문:
    else:
        실행문:
이렇게 else문에 대해 또 다른 if와 else가 발생하는 경우.

elif문

if <조건문>:
    실행문1:
elif <조건문>:
    실행문1:
else:
    실행문1:
'''

list1 = ['a', 'b']

if 'a' in list1:
    print('a가 있습니다.')
else:
    if 'b' in list1:
        print('b가 있습니다.')
    else:
        print('a와 b가 모두 없습니다.')

if 'a' in list1:
    print('a가 있습니다.')
elif 'b' in list1: #else: 하고 if <조건문>: 이 부분을 그냥 elif <조건문>으로 변경.
    print('b가 있습니다.')
else:
    print('a와 b가 모두 없습니다.')

'''
pass하면 실행문을 실행하지 않고 그냥 넘어갈 때.
'''
list1 = ['a', 'b']

if 'a' in list1:
    pass
else:
    print('a가 없습니다.')

#한줄로 만들기
if 'a' in list1:
    print("있습니다.")
    print("진짜 있습니다.")
else:
    print('없습니다.!')
# 이거를 세미콜론 쓰면 한 줄로 만들 수 있음.
if 'a' in list1: print("있습니다."); print("진짜 있습니다.")
else: print('없습니다.!')

'''
while <조건문>:
    실행문1
    실행문2
'''

#열번 찍어 안 넘어 가는 나무는 없다
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

'''
1. 숫자 포맷팅; 인풋으로는 %d, value는 %숫자로 표시.
    a. 일반적인 숫자
    오늘은 12월 %d 이다.
    b. 변수형 숫자; 인풋으로는 %d, value: %변수
'''
print('오늘은 12월 %d일이다.' %27) #일반적인 숫자
day = 28
print('오늘은 12월 %d일이다.' %day) #이게 변수형 숫자. 즉 변수를 대입할 것이고 그 변수가 나타내는 숫자가 있을 때.

'''
2. 문자 포맷팅:
    a. 일반문자 --> input: %s value: %문자

    b. 변수형 문자 --> input:
                            %s: 문자열
                            %d: 정수형
                            %f: 소수점형
                            %c: 문자
                      value: %변수
'''
print('%s은 %s를 배우고 있습니다.' %('오늘', 'python')) #이게 일반적인 문자

subject = '창업'
print('오늘은 %s를 배우고 있습니다.' %subject)

#쓰까보기
print('%s는 %d월 %d일 입니다.' %('내일', 12, 27))

'''
while True:
    실행문 #실행문이 계속해서 돈다. 얘를 멈추기 위해 if, break를 사용.
    if 조건문:
        break #여기서 강제 종료
        continue #다시 while로 돌아가게 됨. 뒤에 부분 실행하지 않고 바로 while로 돌아감.
'''
# 1부터 5까지 출력해보세요
num1 = 0
while num1 < 10:
    num1 += 1
    print(num1)
    if num1 == 5:
        break

#1부터 10까지 숫자 중 홀수를 출력해보세요
num2 = 0
while num2 < 10:
    num2 += 1
    if num2 % 2 == 0:
        continue
    print(num2)

'''
for문의 기본적인 구조는 다음과 같습니다

for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''

#예제 1
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#예제 2
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#continue와 break는 그대로 사용이 가능합니다.
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)
    if i == 5:
        break

#1부터 10까지 숫자 중 홀수를 출력해보세요
list2 = [1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if i % 2 ==0:
        continue
    print(i)

'''
리스트는 매번 설정하기 번거로우므로 for문은 숫자 리스트를 자동으로 만들어 주는 range라는 함수를 사용합니다.

range(초기값, 마지막값, 증가값)
위와 같은 형태로 표현하고, 증가값은 디폴트가 +1, 마지막값은 포함이 되지 않습니다.
'''

a = range(0,10)
print(a[9])
a = range(0,10,1)
print(a[9])
a = range(0,10,2)
print(a[1])

#기본
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

#리스트 내포 이용
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

#[1,2,3,4] 중에서 짝수인 2와 4에만 3을 곱하여 담고 싶다면 if 문을 사용!
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

'''
리스트 내포의 일반적인 문법은 다음과 같다. "if 조건문" 부분은 앞의 예제에서 볼 수 있듯이 생략할 수 있다.
[표현식 for 항목 in 반복가능객체 if 조건문]
'''
'''
조금 복잡하지만 for문을 2개 이상 사용하는 것도 가능하다. for문을 여러 개 사용할 때의 문법은 다음과 같다.
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
'''
