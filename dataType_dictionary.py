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

#딕셔너리 관련 함수
##key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

for k in a.keys():
        print(k)

##key 객체 리스트로 변환하기
print(list(a.keys()))

# value 리스트 만들기 - values
print(a.values())

#key, value 쌍 얻기 - items
print(a.items())

##key:value 쌍 모두 지우기 - clear
a.clear()
print(a)

##key로 value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
###없는 요소를 가져올 경우 a['key'] -> 오류 발생 , a.get('key')는 None 리턴

##딕셔너리 안에 찾으려는 key가 없을 경우 미리 정해준 디폴트 값을 대신 가져오도록 하기 = get(x, '디폴트값')
print(a.get('nokey', 'foo'))

##해당 key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a) #true
print('email' in a) #false


#예제 다음 표를 딕셔너리로 만드시오
'''
   항목     ㅣ     값
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
   name    ㅣ     홍길동 
   birth   ㅣ     1128
   age     ㅣ     30  
'''
a = {
        'name' : '홍길동',
        'birth' : '1128',
        'age' : 30
}
print(a)