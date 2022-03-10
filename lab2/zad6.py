a = int(input("Podaj a"))
b = int(input("Podaj b"))
c = int(input("Podaj c"))

if (a >= b) & (a >= c):
    print(a)
elif (b >= a) & (b >= c):
    print(b)
else:
    print(c)