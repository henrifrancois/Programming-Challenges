from math import sqrt

def fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
print((fib(35)-1)/2)
