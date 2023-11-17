'''
This file contains the functions that are used to manipulate the dictionary
'''

'''
A dictionary is a collection of Key:Value pairs, used to store data as a map.
As of Python 3.7 dictionaries are ordered
'''

##### Creating a dictionary ########
# 1. Using the curly braces
my_dict = {1:"Hey", 2:"There", 3:45.6, "John":69 }
print(my_dict, " <-- My dictionary")
# values can be anything, but keys can't be duplicate and must be immutable

# 2. Using dict keyword
my_dict = dict([(1, "Hey"), (2, "There"), (3,45.6), ("John", 69)])
print(my_dict, " <-- My dictionary using dict keyword")

# 3. Using dict as a constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict,  " <-- My dictionary using dict as a constructor")

##### Creating a nested dictionary ########

my_dict_nest = {1: 'India', 2: 'Australia', 3: {'A': 'New York', 'B': 'Los Angeles', 'C': 'College Park'}}
print(my_dict_nest, " <-- Nested dictionary")

##### Adding elements to a dictionary ########
my_dict = {1:"Hey", 2:"There", 3:45.6, "John":69 }
print(my_dict, " <-- My dictionary")
my_dict[4] = "Johnny"
print(my_dict, " <-- My dictionary with a new element added")

##### Accessing elements of a dictionary ########
a = my_dict[3]
print(a, " <-- Value of the element with key 3 in the dictionary")

##### Updating elements to a dictionary ########
my_dict[3] = 23.908
print(my_dict, " <-- My dictionary with a updated elements")

##### Length of a dictionary ########
c = len(my_dict)  # returns the number of keys in dictionary
print(c, " <-- Length of the dictionary")

##### Accessing elements of a nested dictionary ########
my_dict_nest = {1: 'India', 2: 'Australia', 3: {'A': 'New York', 'B': 'Los Angeles', 'C': 'College Park'}}
b = my_dict_nest[3]['A']
print(b, " <-- Accessing value from a Nested dictionary")

# del(my_dict["John"])  # Will delete the associated key vlaue pair from the dictionary
# del my_dict  # Will completely delete the dictionary from memory

############################################
########### Other Dict methods #############
############################################

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"} 
print(dict1, " <-- Original Dictionary")

# copy()  -  makes a copy of the dictionary
dict2 = dict1.copy()
print(dict2, " <-- Copy of the original dictionary")

# clear()  -  deletes the contents of the dictionary
dict1.clear()
print(dict1)  # prints empty dictionary

# get(key)  -  returns the vlaue of the key
a = dict2.get(1)
print(a, " <-- Value accessed using get method")

# items()  -  returns a list containing a tuple for each key value pair
print(dict2.items(),  " <-- Items of the dict")

# keys()  -  returns a list containing the dictionary's keys
print(dict2.keys(),  " <-- Keys of the dict")

# values()  -  returns a list containing the dictionary's values
print(dict2.values(),  " <-- Values of the dict")

# pop(key)  -  removes and returns the element of specified key
print(dict2.pop(4),  " <-- Items popped from the dict")

# update({key:value})  -  adds a new key:value pair to dictionary
dict2.update({4:"C++"})
print(dict2,  " <-- Updated a new item to the dict")