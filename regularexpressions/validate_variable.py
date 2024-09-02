# first character must be alphabet  k to m
# second letter must be a number that is / by 3
# follwed by any number of alphabets or numbers

from re import fullmatch

var_name="l3hy77"

pattern="[k-mK-M][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,var_name)

print("invalid" if matcher==None else "Valid" )