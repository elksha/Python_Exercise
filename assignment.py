# 데이터 타입 연습문제
listD = ['Life', 'is', 'too', 'short']
print(" ".join(listD))

# 컨트롤 연습문제
# shirt

# 컨트롤 연습문제
star = 0
while star < 4:
    star = star + 1
    print('*'*star)

# 컨트롤 연습문제
moum = 0
mutsa = "mutzangesazachurum"
for q in mutsa:
    if q == 'a' or q == 'u' or q == 'e' or q == 'i' or q == 'o':
        moum = moum + 1
print(moum)

#1-1. while문을 활용하여 1000이하의 자연수
# 중 3의 배수의 합을 구해보세요 (% 활용)

a = 0
b = 0
while a < 1000:
    a += 1
    if a%3 == 0:
        b += a
print(b)

#1-2. while문을 활용하여 *을 10개부터 1개까지 출력

c = 10
while c > 0:
    print('*'*c)
    c -= 1

#1-3. A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# 여기서 50점 이상의 점수들의 총합 (list의 pop)

d = 0
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
while len(A) > 0:
    e = A.pop()
    if e > 50:
        d += e
print(d)

#2-1. For문을 활용하여 1부터 100까지의 숫자를 출력

f = 0
for i in range(1, 101):
    f += 1
    print(f)

#2-2. For문을 활용하여 A학급의 평균점수 (list의 len)
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

g = 0
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for j in A:
    g += j
    h = g/len(A)
print(h)

#2-3. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드
'''
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''
# 코드를 리스트 내포를 이용하여 표현
numbers = [1, 2, 3, 4, 5]
result = [k*2 for k in numbers if k%2 == 1]