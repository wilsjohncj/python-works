# program to check prime number

num =int(input("enter number"))
isPrime= True

for i in range(2,num):

    if num %i==0: # 16%2 ==0

        isPrime = False

        break
print(f"{num} is prime " if isPrime==True else f"{num} not prime")