# Quicksort is an efficient, general-purpose sorting algorithm. 
# Quicksort is a divide-and-conquer algorithm. 
# It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, 
# according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort.
# The sub-arrays are then sorted recursively. 
# This can be done in-place, requiring small additional amounts of memory to perform the sorting.
# https://stackoverflow.com/questions/65724771/python-how-to-implement-quick-sort-when-middle-element-is-the-pivot
from random import randint


def qsort(arr):
    """Select a 'pivot' element from the array and partition the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot. Return sorted array"""
    # in the simplest case when array is empty (length=0)
    # or contains only one item (length=1) there is no need to do sorting
    if len(arr) < 2:
        return arr
    # If the data are randomly distributed, 
    # selecting the first data point as the pivot is equivalent to a random selection.
    else:
        pivot = arr[0]
        less = [number for number in arr[1:] if number <= pivot]
        greater = [number for number in arr[1:] if number > pivot]
        return qsort(less) + [pivot] + qsort(greater)


# have fun and use one of the fastest sorting algorithms
# create a list of random numbers
a = [randint(1,99) for i in range(1, 21)]
# print the list before and after sorting
print(f"List before sorting: {a}")
print(f"List after sorting: {qsort(a)}")
