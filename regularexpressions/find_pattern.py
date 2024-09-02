from re import findall

text="the fat cat run verry fast to catch rat"

pattern=".at"  # dot means any words ending with "at"

matcher=findall(pattern,text)

print(matcher)