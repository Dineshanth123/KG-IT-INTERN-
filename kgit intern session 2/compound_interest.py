principalamt=float(input("enter principal amount:"))
interestrate=float(input("enter interest rate:"))
year=float(input("enter years:"))
compoundinterest=(principalamt*(1+interestrate/100)**year)-principalamt
print("compound interest:",round(compoundinterest,3))
