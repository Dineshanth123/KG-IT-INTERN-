class Squares:
  def __init__(self,count):
    self.count1=count

  def display(self):
    count=self.count1
    for z in range(1,count+1):
      print(z*z)
    

count=int(input("enter count:"))
obj=Squares(count)
obj.display()

    











