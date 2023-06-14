n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(len(a)):
    c=0
    for j in range(len(b)):
        if(i==j):
            c=a[i]+b[j]
    print(c,end=' ')