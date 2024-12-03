### LOOPS ###

# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

### LISTS ###

# iterate through items in an array
arr = [1, 2, 3, 4, 5]
for item in arr:
    print(item)

# iterate through items in a list with index
for i, item in enumerate(arr):
    print(i, item)

# list comprehension
# create a new list with the items of the old list multiplied by 2
new_arr = [item * 2 for item in arr]
print(new_arr)

# create a new list with the items of the old list that are greater than 2
# like filter in js
new_arr = [item for item in arr if item > 2]
print(new_arr)

### DICTIONARIES ###

# iterate through items in a dictionary
my_dict = {"key1": "value1", "key2": "value2"}
for key, value in my_dict.items():
    print(key, value)

# add a new item to a dictionary
my_dict["key3"] = "value3"
print(my_dict)

# delete an item from a dictionary
del my_dict["key1"]
print(my_dict)

# create a new dictionary with the items of the old list multiplied by 2
new_dict = {item: item * 2 for item in arr}
print(new_dict)

# create a new dictionary with the values of the old dictionary multiplied by 2
old_dict = {"a": 1, "b": 2, "c": 3}
new_dict = {key: value * 2 for key, value in old_dict.items()}
print(new_dict)  # Output: {"a": 2, "b": 4, "c": 6}


### SETS ###

# create a new set with the items of the old arr multiplied by 2
new_set = {item * 2 for item in arr}
print(new_set)  # Output: {2, 4, 6, 8, 10}
