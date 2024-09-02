num=int(input("Enter number"))
actual_num = num

total = 0

digit_count = len(str(num))

while(num!=0):

    digit = num % 10

    exponent = digit ** digit_count

    total= total+exponent

    num=num//10

print(total)
print("Armstrong" if actual_num==total else "not armstrong")