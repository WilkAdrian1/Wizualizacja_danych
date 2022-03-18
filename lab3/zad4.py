def trojkat(a, b, c):
    if a ** 2 & b ** 2 == c ** 2:
        return "jest prostokątny"
    else:
        return "nie jest prostokątny"


print(trojkat(1, 1, 1))
print(trojkat(1, 2, 1))

