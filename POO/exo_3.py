class Car:
    def __init__(self, brand: str, model: str, car_number: int, fabrication_year: int, disponible_color: list, km: int):
        self.brand = brand
        self.model = model
        self.car_number = car_number
        self.fabrication_year = fabrication_year
        self.disponible_color = disponible_color
        self.km = km

    def choose_color(self, wanted_color):
        self.wanted_color = wanted_color
        if(wanted_color not in self.disponible_color):
            print("La couleur que vous voulez n'est pas disponible")
        elif(wanted_color in self.disponible_color):
            self.disponible_color == wanted_color
            print("La couleur", wanted_color, "est bien disponible")

    def display_infos(self, wanted_km):
        print("Ma voiture est une", self.brand, "modéle", self.model, "elle à été fabriquée en", self.fabrication_year, "elle est", self.wanted_color, "et à", self.km, "kilométre")

    def drive(self):
        if self.km >= 350000:
            print("Votre voiture à atteint les", self.km, "l'obsolécense programmée vient donc de la ratrapper")
        elif self.brand.lower == "peugeot"|"renault"|"dacia":
            print("Votre voiture étant une", self.brand, self.model, "elle est donc nul à chier et ne démarre pas")
        else:
           wanted_km = input("Combien de kilométre désirez vous faire ?")
# Thinking to finish the drive methode


car1 = Car(brand = "Mercedes", model="GLS", car_number = 12, fabrication_year = 2023, disponible_color = ["verte", "bleu", "rouge", "noir"], km =0)
wanted_color = input("Quelle couleur désirez vous ?")
car1.choose_color(wanted_color)
car1.display_infos()
