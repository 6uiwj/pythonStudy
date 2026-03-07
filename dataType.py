#숫자형
#제곱
a = 3
b = 4
print(a**b)

#나누기
print(7/4)

#몫
print(7//4)



a=3
b=4
print(a+b)

#문자형
multililne = """
Lfe is too short
you need python"""

print(multililne)

#문자열 연산
#문자열 더하기
head = "Python"
tail = " is fun!"
print(head+tail)

#문자열 곱하기
a = "python"
print(a*2)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

sentence = "You need python"
print(sentence)

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3]) #e

#문자열 인덱싱 활용하기
print(a[0]) #L
print(a[12]) #s
print(a[-1]) #n - 뒤에서부터 읽기
print(a[-2]) #o
print(a[-5]) #y

#문자열 슬라이싱 [x,y)
b = a[0] + a[1] + a[2] + a[3]
print(b) #Life
print(a[0:4]) #Life

print(a[19:]) #19번부터 그 문자열의 끝까지
print(a[:17]) #문자열의 처음부터 17번까지
print(a[:]) #처음부터 끝까지
print(a[19:-7]) #19번부터 -8까지

#슬라이싱으로 문자열 나누기
a = "20260307Sunny"
data = a[:8]
weather = a[8:]
print(data)
print(weather)

a = "Pithon"
#a[1] = 'y' #불가능 <- 문자열의 요솟값은 바꿀 수 없다. 문자열 = 변경 불가능한 자료형
print(a[:1]+'y' + a[2:])

#문자열 포매팅
#1. 숫자 바로 대입
print("I ate %d apples." % 3)

#2. 문자열 바로 대입
print("I ate %s apples." % "five")

#3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I ate %d apples." % number)

#4 2개 이상의 값 넣기
number = 10
day = "three"
print("I eat %d apples per %s days." % (number, day))

#문자열 포맷 코드
"""
%s : 문자열(String)
%c : 문자 1개(Character)
%d : 정수(Integer)
%f : 부동 소수(floating-point)
%o : 8진수
%x : 16진수
%% : Literal %(문자 %자체)
"""

print("Error is %d%%. " % 98)

#포맷 코드와 숫자 함께 사용하기
#1. 정렬과 공백
print("%10s" % "hi") #전체 길이가 10개인 문자열 공간에 값을 오른쪽 정렬하고 나머지는 공백으로 채움
print("%-10sjane." % 'hi') #hi를 왼쪽으로 정렬하고 나머지 공백으로 채움 + jane

#2. 소수점 표현하기
print("%0.4f" % 3.42134234)
