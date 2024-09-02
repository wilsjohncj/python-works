# program to check palindrome or not

num=int(input("enter number"))
actual_num=num

# 3 2 1 use while loop to extract
result=0
while(num !=0):   # use while lopp when we dont know end of execution

    digit=num%10 # % is modulus
    result=result*10+digit  # result = 0*10+33
    num = num //10  # // floor division
print(result)
print("Palidrome" if result==actual_num else "not palindrome")
