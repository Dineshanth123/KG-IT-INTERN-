name1 = input("Enter first Name: ").upper()
name2 = input("Enter second Name: ").upper()
while (name1 != "STOP"):
    print("<<<Alphabetical Order>>>")
    if(name1<name2):
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)
    name1 = input("Enter first Name: ").upper()
    name2 = input("Enter second Name: ").upper()