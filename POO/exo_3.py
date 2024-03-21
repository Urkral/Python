class Car:
    def __init__(self, _brand: str, _model: str, _car_number: int, _fabrication_year: int, _disponible_color: list, _km: int):
        self._brand = _brand
        self._model = _model
        self._car_number = _car_number
        self._fabrication_year = _fabrication_year
        self._disponible_color = _disponible_color
        self._km = _km

    def _choose_color(self, wanted_color):
        self.wanted_color = wanted_color
        if(wanted_color not in self._disponible_color):
            print("La couleur que vous voulez n'est pas disponible")
        elif(wanted_color in self._disponible_color):
            self._disponible_color == wanted_color
            print("La couleur", wanted_color, "est bien disponible")

    def _display_infos(self):
        print("Ma voiture est une", self._brand, "modéle", self._model, "elle à été fabriquée en", self._fabrication_year, "elle est", self.wanted_color, "et à", self._km, "kilométre")

    def _drive(self,wanted_km):
        self.wanted_km = wanted_km
        if self._km >= 350000:
            print("Votre voiture à atteint les", self._km, "l'obsolécense programmée vient donc de la ratrapper")
        elif self._brand.lower == "peugeot" :
            print("Votre voiture étant une", self._brand, self._model, "elle est donc nul à chier et ne démarre pas")
        else:
            self._km += wanted_km
        return self.wanted_km

            


car1 = Car(_brand = "Mercedes", _model="GLS", _car_number = 12, _fabrication_year = 2023, _disponible_color = ["verte", "bleu", "rouge", "noir"], _km =0)
wanted_color = input("Quelle couleur désirez vous ?")
wanted_km = int(input("Combien de kilométre désirez vous faire ?"))

car1._drive(wanted_km)
car1._choose_color(wanted_color)
car1._display_infos()
