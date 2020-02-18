#argv--> è una variabile argomento che contiene gli argomenti che passi allo script Python durante l'esecuzione di esso
#sys è un modulo (libreria)

from sys import argv

# read the WYSS section for how to run this
#è come se prendesse tutto ciò che è in argv, lo scompatta(decomprime) e lo assegna a tutte queste variabili a sinistra in ordine. 
#script si riferisce al nome del file.py

script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#quando vado ad eseguirlo devo scrivere py nomeFile.py argomento1 argomento2 argomento3
#(in questo caso tre argomenti perchè da codice ho deciso 3)

"""
#PUNTO 2 --> meno argomenti 
script, first = argv
print("The script is called:", script)
print("Your first variable is:", first)
"""

"""
#PUNTO 2 --> più argomenti
script, first, second, third, fourth = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
"""




#PUNTO 1: se fornisco meno di tre argomenti, quando lo compilo mi viene detto che non ha abbastanza argomenti per poter eseguire il programma

