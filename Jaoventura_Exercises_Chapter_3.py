import random

print("All exercises here can be found at: http://joaoventura.net/static/files/python_exercises_book.pdf")
print("""\n\n3.1: Exercises with numbers
1. Try the following mathematical calculations and guess what is happening:(3/2),(3//2),(3%2),(3∗∗2).
Suggestion: check the python library reference at https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex.
2. Calculate the average of the following sequences of numbers: (2, 4), (4, 8, 9), (12,14/6, 15)
3. The volume of a sphere is given by 4/3πr. Calculate the volume of a sphere of radius 5. 
Suggestion: create a variable named "pi" with the value of 3.1415
4. Use the module operator (%) to check which of the following numbers is even or odd: (1, 5, 20, 60/7).
Suggestion: the remainder of x / 2 is always zero when x is even.
5. Find some values for x and y such that x < 1/3 < y returns "True" on the PythonREPL. 
Suggestion: try 0 < 1/3 < l on the REPL.""")

print("\n=== Answer 1 ===")
print("Division:", 3/2)
print("Floor Division", 3//2)
print("Finding the remainder:", 3%2)
print("Multiplying to the power of 2:", 3**2)

print("\n=== Answer 2 ===")
x = [2, 4]
y = [4, 8, 9]
z = [12, 14/6, 15]

print("Average of list x:", sum(x)/len(x))
print("Average of list y:", sum(y)/len(y))
print("Average of list z:", sum(z)/len(z))

print("\n=== Answer 3 ===")
pi = 3.1415
print(4/3 * pi * 5)

print("\n=== Answer 4 ===")
num = [1, 5, 20, 60/7]
for n in num:
    o = n%2
    if o == 0:
        print(n, "is even")
    else:
        print(n, "is odd")  # 60/7 comes of as odd, I'm not sure if it would be though considering it is 8

print("\n=== Answer 5 ===")  # This is a boring question so I'm making an alternate
count = 0
while count < 10:
    x = random.random()
    if 0 < x < 1:
        print(x, "makes this statement", True)
    else:
        print(x, "makes this statement", False)
    count += 1

print("\n=== Answer 5.alt ===")
count = 0
while count < 20:
    x = random.randint(-100, 1000)
    y = random.randint(-100, 1000)
    z = random.randint(-100, 1000)
    if x < y:
        if x < z < y:
            print(z, "is inside the range of", x, "and", y, "therefore", True)
        else:
            print(z, "is outside the range of", x, "and", y, "therefore", False)
        count += 1
    else:
        count += 1




print("""\n\n3.2: Exercises with strings
Using the Python documentation on strings (https://docs.python.org/3/library/string.html), solve the following exercises:
1. Initialize the string "abc" on a variable named "s":
(a) Use a function to get the length of the string.
(b) Write the necessary sequence of operations to transform the string "abc" in"aaabbbccc". Suggestion: Use string concatenation and string indexes.
2. Initialize the string "aaabbbccc" on a variable named "s":
(a) Use a function that allows you to find the first occurence of "b" in the string, and the first occurence of "ccc".
(b) Use a function that allows you to replace all occurences of "a" to "X", and then use the same function to change only the first occurence of "a" to "X".
3. Starting from the string "aaa bbb ccc", what sequences of operations do you need to arrive at the following strings? 
You can find the "replace" function.
(a) "AAA BBB CCC"
(b) "AAA bbb CCC\"""")

print("\n=== Answer 1 ===")
s = "abc"
print(len(s))
s = s.replace("a", "aaa")
s = s.replace("b", "bbb")
s = s.replace("c", "ccc")
print(s)

print("\n=== Answer 2 ===")
s = "aaabbbccc"
f = s.find("b")
g = s.find("c")
print("b first appears at index:", f, "| c first appears at index:", g)
# s = s.replace("a", "X")  # changes all a's to X
# print(s)
s = s.replace("a", "X", 1)  # changes all a's to X
print(s)

print("\n=== Answer 3 ===")
s = "aaa bbb ccc"
# s = s.upper()  # changes all lowercase to uppercase
# print(s)
s = s.replace("a", "A")
s = s.replace("c", "C")
print(s)




print("""\n\nChapter 3.3: Exercises with lists
Create a list named "l" with the following values ([1, 4, 9, 10, 23]). 
Using the Python documentation about lists (https://docs.python.org/3.5/tutorial/introduction.html#lists) 
solve the following exercises: 
1. Using list slicing get the sublists [4, 9] and [10, 23]. 
2. Append the value 90 to the end of the list "l". 
Check the difference between list concatenation and the "append" method. 
3. Calculate the average value of all values on the list. You can use the "sum" and"len" functions. 
4. Remove the sublist [4, 9]""")

l = [1, 4, 9, 10, 23]

print("\n=== Answer 1 ===")
print(l[1:3], "and", l[3:5])


print("\n=== Answer 2 ===")
l.append(90)
print(l)

print("\n=== Answer 3 ===")
print("The average for the l list is:", sum(l)/len(l))

print("\n=== Answer 4 ===")
l.pop(2) and l.pop(1)
print(l)

