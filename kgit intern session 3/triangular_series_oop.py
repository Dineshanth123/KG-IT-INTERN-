class Triangularseries:
  def __init__(self,count):
    self.count1=count

  def display(self):
    count=self.count1
    y=0
    for x in range(1,count+1):
      res=x+y
      print(res)
      y=res

    

count=int(input("enter count:"))
obj=Triangularseries(count)
obj.display()

    











