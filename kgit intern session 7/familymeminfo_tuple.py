fam = []

dad = ('father','09/01/1971',"yellow")
mom = ('mother','10/04/1979','green')
bro = ('brother','22/04/2003','blue')
me = ('Dinesh Kanth','06/11/2004','white')
all = (dad,bro,me)
for i in all:
    fam.append(i)
print("-------------------------------")
print(tuple(fam))
print("-------------------------------")

