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

print("\n=== Answer 1 ===")
list =[127,239,203,874,115,706,477,108,109,160]
sum = 0

def add(x):
    global sum
    
    for val in list:
        print(list, val)
        sum += val
    return "The total sum of the list is: " + str(sum)
    
    
print(add(sum))


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