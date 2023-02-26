

def binary_search_function(sorted_array, number):
    """The binary_search_function takes a sorted array of numbers 
    and a specific number which is needed ti be found in provided array.
    If the numer is in array, function returns its index,
    in other case it returns a not found message"""

    # variables for start and end points of search - first and last elements of array
    search_start = 0
    search_end = len(sorted_array) - 1
    # the function will search while the array contains at least one number
    while search_start <= search_end:
        # the function assumes that the sought-for number is in the middle of the array
        middle = int((search_start + search_end) / 2)
        guess = sorted_array[middle]
        # if the number is in the middle of the array, function returns its index
        if guess == number:
            return f"The index of {number} is {middle}"
        # if the guess is greater or less than the sought-for number, function cuts array in half
        # and the search starts from beginning but with updated start or end point
        elif guess > number:
            search_end = middle - 1
        elif guess < number:
            search_start = middle + 1
    # if the updated search end point is greater then search start point, the search stops
    else:
        return f"Number {number} not found in the array"


array_a = [0, 7, 10, 25, 40, 51, 600, 700, 851, 999, 1000, 1100]

print(binary_search_function(array_a, 25))
print(binary_search_function(array_a, 7))
print(binary_search_function(array_a, 2))

array_b = list(range(1000, 1000000, 120))

print(binary_search_function(array_b, 2))
print(binary_search_function(array_b, 1120))
