import math

numbers_input = input("Type The Number (separated by commas) or one number:  ")
x = [int(num) for num in numbers_input.split(",")]

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for num in x:
    if isprime(num):
        print(f"This Number is Prime: {num}")
    else:
        print(f"This Number is not Prime: {num}.")
