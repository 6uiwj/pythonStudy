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

