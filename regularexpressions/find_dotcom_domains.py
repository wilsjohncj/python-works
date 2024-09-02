# read domain.txt and find domains with .com 

from re import fullmatch

f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\regularexpressions\\domain.txt","r")

# pattern=".*.com"    
pattern="[\w\W]+\\.com"
for line in f:

    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher !=None:

        print(domain)