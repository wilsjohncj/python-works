# WAP to find 2nd largest number

number=[0,3,5,7,-1,9,2,10,4]

# number.sort()

smallest_num=number[0]  # 3

second_smallest=number[-1]  # 10

for i in number:
    if i < second_smallest and i < smallest_num:
        second_smallest=smallest_num
        smallest_num=i
    elif i < second_smallest and i > smallest_num:
        second_smallest = i
print(f" Second smallest is {second_smallest}")


