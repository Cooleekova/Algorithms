# recursion is a method of solving a computational problem 
# where the solution depends on solutions to smaller instances of the same problem


"""Example of recursive factorial function"""

# Factorial of a positive integer is defined 
# as the product of that number with every whole number less than or equal to 'n' till 1.
def factorial(n: int) -> int:
    if n == 1:
        return 1
    elif n <= 0:
        return "Number must be greater than zero"
    else:
        return n * factorial(n-1)


# have fun and find some factorials
print("Factorial function results:")
print(factorial(3))
print(factorial(5))
print(factorial(14))



"""Recursive function for the Fibonacci sequence """


#  the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
def fibonacci(index):
    """Return the number of the Fibonacci sequence corresponding to the entered index"""
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)


print("\nFibonacci function results:")
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(13))


"""Recursive palindrome check function """

# A palindrome is a word, number, phrase, 
# or other sequence of symbols that reads the same backwards as forwards
# including an emty sequence and a sequence with only one element 

def palindrome(sequence):
    """Check if the sequence's first and last elements are equal,
    if so, check the second pair of elements and so on
    until there is only one middle element or no elements at all left"""
    if len(sequence) <= 1:
        return (f"Yes, the sequense is a palindrome", True)
    elif sequence[0] != sequence[-1]:
        return (f"No, the sequense is NOT a palindrome", False)
    return palindrome(sequence[1:-1])


# have fun and check some palindromes]
print("\nPalindrome function results:")
print(palindrome("1221"))
print(palindrome("saippuakivikauppias"))
print(palindrome("123456")[1])


"""Some more examples of recursive functions"""


def greatest_number(arr):
    """Find the greatest number in a given array"""
    if len(arr) == 1:
        return arr[0]
    else:
        greatest = greatest_number(arr[1:])
        if arr[0] > greatest:
            return arr[0]
        return greatest


# have fun and find some maximums
print("\nGreatest number function results:")
print(greatest_number([9,2,3]))
print(greatest_number([1]))
print(greatest_number([1,2,100]))
print(greatest_number([1,10,2,3]))


def sum_of_all_elements(arr):
    """Find a sum of all the elements in a given array"""
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_of_all_elements(arr[1:])
    

# have fun and find some totals
print("\nSum function results:")
print(sum_of_all_elements([1, 1, 1]))
print(sum_of_all_elements([100, 100, 100]))


def count_elements(arr):
    """Find the length of a given array"""
    count = 0
    if len(arr) == 1:
        return 1
    else:
        count = count_elements(arr[0:1]) + count_elements(arr[1:])
    return count

# have fun and find a length
a = list(range(900))
print(f"Length of the list: {count_elements(a)}")


# recursive implementation of binary search function
def binary_search_recursive_function(sorted_array, number, search_start=0, search_end=None):
    """The binary_search_function takes a sorted array of numbers 
    and a specific number which is needed to be found in provided array.
    If the numer is in array, function returns its index,
    in other case it returns a not found message"""
    if search_end is None:
        search_end = len(sorted_array) - 1
    if search_start > search_end:
        return f"{number} is not in the list"
    middle = int((search_start + search_end) // 2)
    if number == sorted_array[middle]:
        return f"The index of {number} is {middle}"
    elif number < sorted_array[middle]:
        return binary_search_recursive_function(sorted_array, number, search_start, middle - 1)
    elif number > sorted_array[middle]:
        return binary_search_recursive_function(sorted_array, number, middle + 1, search_end)


# have fun and do binary search
d = list(range(1, 100000))
print(f"Binary search found out that: {binary_search_recursive_function(d, 999)}")
