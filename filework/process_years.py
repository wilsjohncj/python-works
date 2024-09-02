f_read=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\years.txt","r")
f_century=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\century.txt","w")
f_non_century=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\non_century.txt","w")

for year in f_read:
    y = int(year.rstrip("\n"))

    if y % 100 == 0:

        f_century.write(str(y)+"\n")

    else:

        f_non_century.write(str(y)+"\n")
    
