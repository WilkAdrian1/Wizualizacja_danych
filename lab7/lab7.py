# import numpy as np

# a = np.array([20,30,40,50])
# b = np.arange(4)
#
# c = a + b
# print(c)
#
# d = b**2
# print(d)
# e = np.sqrt(a)
# print(e)
# print(e + b)
# a += b
# print(a)
#
# a =  np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
#
# a = np.array([[3, 1, 5], [6, 2, 1]])
# b = np.array([[3, 2], [5, 3], [6, 1])
# c= np.dot(a, b)
# d = a.dot(b)
# print(c)
# print(d)
#
# a = np.arange(3)
# b = np.arange(3)
# print(a.dot(b))
#
# a = np.arange(6).reshape((3, 2))
# for b in a:
#     for c in b:
#         print(c)
#
# print('')
# for b in a.flat:
#     print(b)
#
#
# a = np.arange(12).reshape((3, 4))
# print(a)
# b = a.reshape((4,3))
# print(b)
#
# print(a.ravel())
#
# c = b.T
# print(c)

import numpy as np
# zad1
# a = np.arange(0, 3)
# b = np.arange(1, 4)
# print(a)
# print(' ')
# print(b)
# print(' ')
# print(a * b)

# zad2
#
# a = np.arange(1, 10).reshape(3, 3)
# print(a)
# print("najmniejszy wiersz: ", np.amin(a, axis=0), ", najmniejsza kolumna: ", np.amin(a, axis=1))
#
# b = np.arange(1, 17).reshape(4, 4)
# print(b)
# print("najmniejszy wiersz: ", np.amin(b, axis=0), ", najmniejsza kolumna: ", np.amin(b, axis=1))

# zad3
# a = np.arange(0, 3)
# b = np.arange(1, 4)
#
# print(np.dot(a, b))

# zad4
# import math
#
# a = np.full((1, 3), 5)
# b = np.full((1, 3), math.pi)
#
# print(a)
# print(b)
# print(a * b)

# zad5

# a = np.arange(6).reshape(2, 3)
# print(a)
# print(" ")
# b = [np.sin(i) for i in a]
# print(b)

# zad6
# a = np.arange(6).reshape(2, 3)
# print(a)
# print(" ")
# b = [np.cos(i) for i in a]
# print(b)

# zad7
# a = np.arange(0, 3)
# b = np.arange(1, 4)
# print(a)
# print(" ")
# print(b)
# print(" ")
# c = a + b
# print(c)

# zad8
# a = np.arange(9).reshape(3, 3)
# for i in a:
#     print(i)

# zad9
# a = np.arange(9).reshape(3, 3)
# print(a)
# print(" ")
#
# print(a.flat[0:9])
# for i in a:
#     print(i.flat)
#
# to chyba dobrze
# a = np.arange(9).reshape(3, 3).flat
# for i in a:
#     print(i)

# zad10
# a= np.ndarray(shape=(9,9),dtype=int)
# a.fill(1)
# print(a)
# a = a.reshape(3,27)
# print(a)
# dzielnikami liczby 81

# zad11
a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
c = np.arange(12).reshape(2,6)

print(a)
print(b)
print(c)

print(a.flatten())
print(b.flatten())
print(c.flatten())