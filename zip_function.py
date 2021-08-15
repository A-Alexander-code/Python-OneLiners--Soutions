list_1 = [1,2,3]
list_2 = [4,5,6]

# Zip two list together
zipped = list(zip(list_1,list_2))
print(zipped)

# Uzip to list again
new_list_1, new_list_2 = zip(*zipped)
print(new_list_1)
print(new_list_2)