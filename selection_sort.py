from random import randint
import time

# Selection sort is an in-place comparison sorting algorithm. 
# It has an O(n2) time complexity

def selection_sort(arr):
    for item in range(len(arr)-1):
        # assume that the item is smaller than other items after it
        minimum = item
        value_index = item + 1
        # compare current item to every item in the list after it
        while value_index < len(arr):
            # if there is a smaller item, refresh the minimim variable
            if arr[value_index] < arr[minimum]:
                minimum = value_index
            # repeat for every item in the list
            value_index += 1
        # put the smallest item to the beginning of the list
        arr[item], arr[minimum] = arr[minimum], arr[item]
        # go to the next item
    return arr


# create a list of random numbers
a = [randint(1, 99) for i in range(4)]
# print the list before and after sorting
print(f"List before sorting: {a}")
print(f"List after sorting: {selection_sort(a)}")


"""
# about O(n2) time complexity
# measure algorythm performance on a short and a long list

short_list = list(randint(1, 99) for i in range(100))
start_short = time.time()
selection_sort(short_list)
end_short = time.time()
time_for_short_list = end_short - start_short

long_list = list(randint(1, 99) for i in range(10000))
start_long = time.time()
selection_sort(long_list)
end_long = time.time()
time_for_long_list = end_long - start_long

print(f"Time for short list (100 elements): {time_for_short_list} seconds, " 
      f"time for long list (10 000 elements): {time_for_long_list} seconds")
"""
