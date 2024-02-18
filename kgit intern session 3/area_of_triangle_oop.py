class Triangle:
  def __init__(self,base,height):
    self.base=base
    self.height=height

  def area(self):
    x=self.base
    y=self.height
    return 0.5*x*y
  
b=float(input("enter base of triangle:"))
h=float(input("enter height of triangle:"))

tr=Triangle(b,h)
print("area of triangle:",round(tr.area(),2))
    