count=int(input("enter count:"))

for x in range(count):
  radius=float(input("enter radius:"))
  if(radius>0):
    print("volume of sphere:",(4*3.14*radius*radius*radius)/3)
  else:
    print("invalid input")
    break