class Human:
    def __init__(self, name: str, first_name: str, born_year: int, children: list):
        self.name = name
        self.first_name = first_name
        self.born_year = born_year
        self.children = children

    def calculate_age(self):
        age = 2024 - self.born_year
        print("Vous avez: ", age, 'ans')
        return age
    
    def presentation(self):
        age = self.calculate_age()
        print(
            "Bonjour, mon prénom est", self.first_name, "mon nom de famille est", self.name, "j'ai", age , "ans et je suis né en", self.born_year
        )

    def reconaze_children(self,child):
        if(child in self.children):
            print("C'est votre enfant")
        else:
            print("Ce n'est pas l'un de vos enfant")

human1 = Human(name = "Potté", first_name = "Henry", born_year = 1988, children = ["Timmy", "Jaque", "Pastis"])
child = input("Donnez le nom de votre enfant: ")
human1.calculate_age()
human1.presentation()
human1.reconaze_children(child)