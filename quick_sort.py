"""
This function takes in a list of integers and the index of the first/last element as low/high and returns
the list sorted in N*Log(N) time due to recursively sorting the original list as two sub arrays.
"""

from typing import List
import random

def quicksort(data: List[int], low: int, high: int):
    print(f"data {data}, low {low}, high {high}")
    if low >= high:
        return
    left = low
    right = high
    medianIndex = (high + low)//2
    pivot = data[medianIndex]
    print(f"pivot {pivot}")
    #place pivot to the last position
    data[medianIndex] = data[high]
    data[high] = pivot
    right -= 1
    
    print(f"Move pivot to end {data}")
    while (left <= right):
        if data[left] > pivot:
            if data[right] <= pivot: #moves the right index to the left even on same value to action the swap. This causes quicksort to be unstable.
                temp = data[left]
                print(f"Found {data}, left {left}, right {right}")
                data[left] = data[right] 
                data[right] = temp
                left += 1
                right -= 1
                print(f"Swap {data}, left {left}, right {right}")
            else:
                right -= 1
        else:
            left += 1
    #Final swap to put pivot in its correct pos
    data[high] = data[left]
    data[left] = pivot
    print(f"Pivot back {data}, left {left}, right {right}")
    
    
    quicksort(data, low, left - 1)
    quicksort(data, left + 1, high)
    

# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(100)]
theory  = random_numbers
quicksort(random_numbers, 0, 99)
output = random_numbers
#Test whether algorithm sorts properly
if output == sorted(theory):
    print("The list has been sorted.")
else:
    print(output)
    #print(sorted(theory))
        
        