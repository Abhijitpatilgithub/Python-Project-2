#using zip function
a=[1,2,3,4]
b=[5,6,7,8]
for c,d in zip(a,b):
    print(c,d)
    print("")
    a=[2,34,5,6]
    b=[67,88,9,1,0]
    for e,f in zip(a,b):
        print(e,f)

#without using zip function
a=[10,22,33,44]
a1=[11,22,55,88]
t=len(a)
for z in range(t):
    print(a[z],a1[z])
