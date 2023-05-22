import math
a=int(input())
rot=math.sqrt(a)
if int(rot+0.5)**2==a:
    print("True")
else:
    print("False")