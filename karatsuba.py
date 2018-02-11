# def bitStr(n, s):
#     if n == 1:
#         return s
#     return [digits + bits for digits in bitStr(1, s) for bits in bitStr(n - 1, s)]

# print(bitStr(3, 'abc'))

from math import ceil
from math import log10
from timeit import default_timer

def karatsuba(x, y):
    # The base case for recursion
    if x < 10 or y < 10:
        return x*y

    #sets n, the number of digits in the highest input number
    n = max(int(log10(x)+1), int(log10(y)+1))

    # rounds up n/2
    n_2 = int(ceil(n / 2.0))

    #adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1

    #splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)

    #applies the three recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd

    #performs the multiplication
    return ((10**n)*ac) + bd + ((10**n_2)*(ad_bc))

starttime = default_timer()
print(karatsuba(1234, 35235))
endtime = default_timer()
print('Computation time: ' + str(endtime - starttime))

starttime = default_timer()
print(1234 * 35235)
endtime = default_timer()
print('Computation time: ' + str(endtime - starttime))
