# if is a conditional statement used to create a code block.
b_k = 15
if b_k > 5:
    print("There are still empty seats to sit.")

print(b_k<5)

# else bir if ifadesi gibi çalışır. if ifadesinin içindeki hiçbir koşul sağlanmazsa, diğer koşulları çalıştırmak için else kullanılır.

kurs = "Cosmios"

if kurs == "Cosmios":
    print("A fantastic training center.")

# else:
#    print("You should think again.")

if kurs != "Cosmios":
    print("You should think again.")


# if is used for the first one,
# elif for the rest (optional) until the end,
# else is used for anything not caught by other conditional statements.

weight = 80

if weight > 100:
    print("That's too heavy! ")

elif weight > 75 :
    print("I can lift that! ")

else:
    print("That's too light! ")


# name = input("Please enter your name : ")
# print("Entered name : ", name)
# print(type(name))



# age = int(input("Please enter your age : "))
# print("Entered age : ", age)
# print(type(age))


n1 = int(input("Please enter number 1: "))
n2 = int(input("Please enter number 2: "))
n3 = int(input("Please enter number 3: "))

if (n1 >= n2 and n1 >= n3):
    print(f"The largest number {n1}")
    print("First block")

elif (n2 >= n1 and n2 >= n3):
    print(f"The largest number {n2}")
    print("Second block")

else:
    print(f"The largest number {n3}")

    


# age = int(input("Please enter your age : "))

# if age >=0:

#     if age >= 0 and age <= 8:
#         audience = "Baby"

#     elif  age >= 8 and age <= 16:
#         audience = "Kid"

#     elif  age >= 17 and age <= 25:
#         audience = "Young"
    
#     else:
#         audience = "Adult"



#     if audience == "Kid":
#         print("It is free to go to cinema! ")

#     elif audience == "Young":
#         print("Discounted price! ")

#     elif audience == "Adult":
#         print("Normal price.")

#     else:
#         print("You are not suitable to go to the cinema.")


# else:
#     print("You entered an invalid age.")    




age = int(input("Please enter your age : "))

if age > 0 and age < 100:
    if age >=0 and age <= 7 :
        audience = "Baby"
        if audience == "Baby":
            print("Not an appropriate age to go to the cinema !")

    elif age >=8 and age <=16 :
        audience = "Kid"
        if audience == "Kid":
            print("It is free to go to cinema!")

    elif age >=17 and age <=25 :
        audience = "Young"
        if audience == "Young":
            print("Discounted price! ")
    else: 
        audience = "Adult"
        print("Normal price.")
else:
    print("You entered an invalid age.")


score = int (input("Enter your score : "))

if score >= 90:
    if score >=95:
        Score_letter = "A+"
    else:
        Score_letter = "A"
elif score >= 80:
    if score >=85:
        Score_letter = "B+"
    else:
        Score_letter = "B"
else:
    Score_letter = "Below B"

print("Your degree %s" % Score_letter)





# TERNATY

# <value-1> if <condition> else <value-2>

x = 0
y = 19

max_value = x if x>y else y
print(max_value)

a = x if x > y else y

if x > y:
    print(x)

else:
    print(y)

    

is_even = "Even" if x % 2 == 0 else "Odd"
is_even_2 = "Odd" if y % 2 != 0 else "Even"
print(is_even)
print(is_even_2)


result = "Pozitive" if x > 0 else ("Negative" if x <0 else "None")
print(result)
