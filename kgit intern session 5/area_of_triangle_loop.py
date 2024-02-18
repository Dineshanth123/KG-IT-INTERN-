count=int(input("enter count:"))

while(count!=0):

  base=float(input("enter base:"))
  height=float(input("enter height:"))
  if(base>0 and height>0):
    print("area:",0.5*base*height)
    count=count-1
  else:
    print("invalid input")
    break
    

  

