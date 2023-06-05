n=int(input())
lst=list(map(int,input().split()))
for i in range (len(lst)):
    if lst[i]==0:
        print (lst[i],end=" ")
for i in range (len(lst)):
    if lst[i]!=0:
        print (lst[i],end=" ")