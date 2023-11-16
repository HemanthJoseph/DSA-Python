'''
This file contains the functions that are used to manipulate the tuple
'''

'''
Tuple is a collection of Python objects, similar to a list
Tuples are immutable
'''

##### Creating a tuple ########
my_tuple = (1, 2, 6.8, "Hello")
print(my_tuple)

##### Creating a tuple with single element ########
# there must be a trailing comma
my_tuple = (1,)
print(my_tuple, type(my_tuple))

##### Accessing elements of a tuple ########
my_tuple = (1, 2, 6.8, "Hello")
a = my_tuple[0]
print(a, " <-- First element of the tuple")

##### Unpacking elements of a tuple ########
a, b, c, d = my_tuple
print(a, b, c, d, " <-- Tuple values unpacked")

##### Concatenating of tuples ########
my_tuple1 = (1, 5.9, "Steven")
my_tuple2 = ("Dell", 68, 90.34)
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3, " <-- New tuple after concatenation")

##### Slicing of a tuple ########
my_tuple = (1, 2, 6.8, "Hello")
print(my_tuple[:2], " <-- First two elements of the tuple sliced")
print(my_tuple[::-1], " <-- Reversing the elements of the tuple by slicing")

# del my_tuple1 # deteles the whole tuple

############################################
########### Other Tuple methods #############
############################################
'''
my_list.index(element) - return index of first occurence of element in tuple
my_list.count(element) - return the count of number of occurences of element in tuple
'''