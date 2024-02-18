name1=input("Enter first name: ")
name2=input("Enter second name: ")
name3=input("Enter third name: ")
name4=input("Enter fourth name: ")
if(name1<name2 and name1<name3 and name1<name4):
    print(name1)
    if(name2<name3 and name2<name4):
        print(name2)
        if(name3<name4):
            print(name3)
            print(name4)
        else:
            print(name4)
            print(name3)
    elif(name3<name4 and name3<name2):
        print(name3)
        if(name2<name4):
            print(name2)
            print(name4)
        else:
            print(name4)
            print(name2)
    elif(name4<name2 and name4<name3):
        print(name4)
        if(name2<name3):
            print(name2)
            print(name3)
        else:
            print(name3)
            print(name2)
elif(name2<name1 and name2<name3 and name2<name4):
    print(name2)
    if(name1<name3 and name1<name4):
        print(name1)
        if(name3<name4):
            print(name3)
            print(name4)
        else:
            print(name4)
            print(name3)
    elif(name3<name1 and name3<name4):
        print(name3)
        if(name1<name4):
            print(name1)
            print(name4)
        else:
            print(name4)
            print(name1)
    elif(name4<name1 and name4<name3):
        print(name4)
        if(name3<name1):
            print(name3)
            print(name1)
        else:
            print(name1)
            print(name3)
elif(name3<name1 and name3<name2 and name3<name4):
    print(name3)
    if(name1<name2 and name1<name4):
        print(name1)
        if(name2<name4):
            print(name2)
            print(name4)
        else:
            print(name4)
            print(name2)
    elif(name2<name1 and name2<name4):
        print(name2)
        if(name1<name4):
            print(name1)
            print(name4)
        else:
            print(name4)
            print(name1)
    elif(name4<name1 and name4<name2):
        print(name4)
        if(name1<name2):
            print(name1)
            print(name2)
        else:
            print(name2)
            print(name1)
elif(name4<name1 and name4<name2 and name4<name3):
    print(name4)
    if(name1<name2 and name1<name3):
        print(name1)
        if(name2<name3):
            print(name2)
            print(name3)
        else:
            print(name3)
            print(name2)
    elif(name2<name3 and name2<name1):
        print(name2)
        if(name1<name3):
            print(name1)
            print(name3)
        else:
            print(name3)
            print(name1)
    elif(name3<name1 and name3<name2):
        print(name3)
        if(name1<name2):
            print(name1)
            print(name2)
        else:
            print(name2)
            print(name1)