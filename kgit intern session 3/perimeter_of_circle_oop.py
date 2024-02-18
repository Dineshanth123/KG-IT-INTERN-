class Circle:
  def __init__(self,radius):
    self.radius=radius

  def perimeter(self):
    x=self.radius
    return 2*3.14*x
  
r=float(input("enter radius of circle:"))
c=Circle(r)
print("perimeter of circle:",round(c.perimeter(),2))
    