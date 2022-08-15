'''

    A recursive function is one that calls itself within the function. This
    concept is quite hard to grasp and will take some time to fully understand.

    A good example to understand this would be considering a sum of all numbers
    from one to n. There are two ways to approach this:

    1. f(n) = 1 + 2 + 3 + ... + n

    2. f(n) = 1                n = 1
       f(n) = n + f(n - 1)     n > 1

'''

def factorial(n):
    """ Simple factorial function using recursion"""

    # This is a necessary base case or else we would be stuck in an infinite loop
    if n <= 1:
        return 1

    else:
        return n * factorial(n-1) # Here the function is calling itself

print(factorial(9))
print(factorial(1))
