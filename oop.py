'''class Auto():
    raeder = 4
    
    def __init__(self,marke,farbe,jahr,modell,tueren):
        self.marke = marke
        self.farbe = farbe
        self.jahr = jahr
        self.modell = modell
        self.tueren = tueren
    
    def info(self):
        print('Dein Auto hat folgende Werte : ')
        print('Marke :',self.marke)
        print('Farbe :',self.farbe)
        print('Jahr :',self.jahr)
        print('Modell :',self.modell)
        print('Tueren :',self.tueren)

    def begruessung(self):
        print('Hallo Lieber, ich bin', self.marke)


class Sportwagen(Auto): #Vererbung
    def __init__(self, marke, farbe, jahr, modell, tueren,folierung,auspuff):
        super().__init__(marke, farbe, jahr, modell, tueren)   #Eltern Eigenschaften zugreifen 
        self.folierung = folierung
        self.auspuff = auspuff
    
    def turbo(self):
        print('Turbo wird aktiviert!')

auto1 = Auto(marke='Volkswagen',farbe='schwarz',jahr=2020,modell='Virtus',tueren=4)
auto2 = Auto(marke='Audi',farbe='dunkelgruen',jahr=2022,modell='R8',tueren=4)
auto3 = Auto(marke='Mercedez',farbe='weiss',jahr=2023,modell='Benz',tueren=4)

print(auto1.farbe)
auto2.begruessung()

sw1 = Sportwagen(marke='BMW',farbe='Blau',jahr=2024,modell='M4',tueren=2,folierung='Matt',auspuff=2)
sw1.begruessung()'''