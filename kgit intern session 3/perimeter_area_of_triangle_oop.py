class Triangle:
  def __init__(self,base,height,s1,s2,s3):
    self.base=base
    self.height=height
    self.s1=s1
    self.s2=s2
    self.s3=s3

  def area(self):
    x=self.base
    y=self.height
    return 0.5*x*y
  
  def perimeter(self):
    x=self.s1
    y=self.s2
    z=self.s3
    return x+y+z
  
b=float(input("enter base of triangle:"))
h=float(input("enter height of triangle:"))

s1=float(input("enter side1 of triangle:"))
s2=float(input("enter side2 of triangle:"))
s3=float(input("enter side3 of triangle:"))

tr=Triangle(b,h,s1,s2,s3)
print("area of triangle:",round(tr.area(),2))
print("perimeter of triangle:",round(tr.perimeter(),2))
    
    