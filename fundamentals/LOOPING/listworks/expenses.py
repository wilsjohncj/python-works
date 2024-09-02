expenses = [12000,13000,11000,14000,15000,21000,22000,13000]

# find count of objects in expenses
# print all expenses
# print expenses > 15000
# print total expense
expense_count = len(expenses)

# for i in range(0,expense_count):
#     print(expenses[i])

# for i in range(0,len(expenses)):

#     if expenses[i] >= 15000:
#         print(expenses[i])

# print total expense
# tot_exp=0
# for i in range(0,len(expenses)):
#     tot_exp=tot_exp+expenses[i]
# print(tot_exp)

# print average expenses
total_exp=0
aver_exp=total_exp/len(expenses)
for i in range(0,len(expenses)):
    total_exp=total_exp+expenses[i]
aver_exp=total_exp/len(expenses)
print(aver_exp)



    