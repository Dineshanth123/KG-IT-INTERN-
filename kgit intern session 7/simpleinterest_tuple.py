final=[]
principle_amt = (1000,1500,2500,2000,1200,1700,2300,3000)
principle_list = list(principle_amt)
rate = (int(input("Enter the rate of interest: ")))/100
year = int(input("Enter the number of years: "))
for i in principle_list:
    x = i*rate*year
    final.append(x)
    
print("Interest amount:")
for x in final:
    print(f"{x:.2f}")