from math import *
a=float(input("enter coefficient a:"))
b=float(input("enter coefficient b:"))
c=float(input("enter coefficient c:"))
res1=(-b+(sqrt((b**2)-(4*a*c))))/2*a
res2=(-b-(sqrt((b**2)-(4*a*c))))/2*a
print("root 1:",round(res1,2))
print("root 2:",round(res2,2))