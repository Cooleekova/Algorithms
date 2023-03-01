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
print(factorial(3))
print(factorial(5))
print(factorial(14))