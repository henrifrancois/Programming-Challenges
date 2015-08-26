
#def solution():
#    total = []
#    for n in range(0, 1000):
#        if n%3==0:
#            total.append(n)
#        elif n%5 ==0:
#            total.append(n)
#    resultat = 0
#    print(total)
#    for i in total:
#        resultat += i
#    return resultat
#print(solution())

def shorter_solution():
    total = 0
    s = [x for x in range(1,1000) if x%3==0 or x%5==0]
    for x in s:
        total += x
    return total
print(shorter_solution())
