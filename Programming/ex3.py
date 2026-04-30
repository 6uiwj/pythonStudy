"""
게시물의 총 개수와 한페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램
"""

def get_total_page(n,s):
    p = n//s
    x = n%s
    if(x > 0):
        p += 1
    return p

print(get_total_page(10,9))