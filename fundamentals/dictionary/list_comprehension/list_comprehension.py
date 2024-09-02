# list comprehension

lst=[10,2,3,4,5,6]

squares = [n**2 for n in lst]

cubes=[n**3 for n in lst]

even_numbers = [n for n in lst if n%2==0]
odd_numbers = [n for n in lst if n%2!=0]

print(squares)
print(cubes)
print(even_numbers)
print(odd_numbers)

words=["fly","flyin","flyout","flyoff","out","in"]

# print list of words starting with fly

filter_words=[w for w in words if w.startswith("fly")]
print(filter_words)