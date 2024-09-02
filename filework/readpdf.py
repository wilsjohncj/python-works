f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\news.txt","r")

word_lst = []

for line in f:

words=line.strip("\n").split(" ")

for w in words:

#         word_lst.append(w)

# print(word_lst)