f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\filework\\students.txt","r")

students=[]

for stud in f:
    students.append(stud.rstrip("\n"))

print(students)