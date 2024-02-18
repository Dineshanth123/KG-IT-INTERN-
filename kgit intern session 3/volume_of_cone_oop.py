class Cone:
  def __init__(self,radius,height):
    self.radius=radius
    self.height=height

  def volume(self):
    x=self.radius
    y=self.height
    return (3.14*x*x*y)/3
  
r=float(input("enter radius of cone:"))
h=float(input("enter height of cone:"))
cu=Cone(r,h)
print("volume of cone:",round(cu.volume(),2))
    