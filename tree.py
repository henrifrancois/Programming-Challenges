T = int(input())
for testcase in range(0, T):
    N = abs(int(input()))
    H = 1
    while N > 0:
        if N % 2 == 0:
            H = H*2
            N -= 1
            if N % 2 == 1:
                H = H+1
                N -= 1
        elif N % 2 == 1:
            H = H*2
            N -= 1
            if N % 2 == 0 and N > 0:
                H = H+1
                N -= 1
            elif N == 0:
                H = H
            elif N % 2 == 1:
                H == H+1
    print(H)
