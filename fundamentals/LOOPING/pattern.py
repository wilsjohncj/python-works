# print below pattern
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# nested loop - inner loop will work first and complte

# for row in range(1,4): # row = 1 first value

#     for col in range(1,5): # col = 1 first value

#         print(row,end=" ")

#     print()

# print below pattern
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

for row in range(1,5):

    for col in range(1,7):

        print("*",end=" ")

    print()
       