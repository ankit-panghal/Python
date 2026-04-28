'''from dataclasses import dataclass
#wenn alle 3 Datenklasses benutzen wollen
#Das erstellt automatisch: __init__ , __repr__, __eq__

@dataclass
class Auto():
   marke: str
   farbe: str
   jahr: int
   modell: str
   tueren: int

auto1 = Auto(marke='Volkswagen',farbe='schwarz',jahr=2020,modell='Virtus',tueren=4)
auto2 = Auto(marke='Audi',farbe='dunkelgruen',jahr=2022,modell='R8',tueren=4)
auto3 = Auto(marke='Volkswagen',farbe='schwarz',jahr=2020,modell='Virtus',tueren=4)
print(auto1)
print(auto1.farbe)
print(auto1 == auto3) # True (Werte)'''




'''class Auto():
    raeder = 4
    
    # wird aufgerufen wenn du Auto("BMW", "rot") schreibst
    def __init__(self,marke,farbe,jahr,modell,tueren): #Dataclass 1
        self.marke = marke
        self.farbe = farbe
        self.jahr = jahr
        self.modell = modell
        self.tueren = tueren
    
    #wird aufgerufen wenn du print(a) schreibst.Ohne es sieht man nutlose Speicheradresse
    def __repr__(self): #Dataclass 2 (fuer Fehlerbehebung )
     return f"Auto(marke={self.marke},farbe={self.farbe})"
    
    #wird aufgerufen wenn du a1 == a2 schreibst. Vergleicht die Werte.
    def __eq__(self,other): #Dataclass 3
      return self.marke == other.marke and self.farbe == other.farbe

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
auto4 = Auto(marke='Volkswagen',farbe='schwarz',jahr=2020,modell='Virtus',tueren=4)

print(auto1.farbe)
auto2.begruessung()

sw1 = Sportwagen(marke='BMW',farbe='Blau',jahr=2024,modell='M4',tueren=2,folierung='Matt',auspuff=2)
sw1.begruessung()

print(auto1 == auto4)'''

