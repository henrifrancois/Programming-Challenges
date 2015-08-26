T = int(input())
for testcase in range(0, T):
    N = int(input())
    N_string = str(N)
    for number in N_string:
        if int(number) == 0:
            pass
        if int(number) != 0:
            x = []
            for number in N_string:
                if number != "0" and N % int(number) == 0:
                    x.append(number)
    print(len(x))
