from sys import argv

script, filename = argv

print(f"Il nome dell'esercizio è: {script}")
print("\n") #per andare a capo

#apro il file di testo
txt = open(filename)

print(f"Here's your file {filename}:") 

#leggo e stampo il contenuto del file di testo
print(txt.read())


#se voglio aprire un altro file di testo
"""
# print("Type the filename again:")
file_again = input("> ")  #inserisco il nome del file di testo da aprire

txt_again = open(file_again) #apro il file di testo
print(txt_again.read()) #leggo e stampo il contenuto del file di testo
"""
#chiudo entrambi i file di testo
txt.close()
#txt_again.close()

print(f"Il file {filename} è stato chiuso")
#print(f"Il file {file_again} è stato chiuso")

"""se commento le righe dalla 17 alla 23, lui apre il primo file, lo legge, lo stampa e lo richiude. L'esercizio finisce così"""
