#변수 만드는 법
a = 1
b = "python"
c = [1,2,3]

print(id(c))

#리스트를 복사하고자 할 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

a[1] = 4
print(a)
print(b)

#복제한 리스트가 다른 주소값을 가리키도록 하기
## 1. [:]이용하기
a = [1,2,3]
b = a[:] #리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1]=4
print(a)
print(b)

##2. copy 모듈 이용하기
from copy import copy #copy모듈 import
a= [1,2,3]
b = copy(a)
print(b is a) #False

##2-1 list 내장 함수 copy 사용
c = a.copy()
print(c is a) #False

#변수를 만드는 여러가지 방법
a, b = ('python', 'life') #튜플
print(a,b)
(a, b) = 'python', 'life' #위와 동일
print((a,b))
[a,b] = ['python', 'life']
print([a,b])
a = b= 'python' #여러 개의 변수에 같은 값 대입

a = 3
b = 5
a, b = b, a #a와 b의 값을 바꿈
print(a, b) #5, 3

#예제
a=[1,2,3]
b = [1,2,3]
print(a is b) #False - 서로 다르 객체