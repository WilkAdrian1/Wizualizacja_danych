a = 10
b = 20.1



def dodawanie(a, b):
    return (a + b)

def mnozenie(a, b):
    return (a * b)

def dzielenie(a, b):
    return (a / b)

def odejmowanie(a, b):
    return (a - b)

dzialania = [
    dodawanie(a, b),
    mnozenie(a, b),
    dzielenie(a, b),
    odejmowanie(a, b)
]

for x in range(4):
    print(dzialania[x])