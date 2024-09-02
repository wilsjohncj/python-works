lasy_digit_max= lambda n1,n2: n1 if n1%10 > n2%10 else n2
print(lasy_digit_max(127,872))

# odd_even(n) odd else even

odd_even = lambda n:"Even" if n%2==0 else "odd"

print(odd_even(12))
