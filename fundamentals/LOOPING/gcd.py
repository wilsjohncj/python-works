# GCD of (12,24) # 1,2,3,46,12,(12)

number1 = int(input("enter number 1"))
number2 = int(input("enter number 2"))

gcd = 1

for i in range(1,number1+1): 

    if number1%i==0 and number2%i==0:
        gcd=1
print(gcd)
