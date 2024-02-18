count=int(input("enter count:"))

for x in range(count):
  radius=float(input("enter radius:"))
  if(radius>0):
    print("perimeter of circle:",2*3.14*radius)
  else:
    print("invalid input")
    break