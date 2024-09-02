# read a year from user and print century year if year end with two zeros
# else print non century year

year=int(input("Enter year"))

if (year%100)==0:
    print(f"Year is century")
else:
    print('non century year')