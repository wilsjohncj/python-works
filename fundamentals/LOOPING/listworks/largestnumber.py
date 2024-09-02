# number = [1,3,2,5,7,9,10,4]
# number.sort()
# print(number[-1])

# wap to find the largest num without using methids

number = [1,3,2,5,7,9,20,4]

largest_num=number[0]

for i in number:

    if i > largest_num:
        largest_num = i
print(f" Largest number is {largest_num}")

