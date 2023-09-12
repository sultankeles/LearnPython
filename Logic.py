# strip searches for trimming from both the right and left sides.
not1 = "  Python is a very nice language. "
notel_3 = not1.strip(" P")
print(notel_3)

# lstrip searches for trimming from the left, while rstrip searches for trimming from the right.
not2 = "  Python is a very nice language.  "
notel_4 = not2.lstrip(" Python")
print(notel_4)

# To check if only letters are used in the entered text,

a = "abcd"
b = a.isalpha()
print(b)

c = "abcd8"
d = c.isalpha()
print(d)

# To check if only numbers are used in the entered text,

n = "1234"
m = n.isdigit()
print(m)

# To find the index number of an element in the entered text,

x = "Ali bana to at"
y = x.index("to")
print(y)

s = "Ali bana to at"
r = s.isupper()
print(r)

# LOGICAL OPERATORS


d_e = "sultankeles.....@....com"
d_p = "Test123"

w_e = "sultankeles...@...com"
w_p = "Test123"

o_1 = d_e == w_e
o_2 = d_p == w_p

print(o_1)
print(o_1 and o_2)
print(not o_1 and o_2)
print(o_1 or o_2)
print(o_1 or not o_2)

# In logical operators, 0 represents False.

print(bool(0))
print(bool(0.0))
print(bool(0+0j))
print(bool(None))
print(bool([])) # An empty list is always considered False.
print(bool({})) # An empty dictionary is always considered False.
print(bool(set())) # An empty set is always considered False.
print(bool(())) # An empty tuple is always considered False.
print(bool("")) # An empty string is always considered False.


q = not False and True
print(q)

w = True or False and False
print(w)

t = 5 and "string" and ["a"] and [] and True
print(t)

j =  ["a"] and "False" and 1 and "True" and {"true":"true"}
print(j)

o = 0 or "" or 1 or []
print(o)

f = [] or False or 0 or {}
print(f)

# In JavaScript,
# The expression 2 == '2' (checks if both are 2).
# The data types 2 === '2' (check if their data types are the same).

# But in Python,
2 == "2" # When we query it like this, it checks both the value and the data type.

d_p = "Test123"
d_w = "Test123"

output = d_p != w_p

print(output)

g = 54
h = 54

print(g >= h)
