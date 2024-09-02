from re import finditer
text="abc 7Klefg@#"

# pattern="\d" # like [0-9]
#pattern="\D" # [^0-9]

#pattern="\w" # [a-zA-Z0-9]
#pattern="\W" # [a-zA-Z0-9] excludes all alphabets and numerics
#pattern="\s" # [a-zA-Z0-9] includes space
pattern="\S" # [a-zA-Z0-9] excludes space

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())