# read a number from user 
# print fizz if num is / by 3
# print buzz if num is / by 5
# print fizzbuzz if num is / by 15

num = int(input("Enter number"))

if num % 15 == 0:  #  modulus operator is percent symbol
    print("fizz buzz")
elif num%5 == 0:
    print("buzz")
elif num%3 ==0:
    print("fizz")
else:
    print("invalid")

