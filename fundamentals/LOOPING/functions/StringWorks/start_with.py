# program to check starts with

text="hello world"
print(text.startswith("h"))
print(text.endswith("ld"))
text="/nhello world/n"
print(text.strip("/n"))
word="hellopython"
# 012345678910  index
sliced_str=word[0:5]  # 0 is start and 5 is end
print(sliced_str)
sliced_str_last=word[5:11]
print(sliced_str_last)
sliced_str_last1=word[5:] # this prints from 5 to end ie 2nd parameter not given
print(sliced_str_last1)
sliced_str_2=word[10:4:-1]
print(sliced_str_2)
sliced_str_3=word[::-1]
print(sliced_str_3)
sliced_str_4=word[:5]
print(sliced_str_4)
