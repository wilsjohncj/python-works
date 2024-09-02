# 1st character upper case
# next character IS A digit 1-9
# next digit 0-9
# 4th 0 or 1 white space character
# next 4 characters any number from 0-9
# last character from 1-9

# eg S71 1993

# validate gmail id

from re import fullmatch

passport_num=input("enter passport num ")

pattern="[A-Z][1-9][0-9][0\\s]\\d{4}[1-9]"   

matcher=fullmatch(pattern,passport_num)

print("invalid" if matcher==None else "valid")
