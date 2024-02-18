amount=float(input("enter amount:"))
rate=float(input("enter rate of interest:"))
years=float(input("enter years:"))
while(True):
  if(amount>0 and rate>0 and years>0):
    print("compound interset:",(amount*(1+rate/100)**years)-amount)
    break
  else:
    print("invalid input")
    break


  