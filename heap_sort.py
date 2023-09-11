"""
given input list, put list into a tree (heap).
Now create a max heap where parent node > child
Once sorted (1 run), swap first and last node and then delete the now-last node (aka largest element found and placed in order at the end so no
need to check that position anymore
Only one element left in heap = sorted array

Can create the heap using an array representation
"""
from typing import List
import random

def Heapsort(data):
    n = len(data)
    #creates max heap from the heap
    for i in range(n//2 - 1, -1, -1):
        Heapify(data, n, i) 
    #Then we can order the max element and move it to the end and repeat the heapify step
    for lastIndex in range(n - 1, 0, -1):
        data[0], data[lastIndex] = data[lastIndex], data[0]
        #calls heapfiy on the shortened data (index is one less of array length n)
        Heapify(data, lastIndex, 0)

def Heapify(data, n: int, i: int):
    print(data)
    largestChild = i
    leftChild = 2 * i + 1
    rightChild = leftChild + 1
    if n > leftChild and data[leftChild] > data[largestChild]:
        largestChild = leftChild
    if n > rightChild and data[rightChild] > data[largestChild]:
        largestChild = rightChild
    #case where we need to swap, if it's not the same node and is larger or equal
    if i != largestChild:
        data[i], data[largestChild] = data[largestChild], data[i]
        print(data)
        #Ensures the max heap characteristic is in place after the swap 
        Heapify(data, n, largestChild)
        print(data)


# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]
original  = random_numbers
Heapsort(random_numbers)
#Test whether algorithm sorts properly
if random_numbers == sorted(original):
    print(random_numbers)
    print("The list has been sorted.")
else:
    print("The list has NOT been sorted.")
    print(random_numbers)
    #print(sorted(theory))
        
    