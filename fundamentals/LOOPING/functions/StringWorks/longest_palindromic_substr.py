# longest palindrome substring from giv=en string

# text1 = "ababba"
text = "RACECAR"
# below are palindromes
# a , # b # aba # bb # bab # abba # R # A # C # E # CEC # ACECA

for i in range(0,len(text)):
    left = i

    right = i

    # while(text[left]==text[right] and left >=0 and right<len(text)):
    while( left >=0 and right<len(text) and text[left]==text[right]):

        current_palindrome=text[left:right+1]
        print(current_palindrome)
        left = left -1
        right=right+1

