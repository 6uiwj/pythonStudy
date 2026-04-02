#01
#shirt

#02 3의 배수의 합 구하기
a = 0
answer = 0
while a < 1000:
    a = a + 1
    if a%3 == 0:
        answer += a
    else: continue
print(answer)

#03 별 표시하기
i = 0
while True:
    i = i + 1
    if i > 5: break
    print("*"*i)

#04 1부터 100까지 출력하기
for i in range(1,101):
    print(i)

#05 평균 점수 구하기
# [ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
scores = [ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
score = 0
for i in scores:
    score += i
average = score/len(scores)
print(average)

#6 리스트 컴프리헨션 사용하기
##리스트 요소중 홀수만 골라 2를 곱한 값을 result 리스트에 담는 예제
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 != 0:
        result.append(n*2)
print(result)

##리스트 컴프리헨션으로 바꾸기
result = [n*2 for n in numbers if n % 2 != 0]
print(result)