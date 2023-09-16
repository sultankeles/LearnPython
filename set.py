# Sets are not ordered.
# Elements cannot repeat themselves.
# Elements are immutable!!! However, an element can be removed or a new element can be added.
# It is defined using set() or {}, but if we want to create an empty set, we must use the set() function.

set_1 = {1,"v", 3}

print(set_1)
print(type(set_1))



#set_2 = set([1,2,3,{1,2,"d",3}])

#print(set_2)
#print(type(set_2))



set_3 = set()

print(set_3)
print(type(set_3))


set_4 = {"apple", "banana", "apple"}

print(set_4)

set_5 = "AppleApllea...PPLE"

set_5_1 = set(set_5)

print(set_5_1)

# After converting any list to a set, duplicate elements within it are reduced to unique ones, but when we convert it back to a list, it does not return to its duplicated state and remains in the form it was in the set.

list1 = ["Apple", "Apple", True, 23, 0.8, "banana", "Banana", 1]
print(list1)



# The .add() method is used to add an element to the respective set.

set_7 = {1,2,3,4}

set_7.add(5)

print(set_7)


# If we want to copy a set into another set, we must use the .copy() function; otherwise, any changes made to the copied set will also affect our reference set.

set_8 = set_7.copy()

set_8.add("a")

print(set_8)
print(set_7)

# When comparing different elements, it compares the elements between sets of the same length. Since they are unordered, it does not check them sequentially; it only lists the differences.

set_9 = {1, 2, 3, 4, 'a', 6, 5, 8}
set_new = {1, 2, 3, 4, 5, 'a', "x", 10}

diff_set = set_9.difference(set_new)

print(diff_set)

