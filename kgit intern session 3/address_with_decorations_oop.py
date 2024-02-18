class Address:
  def __init__(self,name):
    self.name=name

  def dec(self):
    print("---------------------------------")
  
  def display(self):
    print(self.name)

obj=Address("Somanur,Coimbatore-641 668")
obj.dec()
obj.display()
obj.dec()
    
