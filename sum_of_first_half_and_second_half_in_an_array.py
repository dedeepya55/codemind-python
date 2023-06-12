n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in range(0,n//2):
    s=s+a[i]
for i in range(n//2,n):
    d=d+a[i]
print(s)
print(d)
    