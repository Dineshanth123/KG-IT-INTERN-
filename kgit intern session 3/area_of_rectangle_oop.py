class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth

  def area(self):
    x=self.length
    y=self.breadth
    return x*y
  
l=float(input("enter length of rectangle:"))
b=float(input("enter breadth of rectangle:"))
rc=Rectangle(l,b)
print("area of rectangle:",round(rc.area(),2))
    