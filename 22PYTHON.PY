#operators
#arithmetic
#+,-,%,*,/,//,**
print("arithmetic")
print(5+3)
print(5-3)
print(5%3)
print(5/3)
print(5//3)
print(5**3) 

#logical
# and or not
x=5
y=3
print("logical")
print(x==5 and y==3)
print(x==5 or y==3)
a=not x==5
b=not y==3
print(a)
print(b)

#relational
# < > == <= >= !=
x=5
y=3

print("relational")
print(x>y)
print(x<y)
print(x==y)
print(x<=y)
print(x==y)
print(x!=y)


#bitwise
# & | ^ ~ << >>

x=5
y=3
print("bitwise")
print(a&b)
print(x<<5)
print(x|y)
print(x^y)
print(y>>x)


#assignment
# = += -= *= /= %= ** //
x=5
x+=3
print(x)
x-=9
print(x)
x*=3
print(x)
x/=2
print(x)
x%=5
print(x)
x**10
print(x)
x//15
print(x)


#identity
a=[1,2,3,4]
b=[1,2,3,4]
c=a
print(a is b)
print(a is c)
print(a is not b)