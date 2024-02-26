class Etudiants:
    def __init__(self):
        #Les 2 underscore permettes de rendre l'attribut privé
        self.__maVariable = 55

    def affichage(self):
        self.__maVariable = 5
        print('var = ' , self.__maVariable)

    #Asseceur (getter)
    @property
    def maVariable(self):
        return self.__maVariable

    #Mutateur (setter)
    @maVariable.setter
    def maVariable(self, value):
        self.__maVariable = value


# Instance monObj, instancié de la classe Etudiants
monObj = Etudiants()
monObj.affichage()

#2 objets qui ont le même attributs, mais qui ne partagent rien
monObj2 = Etudiants()
monObj2.affichage()

