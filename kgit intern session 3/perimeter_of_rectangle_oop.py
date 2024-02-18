class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth

  def perimeter(self):
    x=self.length
    y=self.breadth
    perm=(2*x)+(2*y)
    return perm
  
l=float(input("enter length of rectangle:"))
b=float(input("enter breadth of rectangle:"))
rc=Rectangle(l,b)
print("perimeter of square:",round(rc.perimeter(),2))
    