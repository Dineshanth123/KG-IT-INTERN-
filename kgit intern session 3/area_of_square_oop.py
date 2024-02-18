class Square:
  def __init__(self,side):
    self.side=side

  def area(self):
    x=self.side
    return x*x
  
n =float(input("enter side of square:"))
sq=Square(n)
print("area of square:",round(sq.area(),2))
    