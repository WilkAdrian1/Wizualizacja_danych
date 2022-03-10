lista=[]
count = 0
while count <=9:
    a = int(input("Podaj liczbe"))
    count+=1
    if a % 2 == 0 :
        lista.append(a)
print(lista)