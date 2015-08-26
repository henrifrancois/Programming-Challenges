def big_factorial(n):
    counter = 1
    while n>1 :
        counter = n*counter
        n -= 1
    return counter

print(big_factorial(3))
