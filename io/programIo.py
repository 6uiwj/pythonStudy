#sys 모듈 사용하기
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')