# /Simple Calculator

# to take value from user num1 & num2 
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

# choose any one for calculate
choose=int(input("Press 1 for addition: \nPress 2 for substraction: \nPress 3 for multiplication: \nPress 4 for divison: "))

if choose==1:
    print(f"The addition of {num1} and {num2} is= {num1+num2}")
elif choose==2:
    print(f"The substraction of {num1} and {num2} is= {num1-num2}")   
elif choose==3:
    print(f"The multiplication of {num1} and {num2} is= {num1*num2}") 
elif choose==4:
    print(f"The divison of {num1} and {num2} is= {num1/num2}")  
else:
    print("Number is not found!")   
