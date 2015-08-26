from math import sqrt

T = int(input())
for testcase in range(0, T):
    A_input, B_input = input().strip().split()
    A, B = int(A_input), int(B_input)
    Ar, Br = int(sqrt(A)), int(sqrt(B))
    squares = []
    for value in range(Ar, Br+1):
        if value**2 in range(A, B+1):
            squares.append(value)
    print(len(squares))
