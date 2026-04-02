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