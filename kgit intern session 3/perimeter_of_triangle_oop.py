class Triangle:
  def __init__(self,s1,s2,s3):
    self.side1=s1
    self.side2=s2
    self.side3=s3

  def perimeter(self):
    x=self.side1
    y=self.side2
    z=self.side3
    return x+y+z
  
s1=float(input("enter side1 of triangle:"))
s2=float(input("enter side2 of triangle:"))
s3=float(input("enter side3 of triangle:"))

tr=Triangle(s1,s2,s3)
print("perimeter of triangle:",round(tr.perimeter(),2))
    