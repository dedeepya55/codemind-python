num=int(input())
temp=num
rev=0
s=0
i=1
while num:
    rev=rev*10+num%10
    num=num//10
while rev:
    s=s+(rev%10)**i
    rev=rev//10
    i=i+1
if s==temp:
    print("True")
else:
    print("False")
    