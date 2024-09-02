# program to print largest among 3 numbers

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))

if num1 > num2 and num1 > num3:
    largest_num = num1
elif num2 > num1 and num2 > num3:
    largest_num = num2
else:
    largest_num = num3
print(f" {largest_num} is the largest")