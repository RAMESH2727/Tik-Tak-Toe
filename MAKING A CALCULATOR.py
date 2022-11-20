#making a calculator
print("making a calculator")
#this function is used for the addition of two numbers 
def addition(x,y): 
    return x+y
#this function is used for the subtraction of two numbers
def subtract(x,y):
    return x-y
#this function is used for the multiplication of two numbers
def multiply(x,y):
    return x*y
#this function is used for the division of two numbers
def divide(x,y):
    return x/y

print("\nselect operator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
#input given by the user
choice=input("enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("result")
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
