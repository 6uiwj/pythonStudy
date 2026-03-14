#문자열 복습 문제

#문제1
"""
다음 코드의 출력 결과는? 
a = 5
b = 2

print(a ** b)
print(a / b)
print(a // b)
"""
# 답: 25, 2.5, 2

#문제2
"""
다음 코드의 출력 결과는?
a = "python"
print(a * 3)
"""
# 답: pythonpythonpython

#문제3
"""
문자열의 길이를 구하여라
"Life is too short"
"""
#답: print(len("Life is too short"))

#문제4
"""
다음 문자열에서 마지막 문자를 출력하는 코드를 작성해라.
a = "Python"
"""
#답: print(a[-1])

#문제5
"""
다음 문자열에서 "Life만 출력해라
a = "Life is too short"
"""
#답: print(a[0:4]

#문제6
"""
다음 문자열에서 "Python"만 출력해라.
a = "Life is too short, You need Python"
"""
#답: print(a[-6:])

#문제7
"""
다음 문자열을 두 개로 나누어 출력해라.
a = "20260307Sunny"
20260307
Sunny
"""

"""
답:
date = a[0:8] 
weather = a[8:] 
print(date) 
print(weather)
"""

#문제8
"""
다음 문자열을 PythOn → Python 으로 바꾸는 코드를 작성해라.
a = "PythOn"
"""
#답: print(a[:4]+'o'+a[5:])
#print(a.replace("O", "o"))

#문제9
"""
다음 문자열에서 "Life" 를 "Your leg" 로 바꿔라.
a = "Life is too short"
"""
#답: print(a.replace("Life", "Your leg"))

#문제10
"""
다음 문자열을 리스트로 나누어라.
a = "a:b:c:d"
['a', 'b', 'c', 'd']
"""
#답: print(a.split(":"))

#문제11⭐⭐⭐⭐⭐
"""
다음 변수들을 사용해서 아래 문장을 출력해라.
name = "Tom"
age = 25
My name is Tom and I am 25 years old.
"""
name = "Tom"
age = 25
print(f'My name is {name} and I am {age} years ord')
#print("My name is %s and I am %d years old." %(name, age))
#print(f"My name is {name} and I am {age} years old.")

#문제12⭐⭐⭐⭐⭐
"""
다음 문자열을 가운데 정렬로 출력해라.
****python****
"""
print(f'{"python":*^14}')
#답: print("{0:*^14}".format("python"))
#답: print(f'{"python":*^14}')

#문제13
"""
a = "Life is too short"
"""
#답: print(a.find("too"))

#문제14
"""
다음 문자열의 "b" 개수를 세어라.
a = "hobby"
"""
#답: print(a.count("b"))

#문제15
"""
다음 문자열을 처리해서 결과를 만들어라.
a = "  python  "
1️⃣ 양쪽 공백 제거
2️⃣ 대문자로 변환
"""
#답: print(a.strip().upper())

#문제
"""
log = "20260307:ERROR:Database connection failed" 파싱하기
출력:
date : 20260307
level : ERROR
message : Database connection failed
"""
log = "20260307:ERROR:Database connection failed"

a=log.split(":")
print(f"""date : {a[0]}
level : {a[1]}
message: {a[2]}""")