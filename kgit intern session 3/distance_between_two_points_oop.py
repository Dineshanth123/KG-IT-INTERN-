from math import *
class Distance:
  def __init__(self,x1,y1,x2,y2):
    self.x1=x1
    self.y1=y1
    self.x2=x2
    self.y2=y2

  def display(self):
    a=self.x1
    b=self.y1
    c=self.x2
    d=self.y2
    return sqrt(((c-a)**2)-((d-b)**2))
  
x1=float(input("enter x1:"))
y1=float(input("enter y1:"))
x2=float(input("enter x2:"))
y2=float(input("enter y2:"))
obj=Distance(x1,y1,x2,y2)
print("distance:",round(obj.display(),2))
