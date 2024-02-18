n1=float(input("enter number 1:"))
n2=float(input("enter number 2:"))
n3=float(input("enter number 3:"))
n4=float(input("enter number 4:"))
n5=float(input("enter number 5:"))
if((n1>n2) and (n1>n3) and (n1>n4) and (n1>n5)):
  print("n1 is greater")
elif((n2>n1) and (n2>n3) and (n2>n4) and (n2>n5)):
  print("n2 is greater")
elif((n3>n1) and (n3>n2) and (n3>n4) and (n3>n5)):
  print("n3 is greater")
elif((n4>n1) and (n4>n2) and (n4>n3) and (n4>n5)):
  print("n4 is greater")
else:
  print("n5 is greater")
