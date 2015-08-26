def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def challenge():
    fibonnaci = list(fib2(4000000))
    print(fibonnaci)
    evens = [value for value in fibonnaci if value % 2 == 0]
    total = 0
    for number in evens:
        total += number
    return total
