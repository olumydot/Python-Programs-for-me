"""This program returns the sum of the first n fibonacci numbers"""


# catch_values = {}
#
#
# def fibonumber(n):
#     # check if value has been computed before
#     if n in catch_values:
#         return catch_values[n]
#
#     # compute the nth fib term
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         returned_value = fibonumber(n-1) + fibonumber(n-2) # return the sum of the previous 2 terms
#
#     # store the returned value in the catch and return it
#     catch_values[n] = returned_value
#     return returned_value
#
#
# m = eval(input("input an integer value  "))
# for n in range(1,m+1):
#     print(n, ":", fibonumber(n))
#


# # I can rewrite the same code using a functool library

from functools import lru_cache


# lru is least recently used
@lru_cache(maxsize=50000)
def fibonumber(n):
    # compute the nth fib term
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        returned_value = fibonumber(n - 1) + fibonumber(n - 2)  # return the sum of the previous 2 terms
        return returned_value


m = eval(input("input an integer value  "))
for n in range(1, m+1):
    print(n, ":", fibonumber(n))
