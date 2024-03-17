ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here 

# Lists are ordered and mutable collections that allow duplicate elements.
# I can modify elements by their index.
ft_list[1] = "World!"

# Tuples are ordered and immutable collections that allow duplicate elements.
# I converted the tuple to a list, modified it, then converted it back to a tuple.
tmp = list(ft_tuple)
tmp[1] = "Morocco!"
ft_tuple = tuple(tmp)

# Sets are unordered, mutable collections that do not allow duplicates.
# We can remove an element and add another one to change the value.
ft_set.remove("tutu!")
ft_set.add("Ben Guerir!")

# Dictionaries are ordered mappings of unique keys to values.
# I updated the value associated with the key "Hello".
ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
