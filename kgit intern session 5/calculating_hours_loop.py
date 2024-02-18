weeks=int(input("enter number of weeks:"))
l=[]
for x in range(weeks):
  lis=list(map(int,input("enter minutes:").split()));
  l.append(lis)
box=[]
for i in l:
  box.append(sum(i))
print("time in hours:",(sum(box))/60)

