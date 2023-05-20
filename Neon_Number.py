n=int(input())
s=n*n
q=s
sq=0
while(q>0):
    r=q%10
    sq=sq+r
    q=q//10
if(sq==n):
    print("Neon Number")
else:
    print("Not Neon Number")