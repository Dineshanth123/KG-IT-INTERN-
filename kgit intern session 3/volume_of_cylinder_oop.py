class Cylinder:
  def __init__(self,radius,height):
    self.radius=radius
    self.height=height

  def volume(self):
    x=self.radius
    y=self.height
    return 3.14*x*x*y
  
r=float(input("enter radius of cylinder:"))
h=float(input("enter height of cylinder:"))
cy=Cylinder(r,h)
print("volume of cylinder:",round(cy.volume(),2))
  