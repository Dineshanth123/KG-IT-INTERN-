count=int(input("enter count:"))

for x in range(count):
  side1=float(input("enter side1:"))
  side2=float(input("enter side2:"))
  side3=float(input("enter side3:"))
  if(side1>0 and side2>0 and side3>0):
    print("perimeter of triangle:",side1+side2+side3)
  else:
    print("invalid input")
    break