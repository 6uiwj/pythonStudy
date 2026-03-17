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