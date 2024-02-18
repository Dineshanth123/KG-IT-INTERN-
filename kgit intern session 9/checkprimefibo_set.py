number = int(input("Enter the number: "))
prime = {2,3,5,7,11,13,17,19,23,29}
fibo = {0,1,1,2,3,5,8,13,21,34}
if number in prime:
    print("It is Prime number ",number)
else:
    print("It is not Prime number")
    
if number in fibo:
    print("It is Fibonacci number ",number)
else:
    print("It is not Fibonacci number ")