#esercizio Stringhe dispense
#PUNTO 2: i punti in cui viene inserita una stringa all'interno di una stringa sono 4


types_of_people = 10    #viene inizializzata una nuova variabile

#in x viene inserita la stringa
#metto la f davanti poichè uso un tipo speciale di stringa per "formattare"
x = f"There are {types_of_people} types of people."  

#vengono inserite delle stringhe all'interno di queste due variabili
binary = "binary"   
do_not = "don't"
#stessa questione di prima
y = f"Those who know {binary} and those who {do_not}."

#stampo le due variabili contenente due stringhe
print(x)
print(y)

#faccio una stampa utilizzando anche il procedimento per il tipo speciale di stringa
print(f"I said: {x}")
print(f"I also said: '{y}'")

#equivale alla procedura in alto per salvare una stringa e concatenargli altre stringhe/valori
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
#       |
#       |
#      \ /
#equivale a questo
"""
hilarious = False
joke_evaluation = f"Isn't that joke so funny?!{hilarious}
print(joke_evaluation)
"""

#inserisco due stringhe all'interno di due variabili
w = "This is the left side of..."
e = "a string with a right side."

#PUNTO 4: concateno le due stringhe con l'operatore +
print(w + e)