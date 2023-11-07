from typing import List
import random

def selection_sort(data: List[int]):
    n = len(data)
    print(data)
    for i in range(1,n):
        min_tup = (i-1,data[i-1]) #key,val in a tuple
        for j in range(i,n): #last iteration n to n ignored since it must be the largest left over in the last position
            if data[j] < min_tup[1]:
                min_tup = (j, data[j]) #minimum value in unsorted position
        data[min_tup[0]], data[i-1] = data[i-1] ,min_tup[1] #swap value of the ith position with the minimum value
        print(data)


# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]

selection_sort(random_numbers)
output = random_numbers
#Test whether algorithm sorts properly
if output == sorted(random_numbers):
    print("The list has been sorted.")
else:
    print(output)
    print(sorted(random_numbers))
        
    