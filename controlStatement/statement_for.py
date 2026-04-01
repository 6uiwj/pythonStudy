#for문
'''
for 변수 in 리스트 (또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
'''

##전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

##다양한 for 문의 사용
a = [(1,2),(3,4),(5,6)]
for(first, last) in a:
    print(first + last) # 3, 7, 11

##for 문의 응용
"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여주시오.
"""
number = 0
marks = [90, 25, 67, 45, 80]
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

#for문과 continue 문
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a) # range(0,10)

a = range(1,11)
print(a)

##range 함수의 예시 살펴보기
###1부터 10까지 더하기
add = 0
for i in range(1,11):
    add += i

print(add)

number = 0
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

a = 0
for i in range(1, 101):
    a += i
print(a)

##for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end =" ") #end : 줄 끝에 무엇을 붙일지 설정, 기본값 줄바꿈
    print('')


#리스트 컴프리헨션 사용하기
'''
[표현식 for 항목 in 반복_가능_객체 if 조건문]

[표현식 for 항목1 in 반복_가능_객체 if 조건문1
       for 항목2 in 반복_가능_객체 if 조건문2
       ...
       for 항목n in 반복_가능_객체 if 조건문n
]
'''
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

a = [ 1,2,3,4]
result = [num*3 for num in a if num*2==0 ]
print(result)

result = [i*j for i in range(2,10)
          for j in range(1,10)]
print(result)