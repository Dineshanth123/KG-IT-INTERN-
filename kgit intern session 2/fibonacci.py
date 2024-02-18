count=int(input("enter count:"))
x=0
y=1
print(x)
print(y)
for z in range(2,count):
  res=x+y
  print(res)
  x=y
  y=res
  