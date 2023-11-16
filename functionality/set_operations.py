'''
This file contains the functions that are used to manipulate the set
'''

'''
A Set is an unordered collection of data that is iterable, mutable and has no duplicates allowed
'''

##### Creating a set ########
my_set = {"Hey", 1.0, 69}   # by using the curly braces
print(my_set, " <-- My initial set")

my_set = set(["Hey", 1.0, 69])  # by typecasting
print(my_set, " <-- My initial set using typecasting")

##### Adding elements to a set ########
my_set.add(5)
print(my_set, " <-- Updated set")

##### Creating a frozen set ########
my_set_frozen = frozenset(["tell", 99, 45.87])  # frozen sets are immutable
# my_set_frozen.add("g")  # this would result in an error

##### Merging two sets ########
# 1. Union function
people = {"Hemanth", "Bharadwaj", "Emre"}
vampires = {"Dracula", "Renfield"}

population = people.union(vampires)
print(population, " <-- Sets merged using union")

# 2. | operator
people = {"Hemanth", "Bharadwaj", "Emre"}
vampires = {"Dracula", "Renfield"}

population = people|vampires
print(population, " <-- Sets merged using | operator")

##### Finding intersection between two sets ########
# 1. Intersection function
set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)

common_set = set1.intersection(set2)
print(common_set, " <-- Common elements in both sets found using intersection function")

# 2. & Operator

common_set = set1&set2
print(common_set, " <-- Common elements in both sets found using & Operator")

##### Finding difference between two sets ########
# 1. Difference function
diff_set = set1.difference(set2)
print(diff_set, " <-- Uncommon elements in both sets found using difference function")

# 2. - Operator
diff_set = set1-set2
print(diff_set, " <-- Uncommon elements in both sets found using - Operator")

##### Clearing a set ########
set1.clear()
print(set1, "<-- Empty set")

##### Multiple additions to a set ########
test_set = {6, 4, 2, 7, 9}
new_elements = [1, 5, 10]
print(test_set, " <-- Original set")
print(new_elements, " <-- New elements to be added")
test_set.update(new_elements)
print(test_set, " <-- Updated list, unlike union, update orders the list internally")

##### Removing elements a set ########
test_set = {6, 4, 2, 7, 9} 
test_set.pop()  # removes elements in ascending order
print(test_set, " <-- Popped the smalled element")
test_set.discard(7)
print(test_set, " <-- Discarded the element 7")