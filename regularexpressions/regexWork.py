from re import finditer

text="abcyhbhabckjuyhabckytrfabc"

match_abc=finditer("abc",text)
count=0
for m in match_abc:

    print(m.start(),"==",m.group())

    count=count+1

print("no. of abc",count)

