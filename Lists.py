a, b, *c = 10, 20, 30, 40

print(a)
print(b)
print(c)

# TO CREATE A LIST

name = "sultan"

list_1 = [name]

print(list_1)
print(type(list_1))

# To list the elements of the string expression we created,
list_2 = list(name)

print(list_2)
print(type(list_2))

# To create an empty list,
list_3 = []

print(list_3)
print(type(list_3))


#To create a list within a list,
list_4 = [11, 11.0, "onbir", True, ["True"], ("a","n"), {1,2,3}, {"True":True}]

print(list_4)
print(type(list_4))

# Lists are mutable. Additions and removals can be made later.

# .append() allows us to add an object to the end of the list. However, we cannot obtain output using the list.append(element) formula. To get the output, we should print the list.

list_5 = [1,2,3,4]
print(list_5)

list_5.append("Numbers")
print(list_5)

# .insert()list : It allows us to add an object to a specific position in the list.

list_6 = ["a", "b", "c"]
list_6.insert(0, "z")

print(list_6)

# .remove() : It allows us to delete the desired element from the list.

# If there are multiple occurrences of an element, it deletes the first one and then stops.

list_7 = [2,"f",True,1.0,9]
list_7.remove(9)

print(list_7)

list_7_2 = [2,9,"f",True,1.0,9]
list_7_2.remove(9)


print(list_7_2)


# It is used to print in ascending order or alphabetically.

list_8 = [9,3,7,5,6,54,23]
list_8.sort()

print(list_8)


list_9 = ["ala", "ida", "qal", "85"]
list_9.sort()

print(list_9)
print(len(list_9))

# We can permanently change the desired index number of the relevant list using assignment operators along with square brackets.


car = ["Opel", "Dacia", "Mazda", "Toyota"]

car[0] = "Honda"

print(car)


car[0:2] =  ["BMW", "Mercedes"]

print(car)

# If we write fewer elements than specified, it deletes the elements we didn't modify from the list.

car[0:2] =  ["Audi"]

print(car)

# If we write more elements than specified, it continues to change the list sequentially.

car[1:2] =  ["Tesla", "RR", "Ferrari"]

print(car)

# We access the list with city_list[0] .
# We access the second element of the list with city_list[0][2].

s= [["Ali",70], ["Veli", 49], ["Derya", 99]]

print(s[0])

print(f"{s[0][0]} scored {s[0][1]} points on the exam.")

print(f"{s[1][0]} scored {s[1][1]} points on the exam.")

print(f"{s[2][0]} scored {s[2][1]} points on the exam.")

# The syntax to slice an array is as follows:
# [start : stop : step] 
# If no start value is given, it is assumed to be 0 by default. If no stop value is given, it is considered as the last element. If no step value is specified, it is assumed to be 1.
