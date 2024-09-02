# write a function to check for leap year
year=int(input("Enter Year)"))
def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return(True) 

    else:

        return(False)

print(is_leap_year(year))