count=int(input("enter count:"))

for x in range(count):
  length=float(input("enter length:"))
  breadth=float(input("enter breadth:"))
  height=float(input("enter height:"))
  if(length>0 and breadth>0 and height>0):
    print("volume of cuboid:",length*breadth*height)
  else:
    print("invalid input")
    break