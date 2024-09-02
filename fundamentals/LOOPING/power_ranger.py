# progam to print power ranger
# eg. 2 -> [2+22]
# eg. 3 -> [3+33+333]
# eg. 4 -> [4+44+444+4444]

power_num=int(input("Enter number"))

pattern=0
total=0

for i in range(1,power_num+1):
    pattern=pattern*10+power_num
    total=total+pattern
    print(pattern)
print(total)


