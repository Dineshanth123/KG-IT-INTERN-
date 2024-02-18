class Sphere:
  def __init__(self,radius,):
    self.radius=radius

  def volume(self):
    x=self.radius
    return (4*3.14*x*x*x)/3
  
r=float(input("enter radius of sphere:"))
sp=Sphere(r)
print("volume of sphere:",round(sp.volume(),2))
    