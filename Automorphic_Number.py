a=int(input())
b=a*a
t=0
while a>0:
    if b%10!=a%10:
        print("Not an Automorphic Number")
        t=1
        break
    b=b//10
    a=a//10
if t==0:
    print("Automorphic Number")
    