f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\land_slide.txt","r")

for line in f:

    lst=line.rstrip("\n").split(" ") # ["Kerala","2018",14]
