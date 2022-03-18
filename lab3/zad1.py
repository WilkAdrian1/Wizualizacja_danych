a = [ 1 -x for x in  range(1, 11)]
print(a)
b = [ 4**y for y in range(8)]
print(b)

c = [x for x in b if x % 2 == 0]
print(c)