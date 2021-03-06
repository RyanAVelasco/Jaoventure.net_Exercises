import random


print("""
=== 5.1: Exercises with the for loop ===
1. Create a function "add" that receives a list as parameter and returns the sum of all elements in the list. 
Use the "for" loop to iterate over the elements of the list.
2. Create a function that receives a list as parameter and returns the maximum valuein the list. 
As you iterate over the list you may want to keep the maximum value found so far in order to keep comparing 
it with the next elements of the list.
3. Modify the previous function such that it returns a list with the first element being the maximum value 
and the second being the index of the maximum value in the list. 
Besides keep the last maximum value found so far, you need to keep also the position where it occured.
4. Implement a function that returns the reverse of a list received as parameter. You may create an empty list and 
keep adding the values in reversed order as they come from the original list. 
Check what you can do with lists at https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.
5. Make the function "is_sorted" that receives a list as parameter and returns True if the list is sorted 
by increasing order. 
For instance [1, 2, 2, 3] is ordered while [1,2, 3, 2] is not. 
Suggestion: you have to compare a number in the list with the next one, so you can use indexes or 
you need to keep the previous number in a variable as you iterate over the list.
6. Implement the function "is_sorted_dec" which is similar to the previous one but all items must be sorted 
by decreasing order.
7. Implement the "has_duplicates" function which verifies if a list has duplicate values.
You may have to use two "for" loops, where for each value you have to check for duplicates on the rest of the list.""")

print("""
=== Answer 1 ===""")
list =[127,239,203,874,115,706,477,108,109,160]
sum = 0

def add(x):
    global sum
    
    for val in list:
        print(list, val)
        sum += val
    return "The total sum of the list is: " + str(sum)
    
    
print(add(sum))


print("""
=== Answer 2 ===""")

def findMax(L):
    global maxValue
    
    for n in L:
        if maxValue > n:
             print("Max:", maxValue, "and Current:", n)
             continue
        else:
             maxValue = n       
             print("Max:", maxValue, "and Current:", n)
   
    print("The largest value found is:", maxValue)
    

maxValue = -9999

numberList = [22,32,11,37,27,33,38,13,23,2,20,27,46,83,98,89]
print("Number List:", numberList)


findMax(numberList)


print("""
=== Answer 3 ===""")


def findMax(L):
    global maxValue
    
    for i, n in enumerate(L):
        if maxValue > n:
             print("Index:", i, "and Max:", maxValue, "and Current:", n)
             continue
        else:
             maxValue = n       
             print("Index:", i, "and Max:", maxValue, "and Current:", n)
   
    print("The largest value found is:", maxValue)
    

maxValue = -9999

numberList = [22,32,11,37,27,33,38,13,23,2,20,27,46,83,98,89]
print("Number List:", numberList)


findMax(numberList)


print("""
=== Answer 4 ===""")
def reverse(list):
    list.reverse()
    return "Sorted List:", list


count = 0
numbers = []

while count < 10:
    numbers.append(random.randint(0, 50))
    count += 1

print("Original List:", numbers)
print(reverse(numbers))


print("""
=== Answer 5 ===""")


def is_sorted(list):
    list.sort()
    prev_number = list[0]
    for n in list:
        if prev_number > n:
            return "failed"
        else:
            return True
    print(list)

count = 0
numbers = []

while count < 10:
    numbers.append(random.randint(0, 50))
    count += 1
print("Unsorted list:", numbers)

print(is_sorted(numbers))

print("Sorted List:", numbers)


print("""
=== Answer 6 ===""")


def is_sorted_dec(list):
    list.sort()
    list.reverse()
    return list


count = 0
numbers = []

while count < 10:
    numbers.append(random.randint(0, 50))
    count += 1

print("Original List:", numbers)
print("Sorted list:", is_sorted_dec(numbers))


print("""
=== Answer 7 ===""")\


def has_duplicates(list):
    pass


numbers = []
insertNumbers = 0
loops = 0

while insertNumbers < 100:  # input any here
    numbers.append(random.randint(0, 100))  # input any range
    insertNumbers += 1

print("Original List:", numbers)

while loops < 100:  # match number in while insertNumbers
    for n in numbers:
        count = numbers.count(n)
        if numbers.count(n) > 1:
            index = numbers.index(n)
            del numbers[index]
    loops += 1
numbers.sort()
print("No duplicate list:", numbers)



print("""
=== 5.2: Exercises with the while statement ==
Implement a function that receives a number as parameter and prints, in decreasing
order, which numbers are even and which are odd, until it reaches 0.

>>> even_odd ( 10)
Even number : 10
Odd number : 9
Even number : 8
Odd number : 7
Even number : 6
Odd number : 5
Even number : 4
Odd number : 3
Even number : 2
Odd number : 1
""")

print(""" 
=== Answer 1 ===
Super easy problem
""")

def even_odd(x):
    while x != 0:
        if x % 2 == 0:
            print("Even number:", x)
            x -= 1
        else:
            print("Odd number:", x)
            x -= 1
 
num = input("Please enter a number: ")
even_odd(int(num))