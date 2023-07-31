# arthmatc operator
a=10
b=20
print(a+b)
a=10
b=20
print(a//b)
a=10
b=20
print(a%b)
a=10
print(a**3)
#assignment operator
a=10
print(a)
a=10
a=a+5
a+=5
print(a)
a=10
a=a-5
a-=5
print(a)
#comparision operator
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
#logical operator
a=10
b=20
print(a==10 and b>=a)
a=10
b=20
print(a==10 or b<a)
print(not a!=10)
#membership operator
a="hello"
print('o'in a)
b=[10,20,30,40,]
print(70 not in b)
#identity operators
a=10
b=20
print(a is b,a==b)
print(a is not b,a<b)
print(a is not b,b>a)
#bitwise operator
a=10
b=8
print(bin(a))
print(bin(b))
print(a&b,bin(a&b))
print(bin(a&b),a&b)
print(a|b,bin(a|b))
print(a^b,bin(a^b))
print(bin(a^b),a^b)
