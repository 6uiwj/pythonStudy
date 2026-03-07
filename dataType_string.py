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

#문자열 슬라이싱 [x,y) 26/03/07
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


#format 함수를 사용한 포매팅 26/03/08
##숫자 바로 대입하기
print("I eat {0} apples".format(3))

## 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

##숫자 값을 가진 변수로 대입하기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

##이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

##인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10,day=3))

##왼쪽 정렬
print("{0:<10}".format("hi")) # :<10 = 왼쪽정렬, 자릿수 10

##오른쪽 정렬
print("{0:>10}".format("hi")) # :>10 = 오른쪽 정렬, 자릿수 10

##가운데 정렬
print("{0:^10}".format("hi")) # :^10 = 가운데 정렬, 자릿수10

##공백 채우기
print("{0:=^10}".format("hi")) # :=^10 = 가운데 정렬, 자릿수10, 공백을 '='로 채움
print("{0:!<10}".format("hi")) # :!<10 = 왼쪽 정렬, 자릿수 10, 공백을 '!'로 채움

#소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y)) #소수점 4자리만 표현
print("{0:10.4f}".format(y)) #소수점 4자리만 표현, 자릿수10

# '{' 또는 '}' 문자 표현하기
print("{{ and }}".format())  # 출력 : { and }



#문자열 포매팅 (v3.6 이상)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.') #딕셔너리형 f 문자열 포매팅

print(f'{"hi":<10}') #왼쪽 정렬, 자릿수10
print(f'{"hi":>10}') #오른쪽 정렬, 자릿수10
print(f'{"hi":^10}') #가운데 정렬, 자릿수10

print(f'{"hi":=^10}') #공백에 문자넣기
print(f'{"hi":!<10}')
print(f'{"hi":@>10}')

print(f'{y:0.4f}')
print(f'{y:!>10.4f}')

print(f'{{and}}')

#예제 -  !!!python!!! 출력하기
print(f'{"python":!^12}')
print("{0:!^12}".format("python"))

#문자열 관련 함수들(문자열 내장함수)
##문자 개수 세기 - count
a = "hobby"
print(a.count('b'))

##위치 알려주기1 -find
a = "Python is the best choice"
print(a.find('b')) #14
print(a.find('k')) #없을 때는 -1 출력

##위치 알려주기2 - index : 찾는 문자열이 없을 때에는 오류 발생
a = "Life is too short"
print(a.index('t'))

##문자열 삽입 - join
print(",".join('abcd')) #a,b,c,d - 각 문자 사이에 ',' 삽입
print(",".join(['a','b','c','d']))

##소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

##대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())

#가장 왼쪽의 연속된 공백 지우기
a = " hi "
print(a.lstrip())

##가장 오른쪽의 연속된 공백 지우기
a = " hi "
print(a.rstrip())

##양쪽 공백 지우기
a = " hi "
print(a.strip())

##문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기 - split
a = "Life is too short"
print(a.split()) #공백을 기준으로 문자열을 나눔 -> 리스트로 반환
b = "a:b:c:d"
print(b.split(':'))

