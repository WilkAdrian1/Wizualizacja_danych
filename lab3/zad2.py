import random

lista1 = []
for i in range(10):
    lista1.append(random.randrange(1, 100))
print(lista1)

parzyste = [lista1[i] for i in range(len(lista1)) if lista1[i] % 2 == 0]
print(parzyste)