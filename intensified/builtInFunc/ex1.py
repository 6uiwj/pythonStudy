#abs
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([]))

#any
any([1,2,3,0])

any([9, ""])
any([])

#chr
print(chr(97))
print(chr(44032))


#dir
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod
print(divmod(7,3))

#enumerate - 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력받아 인덱스 값을 포함하는 enumerate 랙체 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#eval - 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))

#filter
#filter(함수, 반복_가능한_데이터) - 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서 리턴
##기존
def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))

##filter 사용
def positive(x):
    return x > 0
print(list(filter(positive, [1,-3,2,0,-5,6])))

##lambda 사용
print(list(filter(lambda x: x>0, [1,-1,2,0,-5,6])))

#hex - 정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))

#id - 객치를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수
a=3
print(id(3))
print(id(a))

b = a
print(id(b))

#input([prompt]) - 사용자 입력을 받는 함수
#a = input()
#print(a)
#b = input("Enter: ")
#print(b)

#int - 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴
print(int('3'))
print(int(3.4))

#int(x, radix)  - radix진수로 표현된 문자열 x를 10진수로 변환하여 리턴
print(int('11',2)) # 2진수로 구성된 11을 10진수로 변환

print(int('1A', 16))

#isInstance(object, class) - 입력받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True 거짓이면 False 반환
class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b,  Person))

#len(s) - 입력값 s의 길이(요소의 전체 개수) 리턴
print(len("python"))

print(len([1,2,3]))

print(len((1, 'a'))) #(1,'a')로 구성된 튜플의 길이

#list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴
print(list("python"))
print(list((1,2,3)))

#list 함수에 리스트를 입력하면 똑같은 리스트를 복사하여리턴
a = [1,2,3]
b = list(a)
print(b)

#max
print(max([1,2,3]))
print(max("python"))

#min
print(min([1,2,3]))
print(min("python"))

#oct(x) - 정수를 8진수 문사열로 바꾸어 리턴
print(oct(34))
print(oct(12345))

#open(filename, [mode]) - '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 리턴하는 함수
'''
mode |        설명
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
 w   |  쓰기 모드로 파일 열기
 r   |  읽기 모드로 파일 열기
 a   |  추가 모드로 파일 열기
 b   |  바이너리 모드로 파일 열기
'''
#f = open("binary_file","rb") # 바이너리 읽기 모드

#ord(c) - 문자의 유니코드 숫자 값을 리턴하는 함수
print(ord('a'))
print(ord('가'))

#pow(x,y) - x를 y제곱한 결괏값 리턴
print(pow(2,4))
print(pow(3,3))

#range([start], stop, [step]) - for문과 함께 자주 사용, 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴

##인수가 하나인 경우 - 0부터 시작
print(list(range(5)))

##인수가 2개일 경우
print(list(range(5,10)))

##인수가 3개일 경우
print(list(range(1,10,2)))
print(list(range(0, -10, -1)))

#round(number,[ndigits]) - 반올림
print(round(4.6))
print(round(4.2))
print(round(5.768,2))

#sorted(iterable) - 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴
print(sorted([3,1,2]))
print(sorted(['a','c','b']))
print(sorted("zero"))
print(sorted((3,2,1)))

#str(obj) - 문자열 형태로 객체를 변환하여 리턴
print(str(3))
print(str('hi'))

#sum(iterable)
print(sum([1,2,3]))
print(sum((4,5,6)))

#tuple(iterable) - 반복 가능한 데이터를 튜플로 바꾸어 리턴
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#type
print(type("abc"))
print(type([]))
print(type(open("test", 'w')))

#zip(*iterable) - 동일한 개수로 이루어진 데이터들을 묶어서 리턴
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc", "def")))


