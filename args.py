def somme(*args):
  total = 0
  for argument in args:
    total += argument
  return total

print(somme(1,2,3,4,5,6))
