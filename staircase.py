def staircase(n, character):
    counter = 1
    character = str(character)
    while counter != n:
        print((character*counter).rjust(n))
        counter += 1


def staircase2(n, character):
    for x in range(1, n+1):
        print((str(character)*x).rjust(n))
    return n

print(staircase2(6, "#"))
