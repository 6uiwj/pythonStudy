odd = [1, 3, 5, 7, 9]
a= []
b = [1, 2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1,2, ['Life', 'is']]
a = [1,2,3]
print(a)
print(a[0])
print(a[0]+a[2])
print(a[-1])

a=[1,2,3, ['a','b','c']]

print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a = [1,2,['a', 'b', ['Life','is']]]
print(a[2][2][0])


#리스트 슬라이싱
a= [1,2,3,4,5]
print(a[0:2])

b=a[:2]
c=a[2:]
print(b)
print(c)
print(a[1:3])

a= [1,2,3, ['a','b','c'], 4,5]
print(a[2:5]) #[3, ['a','b','c'], 4]
print(a[3][:2]) #['a','b']

#리스트 연산하기
##리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a+b) #1,2,3,4,5,6

##리스트 반복하기
a = [ 1,2,3]
print(a*3)

##리스트 길이 구하기
a = [1,2,3]
print(len(a))

a = [1,2,3]
print(str(a[2])+"hi") #3hi

#리스트의 수정과 삭제
##리스트의 값 수정하기
a = [1,2,3]
a[2] = 4
print(a)

##del 함수를 사용해 리스트의 요소 삭제하기
a = [1,2,3]
del a[1] #삭제 함수 : del 객체
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

#리스트 관련 함수
##리스트에 요소 추가하기 - append
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6]) #[1,2,3,4,[5,6]]
print(a)

##리스트 정렬 - sort
a = [1,4,3,2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

##리스트 뒤집기- reverse (리스트를 역순으로)
a = ['a', 'c', 'b']
a.reverse()
print(a)

##인덱스 반환 - index
a = [1,2,3]
print(a.index(2))
print(a.index(1))

##리스트에 요소 삽입 - insert(a,b) : a 위치에 b 삽입
a = [1,2,3]
a.insert(1,4) #[1,4,2,3]
print(a)

##리스트 요소 제거 - remove(x): 리스트에서 첫번째로 나오는 x를 삭제
a = [1,2,3,1,2,3]
a.remove(2)
print(a) #[1,3,1,2,3]

##리스트 요소 끄집어 내기 - pop : 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제
a = [1,2,3]
print(a.pop()) #3
print(a) #[1,2]

###pop(x): x 번째 요소를 리턴하고 그 요소 삭제
a = [1,2,3]
print(a.pop(1)) #2
print(a) #[1,3]

##리스트에 포함된 요소 x의 개수 세기 - count
a = [1,2,3,1]
print(a.count(1)) #2

##리스트 확장 - extend
a = [1,2,3]
a.extend([4,5])  # == a+[4,5]
print(a) #[1,2,3,4,5]
b= [6,7]
a.extend(b) #[1,2,3,4,5,6,7]
print(a)


"""
append와 extend 차이
 - append : 하나의 객체를 추가
 - extend : iterable의 요소들을 하나씩 풀어서 추가
 
 예시) a = [1,2,3]
    a.append([4,5]) => [1,2,3,[4,5]]
    a.extend([4,5]) => [1,2,3,4,5] 
"""