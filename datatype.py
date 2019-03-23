# 한줄 주석 처리 입니다.

"""
여러 줄 주석 처리입니다.
"""

# 블록을 잡으신 후 Ctrl ? 하셔도 주석 처리됩니다.

'''
1. 숫자형
정수 : 123, 0, -55
실수 : 123.55, -33.12
8진수 & 16진수는 생략
'''

a = 15
print(a)

b = 15.03
print(b)

# 사칙연산이 가능합니다
c = 10
d = 5
print(c+d)
print(c-d)
print(c*d)
print(c/d)

'''
2. 문자형
문자형은 ''혹은 ""으로 감싸서 표현합니다.
'''
str1 = 'hello'
str2 = 'world'

print(str1, str2)

# 문자열 연산
print(str1 + str2)
print(str1 * 3)

'''
이스케이프 문자
\n == 엔터 키
\t == tab 키
\" == "큰 따옴표"
\' == '작은 따옴표'
\\ == \
'''

print("오늘 강의는" + "\'파이썬\'" + "\n입니다")

# 문자열 인덱싱
text = "hello world"
print(text[0])
print(text[1])

# 문자열 슬라이싱
print(text[0:5])

'''
3. 불 자료형
참/거짓을 나타내는 자료형입니다.
True와 False가 있습니다.
'''
a = True
print(a)
b = False
print(b)

c = 1<3
print(c)
d = 1>3
print(d)

'''
4-1. 리스트 자료형
타 언어의 '배열'과 같은 의미를 지닙니다.
array = [] #비어있는 리스트
array = [1, 2, 3] #숫자형 리스트
array = ['hello', 'world'] #문자형 리스트
array = ['hello', 1, 2, 3] #혼합형 리스트
array = [1, 2, [4, 5]] #다중 리스트

리스트 안에는 모든 자료형이 다 들어갈 수 있습니다
'''

# 리스트 인덱싱 & 슬라이싱
list1 = ['hello', 'python', 'java', 'c++', [1, 2, 3]]
print(list1[0])
print(list1[0:2])
print(list1[4][0])

#리스트의 연산
# + : 리스트의 합
# * : 리스트의 반복
list2 = [1, 2]
list3 = [3, 4]
print(list2 + list3)
print(list3 * 3)

#리스트의 수정, 삭제, 삽입

#수정
listA = ['a', 'b', 'c']
print(listA[0])
listA[0] = 'change'
print(listA[0])

#삭제
listB = ['a', 'b', 'c']
del listB[0]
print(listB[0])

#삽입
listC = ['a', 'b', 'c']
listC.append('d')
print(listC)

#연습문제
listD = ['Life', 'is', 'too', 'short']
print(" ".join(listD))

#4-2. 튜플 자료형
tuple1 = (1, 2)
tuple2 = ('a', 'b', 'c')

'''
리스트와의 차이점
1. [] vs ()
2. 튜플 내의 값은 변경, 삭제 삽입이 불가! (리스트는 가능)
'''

#튜플 말구 리스트 쓰세요!!

'''
4-3. 딕셔너리 자료형
{Key1:Value1, Key2:Value2, Key3:Value3, ...}

Key와 Value의 짝으로 이루어진다
Key에는 '변하지 않는' 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있습니다
동일한 Key는 2개 이상 존재할 수 없고, Key에는 리스트는 사용할 수 없음(튜플은 가능)
Value에는 모든 자료형이 가능합니다.
'''

#딕셔너리 생성 예시
dic1 = {'이름' : '홍길동', '나이' : 22, '학교' : '고려대학교'}
print(dic1)

#key를 사용하여 value 얻기
print(dic1['이름'])
print(dic1['나이'])

#key, value 리스트 얻기
keylist = list(dic1.keys())
print(keylist)
valuelist = list(dic1.values())
print(valuelist)

#key, value 튜플형 리스트 얻기
keyvalue = list(dic1.items())
print(keyvalue)

'''
우리가 고등학교 때 배운 '집합과 정확히 같은 개념
특징:
요소의 중복을 허용하지 않는다.
순서가 없다.
'''
list1 = ['1', '2', '3', '4', '5']
print(list1)
setNum = set(['1', '2', '3', '4', '5'])
print(setNum)
#얘는 순서와 관계 없이 나오게 된다. 딕셔너리도 이건 마찬가지이긴 함.
#딕셔너리나 집합은 순서가 없으니 인덱스 기능을 사용할 수 없다.
# 고로 집합을 리스트나 튜플 형식으로 변환한다면 사용할 수 있겠죠?
#list(set), tuple(set)을 사용하면 인덱스 기능을 사용할 수 있다.

#집합의 생성
#사용방법: set([요소1, 요소2, 요소3]) // set('문자열')
setNumber = set([1, 2, 3, 4, 5])
setStr = set(['1', '2', '3', '4', '5'])
setStr2 = set('Good Morning')

print(setStr)

#인덱스 사용하려면 튜플 또는 리스트 형식으로 변경 후 사용.

setNum = set(['1', '2', '3', '4', '5'])
print(setNum)
list2 = list(setNum)
print(list2[1])
tuple1 = tuple(setNum)

'''
set1, set2
1. 차집합(-): set1- set2 or set1.difference(set2)
2. 교집합(&): set1 & set2 or set1.intersection(set2)
3. 합집합(|): set1 | set2 or set1.union(set2)
4. 대칭차집합(^): set1 ^ set2 or set1.symmetric_difference(set2)
'''
set1 = set('Good Morning')
set2 = set('GoodNight')
#1. 차집합
print(set1-set2)
print(set1.difference(set2))
#2. 교집합 (&)
print(set1&set2)
print(set1.intersection(set2))
#3. 합집합
print(set1|set2)
print(set1.union(set2))
#4. 대칭차집합(^): set1^set2 or set1.symmetric_difference(set2)사용.
print(set1^set2)
print(set1.symmetric_difference(set2))
