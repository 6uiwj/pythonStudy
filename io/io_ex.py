#01 홀수,짝수 판별
def is_odd(number):
    if number % 2 == 1 :
        return True
    else :
        return False

#02 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#03 프로그램의 오류 수정하기 1
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다" % total)