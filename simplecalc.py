# function to add two numbers
def add(x,y):
    return x + y

#function to subtract two numbers
def subtract(x,y):
    return x - y 

#function to multiply two numbers 
def multiply(x,y):
    return x * y

#function to divide two numbers
def divide(x,y):
    if y == 0:
        return "cannot divide by zero"
    return x/y

print("select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

# take input from user 
choice = input("enter choice(1/2/3/4/5):")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

if choice == '1':
    print(num1 ,"+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print("exiting calculator...")
    SystemExit
else:
    print("invalid input")
