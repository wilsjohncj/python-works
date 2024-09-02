from re import finditer
text="ab12xyz678#$pqr123cdef"

# pattern="[a-z]{3}"  # prints consecutive pattern position alphabets only
# pattern="[a-z]{3}|[0-9]{3}"  # prints consecutive pattern position alphabets and numerics only

pattern="[c-ht-z]"  # print for c-h or t-z
pattern="([c-h]|[t-z])"  # print for c-h or t-z

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())