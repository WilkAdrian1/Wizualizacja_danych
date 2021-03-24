# symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
def ciag(* liczby):
    # jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        suma = liczby[0]
    # sumujemy elementy ciągu
    for i in range(1,len(liczby)):
        suma *= liczby[i]
    # zwracamy wartość sumy
    return suma

# wywołanie gdy brak argumentów
print(ciag())
# podajemy argumenty
print(ciag(1,2,3,4,5,6,7,8))