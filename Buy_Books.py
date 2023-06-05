n=int(input())
lst=list(map(int,input().split()))
lst2=list(map(int,input().split()))
d=sum(lst)
f=sum(lst2)
if d>f:
    print(0)
else:
    print(f-d)