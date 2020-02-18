"""
dato in input la lunghezza della lista e la lunghezza delle parole desiderate, 
il programma fa rimepire la lista e dopodiche
stampera la nuova lista con le parole di lunghezza = o > di quella inserita dall'utente
"""


lista = []
lista1 = []
dim = input("Quante parole vuoi inserire nella lista?")
lungh = input("Lunghezza parole desiderata: ")


for i in range (0,int(dim)):
    parola = input("Parola: ")
    lista.append(parola)
    
for parola in lista:
    if(len(parola)>=int(lungh)):
        lista1.append(parola)

print(lista)
print(lista1)

"""
for i in range (0,int(dim)):
    parola = input("Parola: ")
    lista.append(parola)
    if(len(parola)>=int(lungh)):
        lista1.append(parola)

print(lista)
print(lista1)
"""