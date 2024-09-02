# wap to find the smallest num without using methids

# number = [3,2,5,7,1,9,10,4]
# smallest_num = number[0]

# for i in number:

#     if i < smallest_num:
#         smallest_num = i
# print(f" Smallest number is {smallest_num}")


# wap to find the second largest number in list

# number=[3,2,5,6,7,4]
# number.sort()
# print(number[-2])

number = [18,2,5,14,1,11,14,4]
largest_num = number[0]
second_largest = number[0]

for i in number:

    if i > second_largest and i > largest_num:

        second_largest = largest_num
       # print(second_largest)
        largest_num = i
       # print(largest_num)
    elif i > second_largest and i <largest_num:
        second_largest = i

print(f" Second largest num is {second_largest}")

# wap to find the sum of odd numbers
# wap to find the count of even and odd numbers in the list

