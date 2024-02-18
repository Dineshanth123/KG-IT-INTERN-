from math import *

count=int(input("enter count:"))

while(count!=0):

  a=float(input("enter coefficient a:"))
  b=float(input("enter coefficient b:"))
  c=float(input("enter coefficient c:"))
  print("root1:",(-b+(sqrt((b**2)-(4*a*c))))/2*a)
  print("root2:",(-b-(sqrt((b**2)-(4*a*c))))/2*a)
  count=count-1




  