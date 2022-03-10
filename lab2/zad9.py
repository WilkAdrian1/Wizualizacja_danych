import math

x = (input("Podaj x aby obliczyc sqrt(x)"))

try:
        wynik = math.sqrt(int(x))
        print(wynik)
except ValueError:
        print("Podano ujemny x")