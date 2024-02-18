count=int(input("enter count:"))

while(count!=0):

  radius=float(input("enter radius:"))
  if(radius>0):
    print("area:",(3.14*radius*radius))
    count=count-1
  else:
    print("invalid input")
    break
    

  

