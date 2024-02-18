amount=float(input("enter amount:"))
rate=float(input("enter rate of interest:"))
years=float(input("enter years:"))
while(True):
  if(amount>0 and rate>0 and years>0):
    print("simple interset:",(amount*rate*years)/100)
    break
  else:
    print("invalid input")
    break


  