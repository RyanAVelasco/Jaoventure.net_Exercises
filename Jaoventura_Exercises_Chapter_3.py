print("All exercises here can be found at: http://joaoventura.net/static/files/python_exercises_book.pdf")





print("""\nChapter 3.3: Exercises with lists
Create a list named "l" with the following values ([1, 4, 9, 10, 23]). 
Using the Python documentation about lists (https://docs.python.org/3.5/tutorial/introduction.html#lists) 
solve the following exercises: 
1. Using list slicing get the sublists [4, 9] and [10, 23]. 
2. Append the value 90 to the end of the list "l". 
Check the difference between list concatenation and the "append" method. 
3. Calculate the average value of all values on the list. You can use the "sum" and"len" functions. 
4. Remove the sublist [4, 9]""")

l = [1, 4, 9, 10, 23]

print("\n=== Question 1 ===")
print(l[1:3], "and", l[3:5])


print("\n=== Question 2 ===")
l.append(90)
print(l)

print("\n=== Question 3 ===")
print("The average for the l list is:", sum(l)/len(l))

print("\n=== Question 4 ===")
l.pop(2) and l.pop(1)
print(l)

