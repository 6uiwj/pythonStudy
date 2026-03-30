
money = True
if money:
    print("택시를 타고 가라") #수행문의 들여쓰기 깊이가 항상 같아야함
else:
    print("걸어가라")


money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#and or not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


#in, not in
print(1 in [1,2,3]) #True
print(1 not in [1,2,3]) #False

print('a' in ('a', 'b', 'c')) #True
print('j' not in 'python') #True

#만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")

#조건 문에서 아무런 일도 하지 않도록  설정하고 싶을때
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#elif
##주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
poke = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#if문 한 줄로 작성하기
poke = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else:print("카드를 꺼내라")

#조건부 표현식
score = 50
if score >= 60:
    message = "success"
else: message = "failure"

message = "success" if score >= 60 else "failure"
#변수 = 조건문이+참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값