class Slope:
  def __init__(self,x,y,c):
    self.x=x
    self.y=y
    self.c=c

  def display(self):
    x1=self.x
    y1=self.y
    z1=self.c
    return (y-c)/x
  
y=float(input("enter y:"))
x=float(input("enter x:"))
c=float(input("enter c:"))
obj=Slope(x,y,c)
print("slope:",round(obj.display(),2))
