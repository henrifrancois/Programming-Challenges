T = int(input())

for i in range(T):

    N,C,M = map(int,input().split())
    answer = 0
    # Compute Answer
    if N > C:
        chocolates = N//C
        if M > 0:
            if chocolates >= M:
                bonus = chocolates//M
                if M == 0:
                    answer == chocolates
                elif (chocolates % M) + bonus >= M:
                    new_bonus = bonus//(chocolates % M)
                    answer = chocolates + bonus + new_bonus
                else:
                    answer = chocolates + bonus
            else:
                bonus = 0
                answer = chocolates
        else:
            answer = chocolates
    else:
        answer = 0
    print(answer)
