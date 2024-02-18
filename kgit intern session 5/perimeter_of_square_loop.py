count=int(input("enter count:"))

for x in range(count):
  side=float(input("enter side:"))
  if(side>0):
    print("perimeter of square:",4*side)
  else:
    print("invalid input")
    break