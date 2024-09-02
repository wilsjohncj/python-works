# topic - dictonary  uses curly brackets
# list [] - use square bracket
# tuple=() use braces
# set=set()
# Dictionary{} user curly brackets with key value

# dict={key:value}
# student={"name":"sukumar","Course":"fullstack"}

# <class dict> : collecction of elements as akey:value pair
# print(student["name"])
# print(student.keys())

# student["name"]="hari" # will update/replace for key value "name"
# print(student)
# student["place"]="chennai" # overwite value or add new if key not present
# print(student)

student={"name":"sukumar","Course":"fullstack"}

# for i in student:
#     print(f"{i} = {student[i]}")

# update the cousre as fullstack in students in iteration


for i in student:
    if i == "Course":
        student[i]="fullstack1"
    print(student)


# delete a key "palce" if it is present in the dict using iteration

for i in student
#     if i=="place":
#         student.pop(i)
# print(student)