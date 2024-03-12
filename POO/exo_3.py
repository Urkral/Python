class Car:
    def __init__(self, brand: str, model: str, car_number: int, fabrication_year: int, color: str, disponible_color: list, km: int):
        self.brand = brand
        self.model = model
        self.car_number = car_number
        self.fabrication_year = fabrication_year
        self.color = color
        self.disponible_color = disponible_color
        self.km = km

    def change_color(wanted_color, color, disponible_color):
        color = wanted_color
        if color not in disponible_color:
            print("La couleur que vous voulez n'est pas disponible")
        elif color in disponible_color:
            disponible_color == color

    def display_infos(brand, model, fabrication_year, color, km):
        print("Ma voiture est une", brand, "modéle", model, "elle à été fabriquée en", fabrication_year, "elle est", color, "et à", km, "kilométre")




    wanted_color = input("Quelle couleur désirez vous ?")