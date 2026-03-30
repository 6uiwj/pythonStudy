a=True
b= False
print(type(a))
print(1==1)
print(2>1)
print(2<1)

#자료형의 참과 거짓
a = [1,2,3,4]
while a: #a가 참일동안
    print(a.pop()) #리스트의 마지막 요소 하나씩 꺼내기

if []:
    print("참")
else:
    print("거짓")


if [1,2,3]:
    print("참")
else:
    print("거짓")

#불 연산
print(bool('python')) #True
print(bool('')) #False

print(bool([1,2,3])) #True
print(bool([])) #False
print(bool(0)) #False
print(bool(3)) #True
