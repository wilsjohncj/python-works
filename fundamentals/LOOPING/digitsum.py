# read a number and print sum of number

num = int(input("enter number"))
total =0 
while(num!=0):
    digit = num%10
    total=total+digit
    num=num//10
print(total)
