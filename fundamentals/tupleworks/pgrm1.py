names = {"hari","sukumar","hello","hello","hp"} # set object - curly bracket
# new_names = ["hp","dell","lenovo"] # square bracket is list object
new_names = {"hp","dell","hello","lenovo"} # set object - curly bracket

# print(names)

# s=set()
# print(type(s))
# duplicates not allowed
# elements are not in order
# cannot fetch a ojbect using index position in set object
# mutable: we can add or remove the elements in the set

# names.add("Kochi") # to add a new element
# print(names)
# names.clear() # clears the set
# print(names)
# names.pop() # removes an element randomly
# print(names)
# names.discard("Hello") # to remove an element decided by user
# print(names)
# names.update(new_names) # will add elements from any collection to the set
# print(names)
# union()
# intersection()
# difference()
# new_names_set=names.union(new_names) # return the elements from two sets and return as a new set
# print(new_names_set)

# new_names_set=names.intersection(new_names) # return common elements and assign in a new set
# print(new_names_set)

# new_names_set=names.difference(new_names) # return element from set names whihc is not in set new_names as new set
# print(new_names_set)

new_names_set=names.symmetric_difference(new_names) # combine all elements from 2 set and remove common elements
print(new_names_set)

