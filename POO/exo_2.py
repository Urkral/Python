class Car():
    def __init__(self, color : str, speed: int, doors: str, brand: str, isOk: bool):
        self.color = color
        self.speed = speed
        self.doors = doors
        self.brand = brand      
        self.isOk = isOk

    def displayInfo(self):
        print(
            "Couleur: ", self.color,
            "Vitesse: ", self.speed, "KM/H",
            "Nombre de portes: ", self.doors,
            "Marque: ", self.brand,
            "Démarre: ", self.isOk
        )

    def goAhead(self, distance: str):
        print("La voiture à avancé de: ", distance, "KM")
        
    def start(self):
        if(self.isOk):
            print("La voiture démmare")
        else:
            print("La voiture est en panne")


car1 = Car(color = "Blanche", speed = 250, doors = 3, brand = "Ferrari", isOk = True)
car1.displayInfo()
car1.start()