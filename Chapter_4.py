import random
import math

print("""\n\n4.1: Exercises with the math module
Use the python documentation about the math module (https://docs.python.org/3/library/math.html)
to solve the following exercises:
1. Find the greatest common divisor of the following pairs of numbers: (15, 21), (152,200), (1988, 9765).
2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.
3. Use the "input" function to ask the user for a number and show the result of the sine, cosine and tangent
of the number. 
Make sure that you convert the user input
from string to a number (use the int() or the float() function).""")

print("""\n=== Answer 1 ===""")
print("GCD of 15, 21 is", math.gcd(15, 21))
print("GCD of 152, 200 is", math.gcd(152, 200))
print("GCD of 1988, 9765 is", math.gcd(1988, 9765))

print("""\n=== Answer 2 ===""")
num = [1, 2, 6, 9, 15]  # I removed 0 because it causes a math domain error

for n in num:
    print(math.log2(n))

print("""\n=== Answer 3 ===""")
# num = float(input("Please enter a number to convert to sine, cosine and tangent: "))
num = random.randint(-360, 360)
print("Sine of", num, "is", math.sin(num))
print("Coine of", num, "is", math.cos(num))
print("Tangent of", num, "is", math.tan(num))

print("""\n\n4.2: Exercises with functions
1. Implement the "add2" function that receives two numbers as arguments and returns the sum of the numbers. 
Then implement the "add3" function that receives and sums 3 parameters.
2. Implement a function that returns the greatest of two numbers given as parameters.
Use the "if" statement to compare both numbers: https://docs.python.org/3/tutorial/controlflow.html#if-statements.
3. Implement a function named "is_divisable" that receives two parameters (named "a" and "b") 
and returns true if "a" can be divided by "b" or false otherwise. 
A number is divisable by another when the remainder of the division is zero. 
Use the modulo operator ("%").
4. Create a function named "average" that computes the average value of a list passed as parameter to the function. 
Use the "sum" and "len" functions.""")

print("""\n=== Answer 1 ===""")


def add_2(val1, val2):
    print("Function got value", val1, "and", val2)
    return val1 + val2


def add_3(val1, val2, val3):
    print("Function got value", str(val1) + ",", val2, "and", val3)
    return val1 + val2 + val3


n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)

print(add_2(n1, n2))
print(add_3(n1, n2, n3))

print("""\n=== Answer 2 ===""")


def great(val1, val2):
    print("Received", val1, "and", val2)
    if val1 > val2:
        return val1
    else:
        return val2

n1 = random.randint(0, 10)
n2 = random.randint(0, 10)

print(great(n1, n2))

print("""\n=== Answer 3 ===""")


def is_divisible(a, b):
    if a%b == 0:
        return True
    else:
        return False


n1 = random.randint(0, 10)
n2 = random.randint(0, 10)

print("Can " + str(n1) + " / " + str(n2) + " equally?", is_divisible(n1, n2))

print("""\n=== Answer 4 ===""")


def get_average(val):
    return sum(val)/len(val)

count = 0
l = []
while count < 10:
    l.append(random.randint(0, 1000))
    count += 1
print("List:", l)

print("Average:", get_average(l))

print("""\n\n4.4: Exercises with recursive functions
1. Implement the factorial function and test it with several different values. 
Cross-check with a calculator.
2. Implement a recursive function to compute the sum of then first integer numbers(wheren is a function parameter). 
Start by thinking about the base case (the sum of the first 0 integers is?) and then think about the recursive case.
3. The Fibonnaci sequence is a sequence of numbers in which each number of the sequence matches 
the sum of the previous two terms. 
Given the following recursive definition implement fib(n).
*See PDF for fib(n) image
Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89, ...""")


print("""\n=== Answer 1 ===""")
count = 1
while count != 11:
    x = random.randint(0, 15)
    print("Test " + str(count) + " for number " + str(x) + ":", math.factorial(x))
    count += 1

print("""\n=== Answer 2 ===""")

print("""\n=== Answer 3 ===""")