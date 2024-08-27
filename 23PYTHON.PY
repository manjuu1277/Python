#control statements
#conditionnal
 
 #if 
y=18
if y>=18:
    print("true")
if y<=18:
    print("wrong")
#elif
a=100
b=200
if b>a:
    print("b is greater than a")
elif  a!=b:
    print("a and b are not equal")
#else
x=23
if x>25:
    print("true")
else:
    print("wrong")


#iterative
#for
num={1,2,3,4,5}
for int in num:
    print(num)
#range
for num in range(0,23):
    print(num)
#while
num=100
while num>0:
    num=num-1
    print(num)

#transfer
#break
for i in range(10,20):
    if i == 6:
        break  
    print(i)
#continue
for i in range(10,20):
    if i <=15:
        continue 
    print(i)
#pass
for i in range(20,30):
    if i%2==0:
        pass
    print(i)
