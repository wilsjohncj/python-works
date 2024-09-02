# program to check whether number is in fibonacci series
fib_number=int(input("Enter number"))
previous=0

current = 1
isfibo=False
next = previous + current
while(next<=fib_number):
    next = previous+current
    previous=current
    current=next
    if next==fib_number:
        isFibo=True
        break
print(isfibo)



