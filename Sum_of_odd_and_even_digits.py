n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range (0,n):
    if i%2==0:
        c+=a[i]
    else:
        d+=a[i]
if c-d==0:
    print('YES')
else:
    print('NO')