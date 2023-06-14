n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if(i!=j and a[i]==a[j]):
            c=a[i]
print(c)