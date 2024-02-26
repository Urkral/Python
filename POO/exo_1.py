class Snake():
    def __init__(self, lenth: int, color: str, speed: int, isVenomous: bool):
        self.lenth = lenth
        self.color = color
        self.speed = speed
        self.isVenomous = isVenomous
    
    def displayInfo(self):
        print("Longueur : ", self.lenth, 
              "Couleur : ", self.color,
              "Vitesse : ", self.speed,
              "Venimeux : ", self.isVenomous)
    
    def moove(self, direction: str):
        print("Le serpent se déplace vers: ", direction)
    
    def eat(self):
        print("Le serpent a mangé")
    
snake1 = Snake(lenth = 5, color = "Bleu", speed = 15, isVenomous = True)

snake1.displayInfo()