distance=float(input("enter distance in kms:"))
speed=float(input("enter speed kms/hr:"))
while(True):
  if(distance>0 and speed>0):
    print("time taken in minutes:",(distance/speed)*60)
    break
  else:
    print("invalid input")
    break


  