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