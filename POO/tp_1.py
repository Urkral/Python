class Monster:
    def __init__(self, breed: str, sub_breed: str, name: str, age: int, isDangerous: bool):
        self.breed = breed
        self.sub_breed = sub_breed
        self.name = name
        self.age = age
        self.isDangerous = isDangerous

    def displayInfo(self):
        print(
            "Race: ", self.breed,
            "Type: ", self.sub_breed,
            "Nom: ", self.name,
            "Age: ", self.age, "ans",
            "Dangereux: ", self.isDangerous,
        )

    def gettingOld(self):
        self.age += 1
        if(self.age >= 100):
            print("T'es mort")


    def becomeDangerous(self):
        if(self.isDangerous == False):
            self.isDangerous = True
        elif(self.isDangerous == True):
            print("Votre monstre est déjà dangereux")



monster1 = Monster(breed = "Ange", sub_breed = "Déchu", name = "Golorackus", age = 98, isDangerous = True)
monster1.gettingOld()
monster1.becomeDangerous()
monster1.displayInfo()
        