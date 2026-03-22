#3
t=(1,)
print(type(t)) #tuple

#4
t = (1, 2, 3, 4, 5)
print(t[2:4])  #(3,4)

#5.
t = (10, 20, 30, 40, 50)
print(t[2:])

#6
t = (1,2,3)

#7.
t1 = (1,2)
t2 = (3,4)
print(t1+t2) # (1,2,3,4)

#8.
t = (1,2)
print(t*3) # (1,2,1,2,1,2)

#9
t= ()
t1 = (1,)
print(t)
print(t1)

#10
t = (1,2,3)
#t = t + (4)
print(t)
##불가능? tuple + int라

#11.
t = (1,2,3)
t = t + (4,)
print(t)

#12.
t = ('a', 'b', 'c')
print(t[1])

#13
t = ('a','b', ('ab', 'cd'))
print(t[2][1])

t = (1, 2, 3, 4, 5)
print(len(t))