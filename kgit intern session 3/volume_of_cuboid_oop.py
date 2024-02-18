class Cuboid:
  def __init__(self,length,breadth,height):
    self.length=length
    self.breadth=breadth
    self.height=height

  def volume(self):
    x=self.length
    y=self.breadth
    z=self.height
    return x*y*z
  
l=float(input("enter length of cuboid:"))
b=float(input("enter breadth of cuboid:"))
h=float(input("enter height of cuboid:"))
cu=Cuboid(l,b,h)
print("volume of cuboid:",round(cu.volume(),2))
    