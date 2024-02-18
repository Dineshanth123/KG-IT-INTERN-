class Compoundinterest:
  def __init__(self,principalamt,rate,time):
    self.principalamt=principalamt
    self.rate=rate
    self.time=time

  def display(self):
    x=self.principalamt
    y=self.rate
    z=self.time
    return (x*(1+y/100)**z)-x
  
princ=float(input("enter principal amount:"))
ra=float(input("enter interest rate:"))
yr=float(input("enter years:"))
ob=Compoundinterest(princ,ra,yr)
print("compound interest:",round(ob.display(),2))
