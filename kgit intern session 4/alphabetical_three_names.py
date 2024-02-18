n1=input("enter name 1:")
n2=input("enter name 2:")
n3=input("enter name 3:")
if((n1<n2) and (n1<n3) and (n3>n2) and (n3>n1)):
  print(n1)
  print(n2)
  print(n3)
elif((n2>n1) and (n2>n3) and (n3>n1) and (n3<n2)):
  print(n1)
  print(n3)
  print(n2)
elif((n2<n1) and (n2<n3) and (n1>n2) and (n1<n3)):
  print(n2)
  print(n1)
  print(n3)
elif((n2<n1) and (n2<n3) and (n3>n2) and (n3<n1)):
  print(n2)
  print(n3)
  print(n1)
elif((n3<n1) and (n3<n2) and (n2>n3) and (n2<n1)):
  print(n3)
  print(n2)
  print(n1)
else:
  print(n3)
  print(n1)
  print(n2)
