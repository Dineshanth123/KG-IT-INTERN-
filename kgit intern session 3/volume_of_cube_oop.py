class Cube:
  def __init__(self,side):
    self.side=side

  def volume(self):
    x=self.side
    return x*x*x
  
n =float(input("enter side of cube:"))
cu=Cube(n)
print("volume of cube:",round(cu.volume(),2))
    