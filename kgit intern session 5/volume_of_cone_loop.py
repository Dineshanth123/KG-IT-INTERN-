count=int(input("enter count:"))

for x in range(count):
  radius=float(input("enter radius:"))
  height=float(input("enter height:"))
  if(radius>0 and height>0):
    print("volume of cone:",(3,14*radius*radius*height)/3)
  else:
    print("invalid input")
    break