for i in range(6):
    x=int(input("Enter x value: "))
    y=int(input("Enter y value: "))
    z=int(input("Enter z value: "))
    if(x>y):
        if(x>z):
            print("X is Larger",x)
    elif(y>z):
        print("Y is Larger",y)
    else:
        print("Z is Larger",z)