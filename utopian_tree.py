T = int(input())
for testcase in range(0, T):
    N = int(input())
    H = 1
    if N == 1:
        print(H*2)
    else:
        if N % 2 == 0:
            while N > 0:
                H = H*2
                H = H+1
                N -= 2
                if N == 0:
                    H = H
            print(H)
        elif N % 2 == 1:
            while N >= 2:
                H = H*2
                H = H+1
                N -= 1
            H = H-1
            print(H)
