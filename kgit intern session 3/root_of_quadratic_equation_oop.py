from math import *
class Quadratic:
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c

  def root1(self):
    x=self.a
    y=self.b
    z=self.c
    return (-y+sqrt((y*y)-(4*x*z)))/(2*x)
  def root2(self):
    x=self.a
    y=self.b
    z=self.c
    return (-y-sqrt((y*y)-(4*x*z)))/(2*x)
  
a1=float(input("enter a:"))
b2=float(input("enter b:"))
c3=float(input("enter c:"))
obj=Quadratic(a1,b2,c3)
print("root 1:",round(obj.root1(),2))
print("root 2:",round(obj.root2(),2))