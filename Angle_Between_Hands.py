import math
x=input()
x=x.split(":")
hh=int(x[0])
mm=int(x[1])
a=abs((30*hh)-(5.5*mm))
b=360-a
if a<b:
    print(f"{a:.1f}")
else:
    print(f"{b:.1f}")