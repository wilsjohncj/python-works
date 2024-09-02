# Program to find largest of 2 numbers

num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))

if num1 > num2:
    print(f" Num1 {num1} is largest")
elif num2 > num1:
    print(f" Num2 {num2} is largest")
elif num1 == num2:
    print(f" Num1 and Num2 are equal")

