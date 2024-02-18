class Square:
  def __init__(self,side):
    self.side=side

  def perimeter(self):
    x=self.side
    return 4*x
  
n =float(input("enter side of square:"))
sq=Square(n)
print("perimeter of square:",round(sq.perimeter(),2))
    