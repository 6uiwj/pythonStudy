#파일 생성하기
#f = open("새파일.txt",'w')
#f.close()
"""
파일_객체 = open(파일_이름, 파일_열기_모드)

파일 열기 모드 ㅣ          설명
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    r        ㅣ 읽기 모드: 파일을 읽기만 할 때 사용한다.
    w        ㅣ 쓰기 모드: 파일에 내용을 쓸 때 사용한다.
    a        ㅣ 추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용한다.
"""

#f = open("C:/doit/새파일.txt",'w')
#f.close()


#파일을 쓰기 모드로 열어 내용 쓰기
# f = open("새파일1.txt",'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

#파일을 읽는 여러가지 방법
##readline 함수 이용하기
# f = open("새파일1.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
#
# f = open("새파일1.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

##readlines 함수 사용하기 / readlines: 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트
# f = open("새파일1.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() #줄바꿈 문자 제거
#     print(line)
# f.close()

##read함수 사용하기 - 파일의 내용 전체를 문자열로 리턴
f = open("새파일1.txt", 'r')
data = f.read()
print(data)
f.close()

##파일 객체를 for문과 함께 사용하기
f = open("새파일1.txt", 'r')
for line in f:
    print(line)
f.close()

#파일에 새로운 내용 추가하기
f = open("새파일1.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with문과 함께 사용하기 - f.close() 자동적용
"""
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
"""
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")