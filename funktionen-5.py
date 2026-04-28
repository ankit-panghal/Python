'''def begruessung(name='Gast'):
    print(f'Hallo, {name}! Willkommen zum Python Kurs.')

begruessung() # Hallo, Gast! Willkommen zum Python Kurs.
begruessung('Alice') # Hallo, Alice! Willkommen zum Python Kurs.'''

'''def berechne_flaeche(radius):
    pi = 3.14159
    return pi * radius ** 2

radius = float(input('Geben Sie den Radius des Kreises ein: '))
flaeche = berechne_flaeche(radius)
print(f'Die Fläche eines Kreises mit Radius {radius} ist {flaeche}.')'''

'''def addieren(*zahlen):
    return sum(zahlen)

print(addieren(1, 2, 3)) # 6'''

'''def objekt(**eigenschaften):
    for key, value in eigenschaften.items():
        print(f"{key}: {value}")
    
objekt(name='Auto', farbe='Rot', marke='Toyota')'''