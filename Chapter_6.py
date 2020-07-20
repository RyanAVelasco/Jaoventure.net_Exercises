print("""

=== 6.1 Exercises with dictionaries ===
Use the python documentation at https://docs.python.org/3/library/stdtypes. 
html#mapping-types-dict to solve the following exercises.
Take the following python dictionary:
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

1. How many students are in the dictionary? Search for the "len" function.
2. Implement a function that receives the "ages" dictionary as parameter and return
the average age of the students. Traverse all items on the dictionary using the
"items" method as above.
3. Implement a function that receives the "ages" dictionary as parameter and returns
the name of the oldest student.
4. Implement a function that receives the "ages" dictionary and a number "n" and
returns a new dict where each student is n years older. 
For instance, new_ages(ages, 10) returns a copy of "ages" where each student is 10 years older.""")

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

print("""
=== Answer 1 ===""")
print("There are:", len(ages), "students.")

print("""
=== Answer 2 ===""")


def average_age(students):
    add = []
    for name, age in students.items():
        add.append(age)

    print("The average age of the students:", sum(add)/len(add))


average_age(ages)

print("""
=== Answer 3 ===""")


def oldest_student(students):
    oldest = 0
    for name, age in students.items():
        if age > oldest:
            oldest = age

    for name, age in students.items():
        if age == oldest:
            return name

print(oldest_student(ages))


print("""
=== Answer 4 ===
The question wasn't clear enough so I assume that '..each student is 10 years older.' means a new
dictionary containing all students above n age.""")


def generate_dict(students, x):
    older_students = {}
    for name, age in students.items():
        if age > x:
            older_students[name] = age
    return older_students


# n = int(input("Please enter a number: "))
n = 10
print(generate_dict(ages, n))

print("""

=== 6.2: Exercises with sub-dictionaries ===
Take the following dictionary:
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

1. How many students are in the "students" dict? Use the appropriate function.
2. Implement a function that receives the students dict and returns the average age.
3. Implement a function that receives the students dict and an address, and returns
a list with the name of all students which address matches the address in the
argument. 
For instance, invoking "find_students(students, ’Lisbon’)" should return
Peter and Anna.""")

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

print("""
=== Answer 1 ===""")
print("There are:", len(students), "students.")

print("""
=== Answer 2 ===""")


def get_average_age(dict):
    tally = []
    for name in dict:
        tally.append(dict[name]["age"])
    return "The average age is: " + str(sum(tally)//len(tally))


print(get_average_age(students))


print("""
=== Answer 3 ===""")
def find_students(student, area):
    log = []
    for name, key in student.items():
        if area in key["address"]:
            log.append(name)
        else:
            continue
    return log


address = input("What area? ").title()
print(find_students(students, address))