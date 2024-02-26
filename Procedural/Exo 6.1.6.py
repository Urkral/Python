list = [1,2,3,4,5]

newNumber = int(input("Veillez entre un nombre entier"))
newIndex = int(input("Veillez sélectionner l'indice de l'index à remplacer"))
list[newIndex] = newNumber
print(list)
del list[-1]
print(list)
print(len(list))