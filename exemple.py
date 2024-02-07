nombre = [10,5,2,9,8]
print(nombre)
nombre[0] = 100
print(nombre)

#8          =>
nombre[0] = nombre[4]
print(len(nombre))
del nombre[0]

print(nombre[1]) 

print(nombre[-1]) #Permet de faire un pas a gauche et donc d'accéder au dernier index de la liste
nombre.insert(5, 44) #Permet de rajouter le nombre 44 à l'index 5
print(nombre)      
