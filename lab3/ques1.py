import math
x1=float(input("enter x1,:"))
y1=float(input("enter y1,:"))
r=float(input("enter radius"))
x2=float(input("enter x2"))
y2=float(input("enter y2"))
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
if d<r:
    print("Inside the boundary")
elif d==r:
    print("On the boundary")
else:
    print("Outside the Boundary")

