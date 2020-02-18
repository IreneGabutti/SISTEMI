#scrivere un programma che riempa una lista arbitraria chiedendo i valori degli elementi all'utente

lista = []
numIns = input("Quanti elementi vuoi inserire nella lista?")
for i in range (0,int(numIns)):
    valoreIns = input("Valore da inserire: ")
    lista.append(valoreIns)

print(lista)
lista.sort()
print(lista)

