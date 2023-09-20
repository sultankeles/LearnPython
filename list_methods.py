list_1 = ["iphone", "samsung", "oppo", "huawei"]

# We can delete an element from the array based on its index number. If we don't specify any index number, it deletes the last element.

# While other deletion methods do not return the deleted variable, the pop method allows us to assign the deleted variable to another variable and use it as a value.

list_1_sil = list_1.pop(1)

print(list_1_sil)
print(list_1)



# The count method counts how many times the same element appears in a list. When an non-existent value is entered, it returns 0.

list_2 = ["iphone", "samsung", "oppo", "huawei"]

list_2_say = list_2.count("oppo")
list_2_say_2 = list_2.count("s")

print(list_2)
print(list_2_say)
print(list_2_say_2)



# We can make additions to the list using the .append method.

list_2.append("google")

print(list_2)



# We can assign another list to reference the original list without altering it.

list_3 = ["iphone", "samsung", "oppo", "huawei"]

list_3_copy = list_3

print(list_3_copy)

# However, when assigned in this way, any changes made to list_3_copy will also affect the original list (list_3).

list_3 = ["iphone", "samsung", "oppo", "huawei"]

list_3_copy = list_3
list_3_copy.append("sultan")

print(list_3_copy)
print(list_3)


# To make changes only to the copied list without altering the original list, we need to use the .copy() method.

list_4 = ["iphone", "samsung", "oppo", "huawei"]

list_4_copy = list_4.copy()
list_4_copy.append("google")

print(list_4)
print(list_4_copy)



# We can query the index number of the desired element using the .index method. Even if there are multiple occurrences of the same element, it will output the index number of the first one it finds and won't continue checking the rest.

list_3 = ["iphone", "samsung", "oppo", "huawei", "oppo"]

print(list_3.index("oppo"))


# The .reverse method reverses the order of the list to its original sequence.

list_3 = ["iphone", "samsung", "oppo", "huawei", "oppo"]

list_3.reverse()

print(list_3)



# With the .extend method, we can add the current list to another mutable data structure (set, dictionary, list, etc.), making it mutable as well.

list_4 = ["iphone", "samsung", "oppo", "huawei", "oppo"]
list_5 = ["google", "casper", "xiaomi", "generel mobile"]

list_4.extend(list_5)

print(list_4)
