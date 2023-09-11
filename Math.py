# If you add, subtract, multiply, or take the modulus of an integer value with a float value, the result will be a float value.

print(20 + 15.2)
print(10 % 5.0)

# Regardless of whether it's an integer or a float value, when division is used in mathematical operations, the result is in the float data type.

print(46 / 23)

# The ** symbol is used to raise a number to a power.

print(2 ** 3)

# // is the expression for finding divisors. It results in an integer.

print(7 // 2)

# "%" is the expression used for taking the modulus.

print(9 % 2)

a = 3       # To increment the 'a' value by one at a time, 

a += 1

s1 = "Sultan"
s2 = 'Sultan'

print(s1)
print(type(s1))
print(s2)
print(type(s2))

s3 = "I'm Sultan"
s4 = 'I\'m Sultan' # We cannot use the expression we use when defining a string inside the string itself. In cases where we need to use the expression inside the string, we should use a backslash before the expression in the string.
print(s4)

s5 = """This is a way of defining a string."""
print(s5)

mes = "Sultan Keles"

print(mes[0])
print(mes[-5])
print(mes[:7 :3])
print(mes[0 :40 :2])
print(mes[-15:-7])  # It starts from zero and goes up to negative seven.
print(mes[::-1])