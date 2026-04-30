#time
import time
##time.time() : UTC 사용 현재 시간 실수 형태로 리턴
print(time.time())

##time.localtime - 연,월,일,시,분,초 형태로 바꾸는 함수
print(time.localtime(time.time()))

##time.asctime - time.localtime가 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴
print(time.asctime(time.localtime(time.time()))) #ex) Wed Apr 20 16:42:59 2026

##time.ctime = time.asctime(time.localtime(time.time()) - 항상 현재시간 리턴
print(time.ctime())

##time.strftime('출력할_형식_포맷_코드', time.localtime(time.time()))
print(time.strftime( '%x', time.localtime(time.time()))) #04/29/26
print(time.strftime( '%c', time.localtime(time.time()))) #Thu May 25 10:13:52 2023

##time.sleep
for i in range(10):
    print(i)
    time.sleep(1)


