# We define tuples using () brackets.
# Tuples are similar to lists; the only difference is that tuples are immutable.
# Even when creating a single-element variable, we should always append a comma to the end.

name = "Sultan"

tuple_1 =(name,)

print(tuple_1)
print(type(tuple_1))


tuple_2 = tuple(name)

print(tuple_2)
print(type(tuple_2))


tuple_3 = ()

print(tuple_3)
print(type(tuple_3))


# We don't need to use () to define a tuple with more than one element.

t_1 = "ali", "ahmet", "veli"

print(t_1)
print(type(t_1))


# Since tuples are immutable, if we want to make any changes, we can convert the tuple we want to manipulate into a list, make the modifications, and then convert it back into a tuple.

tpl_fruit = ("Apple", "Pear", "Quince", "Melan")

print(tpl_fruit)
print(type(tpl_fruit))

# Tuple >> List
list_fruit = list(tpl_fruit)

print(list_fruit)
print(type(list_fruit))


# Editing 
list_fruit[3] = "Melan"

list_fruit.append("Melon")

print(list_fruit)


# List >> Tuple
tpl_fruit = tuple(list_fruit)

print(tpl_fruit)
print(type(tpl_fruit))

# Lists and tuples, being ordered, allow us to access their elements using index numbers.

# They can contain the same element multiple times and can include different data types.

mix_tuple = (22, True, 22, [1,2,3,3], {1,2,3}, "Sultan", 2.0, {1,2,3}, {"a":1})

print(mix_tuple)
print(type(mix_tuple))



names = "Ali", "Veli", "Ahmet"
notes = 20,56,90

print(f"{names[0]} scored {notes[0]} points on the exam.")

s = (
    ("Ali", 30),
    ("Ahmet",34),
    ("Ayşe", 54),
)

print(f"{s[0][0]} scored {s[0][1]} points on the exam.")


# If we want to change 'Winter squash' to 'Marrow',

vegetable_tuple = ("Onion", "Garlic", "Eggplant", "Winter squash ", "Onion")

print(vegetable_tuple[3])

# vegetable_tuple[3] = "Marrow" We received an error because tuples are immutable.

list_vegetable = list(vegetable_tuple)

print(list_vegetable)

list_vegetable[3] = "Marrow"

print(list_vegetable)

vegetable_tuple = tuple(list_vegetable)

print(vegetable_tuple[3])


print(vegetable_tuple[:])
print(vegetable_tuple[:3])
print(vegetable_tuple[2:])
print(vegetable_tuple[::-1])

# We can determine the number of elements it contains using the len method.

print(len(vegetable_tuple))


# To find out how many occurrences of an element there are, we use the count method. It is case-sensitive.

print(vegetable_tuple.count("Onion"))
print(vegetable_tuple.count("onion")) 

# We can find the index number of an element using the .index method.

print(vegetable_tuple.index("Onion"))
