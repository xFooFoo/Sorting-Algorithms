<<<<<<< HEAD
from typing import List
import random

def insertion_sort(data: List[str]):
    n = len(data)
    print(data)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
                print(data)

# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(10)]

insertion_sort(random_numbers)
output = random_numbers
#Test whether algorithm sorts properly
if output == sorted(random_numbers):
    print("The list has been sorted.")
else:
    print(output)
=======
from typing import List
import random

def insertion_sort(data: List[str]):
    n = len(data)
    print(data)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
                print(data)

# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(10)]

insertion_sort(random_numbers)
output = random_numbers
#Test whether algorithm sorts properly
if output == sorted(random_numbers):
    print("The list has been sorted.")
else:
    print(output)
>>>>>>> 99ba043b19b937beec73e75ff2e1f8f760de5c75
    print(sorted(random_numbers))