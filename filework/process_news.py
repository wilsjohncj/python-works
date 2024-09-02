f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\news.txt","r")

# word_lst = []

# for line in f:

#     words=line.strip("\n").split(" ")

#     for w in words:

#         word_lst.append(w)

# print(word_lst)

word_list=[w for line in f for w in line.rstrip("\n").split(" ") if w!=""]

wc={w:word_list.count(w) for w in word_list}

# print(wc)

def  get_value(key):

    return wc.get(key)

srt=sorted(wc,key=get_value,reverse=True)
print(wc)
# print(srt)

