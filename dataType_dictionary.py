##딕셔너리 = 자바의 Map

dic = { 'name' : 'pey',
        'phone': '010-9999-1234',
        'birth' : '1118'}

a = {'a' : [1,2,3]} #value에 list 넣기


#딕서녀리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리에서 key를 사용해 Value 얻기
grade = {'pey' :10, 'julliet':99 }
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])


dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리를 만들 때 주의사항
##key는 고유값, 중복된 key값을 설정하면 하나를 제외한 나머지의 것들이 모두 무시된다.
a = { 1:'a', 1:'b' }
print(a) #{1: 'b'}


##key는 불변값 => list 불가능 / 튜플 가능
