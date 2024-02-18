class Fibonacci:
  def __init__(self,x1,y1,count):
    self.x1=x1
    self.y1=y1
    self.count1=count

  def display(self):
    x=self.x1
    y=self.y1
    count=self.count1
    print(x)
    print(y)
    for z in range(2,count):
      res=x+y
      print(res)
      x=y
      y=res
    
count=int(input("enter count:"))
obj=Fibonacci(0,1,count)
obj.display()

    











