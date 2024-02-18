class Circle:
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    x=self.radius
    return 3.14*x*x
  
r=float(input("enter radius of circle:"))
c=Circle(r)
print("area of circle:",round(c.area(),2))
    