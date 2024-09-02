# program to check leap year

year=int(input("Enter year"))

if (year%100==0 and year%400==0) or (year%100 !=0 and year%4 ==0):

    print(f" {year} is leap year")

else:

    print(f"Not a leap year")

