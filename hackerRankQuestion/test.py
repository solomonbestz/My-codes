
# ITERATION METHOD
from ctypes import sizeof


def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

# RECURSION METHOD
def recurse_sum(n):
    if n == 1:
        return 1
    return n + recurse_sum(n - 1)

# FIBONACCI SERIES FUNCTION IN RECURSION
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n - 2)


if __name__ == "__main__":
    # sum = 0
    # previous = 0
    # next = 1
    # print(previous, next, end=" ")
    # for n in range(10):
    #     sum = previous + next
    #     previous = next
    #     next = sum
    #     print(sum, end=" ") 
    pass
    

   