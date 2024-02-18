count=int(input("enter count:"))

while(count!=0):

  len=float(input("enter length:"))
  bre=float(input("enter breadth:"))
  if(len>0 and bre>0):
    print("perimeter:",2*(len+bre))
    count=count-1
  else:
    print("invalid input")
    break
    

  

