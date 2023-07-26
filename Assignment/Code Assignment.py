# Question 1
string_variable = "Hello, Anuj"
list_variable = [1, 2, 3, 4, 5]
float_variable = 89.3
tuple_variable = (10, 20, 30)



#Question 3
a = 10
b = 2
result = a / b
print(result)  # Output will be 5.0

a = 10
b = 3
result = a % b
print(result)  # Output will be 1

a = 10
b = 3
result = a // b
print(result)  # Output will be 3

base = 2
exponent = 3
result = base ** exponent
print(result)  # Output will be 8



# Question 4

# Create a list with 10 elements of different data types
my_list = [10, "Hello", 3.14, True, [1, 2, 3], (1, 2), {"name": "John", "age": 30}, None, "Python", False]

# Using a for loop to print each element and its data type
for element in my_list:
    print(f"Element: {element}, Data Type: {type(element)}")



#Question 5

def find_divisions(a, b):
    count = 0
    while a >= b and a % b == 0:
        a = a // b
        count += 1
    return count

# Test example
number_a = 100
number_b = 5

result = find_divisions(number_a, number_b)
print(f"{number_a} is purely divisible by {number_b} and can be divided {result} times.")



#Question 6

# Create a list containing 25 integer type data
my_list = [2, 15, 7, 9, 36, 10, 27, 14, 21, 16, 3, 19]

# Using for loop and if-else condition to check divisibility by 3
for num in my_list:
    if num % 3 == 0:
        print(f"{num} is divisible by 3.")
    else:
        print(f"{num} is not divisible by 3.")



#Question 7

# Lists are mutable
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]

# Modifying the list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]



# Strings are immutable
my_string = "Hello"
print(my_string)  # Output: Hello

# Trying to modify the string (Error: strings are immutable)
my_string[0] = "h"  # TypeError: 'str' object does not support item assignment
