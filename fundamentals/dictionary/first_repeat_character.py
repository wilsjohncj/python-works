text="ABTCDDBB"

word_count={} # A:11,B:1,C:1

for char in text: # char=A

    if char in word_count:

        print(char,"first recursivecharacter")
        break
    else:
        word_count[char]=1