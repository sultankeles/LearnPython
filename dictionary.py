# A dictionary is defined with {}.
# Keys are immutable! But the values can be changed.
# The elements are ordered, but we cannot access them using an index; we use keys for that.

dict1 = {"a":1, "b":2, "c":3}

print(dict1)
print(type(dict1))

# While defining with the dict function, we should avoid using quotation marks.

dict1 = dict(a=1, b=2, c=3)

print(dict1)
print(type(dict1))

# To create an empty dictionary,

dict2 = {}

print(dict2)
print(type(dict2))


# To access the value of the respective key,

city_number_plate = {
    "İstanbul":34,
    "İzmir":35,
    "Sakarya":54,
    "Karadeniz":["Rize",53, "Trabzon", 61]
}

print(f"The license plate of Istanbul is: {city_number_plate['İstanbul']}")

print(f"{city_number_plate['Karadeniz'][0]} plakası :{city_number_plate['Karadeniz'][1]}")



# The value of the desired key in the respective dictionary can be changed.

city_number_plate["Karadeniz"] = "Sinop"
print(city_number_plate)

# If we write a non-existent key, we can still add a new key:value pair by using the assignment operator and providing a value.

city_number_plate["Marmara"] = "İstanbul"
print(city_number_plate)




mix_key ={
    2 : "int 2",
    1.2 : "float 1.2",

    "One" : "String 1",
    True : "Boolean",
    #(0, 1.0, True, "One"): "Tuples can also be defined as keys.",
    True : "Boolean 1"
}

print(mix_key)
#print(mix_key[{0, 1.0, True, "One"}])



d_1 = {
    "car":"Jeep",
    "year":2023
}

# To access the keys,

print(d_1.keys())
d_1_keyleri = d_1.keys()
print(d_1_keyleri)

# To access the values,

print(d_1.values())

# To access both keys and values,

print(d_1.items())

# To add,

d_1['vites'] = "Automatic"

print(d_1)

d_1.update({"fuel consumption": " Gas"})

print(d_1)


# To delete a key:value pair,

d_2 = {
    "artist": "L D V",
    "work": "Mona Lisa",
    "Language": "Python",
    "Year": 1991
}

print(d_2)

del d_2["work"]

print(d_2)


# To check if a key is in the key-values,

print("artist" in d_2)
print("Mona Lisa" in d_1)

# We can create dictionaries consisting of multiple nested key:value pairs.


print()


d_4 = {
    "a":"Sultan Keleş",
    "b":"Pakize Kılıç"
}

deleted_key_value = d_4.pop("a")

print(deleted_key_value)



# We can delete all the key:value pairs inside the dictionary using the .clear method.

d_5 = {
    "a":"Sultan Keleş",
    "b":"Pakize Kılıç"
}

d_5.clear()
print(d_5)
