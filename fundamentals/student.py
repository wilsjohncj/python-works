# write a  progrma to write student name and 3 marks and print total and average marks

student_name=input("Enter student name -")

english_mark=input("Enter marks for English - ")

maths_mark=input("Enter marks for maths -")

science_marks=input("Enter marks for Science - ")
total_Marks=int(english_mark)+int(maths_mark)+int(science_marks)
average_marks=total_Marks/3
print(f"Student Name {student_name} ")
print(f"Marks for English - {english_mark}")
print(f"marks for maths - {maths_mark}")
print(f"marks for science {science_marks}")
print(f"Total marks - {total_Marks}")
print(f" Average marks {average_marks}")

