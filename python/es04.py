#enumerate e librerie

import random       #importazione di una libreria


listaNomi = ['Mario Rossi', 'John Doe', 'Tizio Caio']


#enumerate serve per far ritornare sia la posizione, sia l'elemento contenuto in tale posizione
for num, student in enumerate(listaNomi):
    print(f"{num} - {student}")


print(f"Viene interrogato: {listaNomi[random.randint(0,len(listaNomi)-1)]}")
