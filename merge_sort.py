#python doesn't use pointers, only references. Must return the results to data.
from typing import List
import random

def mergesort(data: List[int]):
    n = len(data)
    if n <= 1: #base case if length of array is less than/equal to 
        return data
    medianIndex = n//2
    #keeps splitting then eventually becomes a single element 
    leftArray = mergesort(data[:medianIndex])
    rightArray = mergesort(data[medianIndex:])
    print(leftArray)
    print(rightArray)
    #starts merging L&R together once everything's split up
    return merge(leftArray,rightArray)
    

def merge(leftArray: List[int], rightArray: List[int]):
    #compare left most from each data and put in new list
    mergedArray = []
    l, r = 0, 0 #index for left/right 
    while (l < len(leftArray) and r < len(rightArray)):
        if leftArray[l] < rightArray[r]:
            mergedArray.append(leftArray[l])
            l += 1
        else: #covers case where both values are the same
            mergedArray.append(rightArray[r])
            r += 1
    
    while (l < len(leftArray)):
        mergedArray.append(leftArray[l])
        l += 1
    while (r < len(rightArray)):
        mergedArray.append(rightArray[r])
        r += 1
    return mergedArray
        
# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)
original  = random_numbers
output = mergesort(random_numbers)
#Test whether algorithm sorts properly
if output == sorted(original):
    print(output)
    print("The list has been sorted.")
else:
    print("The list has NOT been sorted.")
    print(output)
    #print(sorted(theory))