#파이썬의 함수 구조
"""
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
"""

def add(a,b):
    return a+b

a = 3
b = 4
c = add(3,4)
print(c)

#매개변수와 인수
## 매개변수: 함수에 입력으로 전달된 값을 받는 변수
## 인수: 함수를 호출할 때 전달하는 입력값

def add(a,b): # 매개변수
    return a + b
print(add(3,4)) #인수

#입력값과 리턴값에 따른 함수의 형태
##입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

#리턴값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3,4)

#입력값도 리턴값도 없는 함수
def say():
    print('Hi')

say()

#매개변수를 지정하여 호출하기
def sub(a,b):
    return a-b
result = sub(a=7,b=3)
print(result)

result = sub(b=7,a=3)
print(result)

#입력값이 몇 개가 될지 모를 때
"""
def 함수_이름(*매개변수):
    수행할_문장
"""
##여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)


result = add_mul('mul', 1,2,3,4,5)
print(result)

#키워드 매개변수, kwargs -> 딕셔너리 형태로 저장
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

#함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) #튜플로리턴 -> 7,12

result1, result2 = add_and_mul(3,4) #각각 리턴
print(result1)
print(result2)

def add_and_mul(a,b):
    return a + b
    return a * b #함수는 리턴값이 하나이므로 반영되지 않음

##return의 또다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보') #return이 실행되어 함수를 빠져나옴

#매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True): #초기값 설정 - 항상 맨 뒤쪽에 놓아야 함 (name, man=True, age 불가)
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)

#함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a+1
vartest(a)

print(a) #1

a = 1
def vartest(a):
    a = a+1
vartest(3)

print(a)

#함수 안에서 함수 밖의 변수를 변경하는 방법
##1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

##2 global 명령어 사용하기
a = 1
def vartest():
    global a #함수 밖의 a를 직접 사용하겠다는 의미
    a = a+1

vartest()
print(a)

#lambda 예약어
##함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용할_표현식
add = lambda a, b: a+b
result = add(3,4)
print(result)