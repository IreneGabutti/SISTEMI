l1 = [1, 2, 3, 8, 4]
l2 = l1
l1.append(9999)
print(l2)

x=input("Dammi un numero: ")
print(x)

for i in range(0,9):
    if(i==2):
        continue
    print(i)