#date due liste calcolare l'intersezione

listaA = ['1', '2', '3', '4']
listaB = ['1', '10','3', '11']
listaInt = []

for x in listaA:
    if x in listaB:
        listaInt.append(x)

print(listaA)
print(listaB)
print(listaInt)