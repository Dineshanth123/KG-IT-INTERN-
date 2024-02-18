count=int(input("enter count:"))

for x in range(count):
  side=float(input("enter side:"))
  if(side>0):
    print("volume of cube:",side*side*side)
  else:
    print("invalid input")
    break