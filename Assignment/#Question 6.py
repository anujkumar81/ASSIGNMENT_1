#Question 6

# Create a list containing 25 integer type data
my_list = [2, 15, 7, 9, 36, 10, 27, 14, 21, 16, 3, 19]

# Using for loop and if-else condition to check divisibility by 3
for num in my_list:
    if num % 3 == 0:
        print(f"{num} is divisible by 3.")
    else:
        print(f"{num} is not divisible by 3.")
