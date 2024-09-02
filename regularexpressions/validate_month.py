# validate months 01,02,09,10,12

# from re import fullmatch

# month_num=input("Enter month")

# pattern="(0?[1-9]|1[0-2])"

# matcher=fullmatch(pattern,month_num)

# print("Invalid" if matcher==None else "Valid")

# validate date

from re import fullmatch

date=input("Enter date")

pattern="(0[1-9|1[0-9|2[0-9|3[0-1])" # 0 or 1 or 2 or 3 use pipe - user square brackets for
#  2nd combination ie after 0 - 1 , upto 9 may come

matcher=fullmatch(pattern,date)

print("invaid" if matcher==None else "Valid")

# validate mobile number with country code mandatory
