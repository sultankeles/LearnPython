products = ["iphone11", "iphone12", "iphone13", "iphone14", "samsung s22"]

print(products[0])
print(products[1])
print(products[2])
print(products[3])
print(products[4])

# This operation is a repetitive task. We can express this using loops in a more concise way.

for pro in products:
    print(pro)



# When the condition is true, the code block executes, and it continues the loop until the condition becomes false.

count = 0
while len(products) > count:  # number of products > count 
    print(products[count])
    count += 1


# If we make a logical error, such as not incrementing a variable, the condition may never become false, and we can initiate an infinite loop. Therefore, we must ensure that we specify the condition to exit the loop, and the only way to stop such an infinite loop is to close VS Code.


# x = int(input("Number : "))

# while x > 0:
#     print("Entered Number: ", x)
#     x = int(input("Number : "))
# print("You did not enter a number that meets the condition.")




number = 0

while number < 6:
    print(number)
    number += 1
print('Now, number is bigger or equal to 6')




my_list = ["a", "b", "c", "d", "e"]

a = 0

while a < len(my_list):
    print("square of {} is : {}".format(a, a**2))
    a += 1



# Guessing Game

answer = 44
question = " What number am I thinking of? "
print ('Let\'s play the guessing game!')

while True:
    guess = int(input(question))

    if guess < answer:
        print("Little higher")

    elif guess > answer:
        print("Little lower")

    else:   # guess == answer
        print("Are you a MINDREADER !!!")
        break   # is used to end the loop.





# ITERABLE

for c in "hey":
    print(c)


seasons = ['spring', 'summer', 'autumn', 'winter']

for season in seasons:
    print(season)


list = [1,2,3,4,5]
for list_elements in list:
    if list_elements % 2 == 0:
        print(list_elements)
        break


for key in {"n1":"one", "n2":"two"}:
    print(key)  # Only keys are printed.


for key in {"n1":"one", "n2":"two"}.values():
    print(key)  # Only values are printed.





# RANGE

for a in range(3,15):
    print(a)


sum = 0
for y in range(10):
    sum = sum + y
    print(sum)

print(*range(0,5))
print(*range(10,0,-2))



# (start:stop:step) is valid within the context of range, and we are specifying a stop point. Therefore, in the example below, range(5) is actually equivalent to range(0, 5, 1).
b = 1
for _ in range(5): 
    b *= 5
    print(b)



n = int(input('Enter a number between 1-10'))

for i in range(11):
    print('{}x{} = '.format(n, i), n*i)



d = list(range(11))

print(d)

print(range(5))     # it will not print the numbers in sequence

print(*range(5))    # '*' separates its elements

print(*('separate'))



# Nested For Loop

list1 = ["one", "two", "three"]
list2 = [1, 2, 3]

for x,y in zip(list1, list2):
    print(f"{x}:{y}")

# We got an output like one:1, two:2 because the inner loop didn't reset before moving to the next iteration. 

# However, it displays the same number of elements;

list3 = ["one", "two", "three", "four"]
list4 = [1, 2, 3]

for z,q in zip(list3, list4):
    print(f"{z}:{q}")



who = ['I am ', 'You are ']
mood = ['happy', 'confident']

for i in who:
    for ii in mood:
        print(i + ii)



sum_num = 0

for i in range(1, 75):
    sum_num += i
print(sum_num)


for i in range(1,4):
    for j in range(1,4):
        print(i, j)



prime = []  # created an empty list to collect prime numbers in it

for num in range (2, 101):
    status = True
    for i in range(2, num):
        if num % i == 0:    # check if the only factors are 1 and itself
            status = False
    if status:
        prime.append(num)   # collect prime numbers in the list

print(prime)
