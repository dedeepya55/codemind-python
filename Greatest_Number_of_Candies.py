n=int(input())
lst=list(map(int,input().split()))
a=int(input())
for i in lst:
    if i+a>=max(lst):
        print("True",end=" ")
    else:
        print("False",end=" ")