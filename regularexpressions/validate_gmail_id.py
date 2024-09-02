# validate gmail id


from re import fullmatch

gmailid=input("enter gmail id ")

# pattern="[a-zA-Z0-9._](@gmail.com)" alternate method
pattern="\\w[\\w\\._]*@gmail.com"   

# + match one or more
# ? optional
# * zero or more

matcher=fullmatch(pattern,gmailid)

print("invalid" if matcher==None else "valid")
