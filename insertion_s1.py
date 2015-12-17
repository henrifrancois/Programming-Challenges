A = int(input())
s = input().strip().split()
x = [int(x) for x in s]

def sort1(x):
    u = x.pop()
    z = A-1
    if u < x[z]:
        while z > 0:
            if u < x[z]:
                x.insert(z, A)
                print(x)
                z -=1
        else:
            pass

sort1(x)
