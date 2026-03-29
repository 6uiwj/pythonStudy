#01
from Tools.scripts.mkreal import join

korean = 80
english = 75
math = 55

print((korean+english+math)/3)

#02
print(13&2)

#03
pin = "881120-1068234"
yyymmdd = pin[0:6]
num = pin[7:]
print(yyymmdd)
print(num)

#04
print(pin[7])

#05
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#06
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#07
a = ['Life', 'is', 'too', 'short']
result = " ".join(a[:])
print(result)

#08
a = (1,2,3)
a = a + (4,)
print(a)

#09
# a = dict()
#a[[1]] = 'python' #키가 가변값이므로 불가능

#10
a =  {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11
a= [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b= list(aSet)
print(b)

#12
a = b = [1,2,3]
a[1]=4
print(b)