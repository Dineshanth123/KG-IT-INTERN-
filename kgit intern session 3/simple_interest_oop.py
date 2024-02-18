class simpleinterest:
  def __init__(self,principalamt,rate,time):
    self.principalamt=principalamt
    self.rate=rate
    self.time=time

  def display(self):
    x=self.principalamt
    y=self.rate
    z=self.time
    return (x*y*z)/100
  
princ=float(input("enter principal amount:"))
ra=float(input("enter interest rate:"))
yr=float(input("enter years:"))
ob=simpleinterest(princ,ra,yr)
print("simpleinterest:",round(ob.display(),2))
