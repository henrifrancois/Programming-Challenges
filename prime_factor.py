#600851475143

def largest_primef(value):
    diviseur = 2
    while (value>diviseur):
        if value % diviseur == 0:
            value = value/diviseur
            print(value)
            diviseur = 2
        else:
            diviseur += 1;
        print(value)

print (largest_primef(600851475143))
