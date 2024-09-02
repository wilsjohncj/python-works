from re import finditer

text="abc123 @6dfdf 876d6ffZ"

# pattern="[abf]"  # checks for a or b or f

# pattern="[a-k]" # checks for a to k

# pattern="[a-z]" # checks for all lowercase alphabets 

# pattern="[A-Z]" # checks for all upper case alphabets

# pattern="[A-Za-z]" # checks for all upper and lower case alphabets

# pattern="[A-Za-z]" # checks for all upper and lower case alphabets

# pattern="[0-9]" # checks for digits

# pattern="[a-zA-Z0-9]" # checks for all alpha numeric

# pattern="[^a-zA-Z]" # check for non alphabets ie exclude alphabets use caret symbol

# pattern="[^0-9]" # exclude all numbers - use caret symbol

# pattern="[\s]"  # checks for space character 

pattern="[^a-zA-Z0-9\s]"  # find only special characters , exclude characters, numbers and spaces

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())