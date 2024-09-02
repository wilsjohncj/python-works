# program to calculate BMI

weight_in_kgs = int(input("Weight in Kgs "))

height_in_cms = int(input("Height in CMS "))

height_in_mts = height_in_cms/100

bmi = round(weight_in_kgs/height_in_mts**2)

print(f"BMI IS {bmi}")

# print weight category - <19 uder weight , 19 to 25 normal weight , 25 to 30 overwieght , >30 obese

if bmi <=19:

    print("Under wieght")

elif bmi<=25:

     print(" normal weight")

elif bmi<=30:
    
    print("Over weight")

else:
    print("Obese")



