# simple calculater
a=int(input("enter value1:-"))
b=int(input("enter value2:-"))
opr=input("enter opr")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a - b)
elif opr == "*":
    print(a * b)
elif opr == "%":
    print(a %b)
else:
    print("invalid opr")

