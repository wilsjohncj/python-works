# validate pancard number
# first 3 characters are alphabets
# 4th place PCAFHT
# 5th palce alphabet
# 4 digit
# 1 alphabet

from re import fullmatch

pan_number=input("enter PAN number ")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"  # {3} maximum 3 - {1,3} MEANS MIN 1 AND MAX 3
# {4} IN BRACKET MEANS 4 DIGITS

matcher=fullmatch(pattern,pan_number)

print("invalid" if matcher==None else "valid")
