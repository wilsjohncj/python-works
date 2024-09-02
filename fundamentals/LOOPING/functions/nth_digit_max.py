# write a function for nth_digit_max with two paramters num1,num2
# nth_digit_max(123,480) =>123
# nth_digit_max(546,127) =>127

num1=int(input("Input num1"))
num2=int(input("Input num2"))

def nth_digit_max(num1,num2):

    num1_last_digit=num1%10

    num2_last_digit=num2%10

    if num1_last_digit > num2_last_digit:

        return num1

    else:

        return num2

print(nth_digit_max)