# Einfuhrung ------------------------------------------------
"""print('Hallo Welt!')
input('Drücken Sie die Eingabetaste, um fortzufahren...')
name = input('Wie heißen Sie? ')
print('') # Abstand
print('hallo', name)"""

# Wahrungrechner----------------------------------------------------
'''print('Willkommen zum Wahrungsrechner!')
euroBetrag = float(input('Geben Sie den Betrag in Euro ein: '))
rupienBetrag = euroBetrag* 109.35
print(f"{euroBetrag} Euro entsprechen {rupienBetrag} Rupien.")'''

#Einfache Data Typen------------------------------------------------------
''' String: 'Hallo', '123', 'True'
    Integer: 1, 42, -5
    Float: 3.14, -0.001
    Boolean: True, False'''

#Strings-----------------------------------------------------
# Diese sind unveranderlich (immutable)
'''x = 'Hallo Welt'
print(x[0]) # H
print(x[-1]) # t
print(x[0:5]) # Hallo (Slicing)
print(x[:5]) # Hallo
print(x[6:]) # Welt
print(len(x)) # 10 length derZeichenkette
print(x.lower()) # hallo welt
print(x.upper()) # HALLO WELT
print(x.split()) # ['Hallo', 'Welt']
x = 'Ciao' + x[6:] # Ciao Welt'''

#Integers und Floats------------------------------------------------------
'''a = 10
b = 3
print(a / b) # 3.3333333333333335 (Float Division)
print(a // b) # 3 (Integer Division)
print(a ** b) # 1000 (Exponentiation)'''

#Booleans und if & else ------------------------------------------------------
'''print(5 > 3) # True
print(5 < 3) # False

streckeInKm = 2
if streckeInKm < 3:
    print('Lauf zu Fuß')
elif streckeInKm < 5:
    print('Nimm das Fahrrad')
else : 
    print('Nimm das Auto')'''


'''age = int(input('Wie alt sind Sie? '))
anzahl = int(input('Wie viele Tickets möchten Sie kaufen? '))
ticketPreisEuro = 0
if age < 18:
    ticketPreisEuro = 5
elif age >= 18 and age <= 65:
    ticketPreisEuro = 10
else:
    ticketPreisEuro = 7.5

print(f'Der Ticketpreis beträgt {ticketPreisEuro*anzahl} Euro.')'''


#Listen------------------------------------------------------
'''namen = ['Alice', 'Bob', 'Charlie']
print(namen[0] +' hat gewonnen!')

newItem = input('Geben Sie einen neuen Namen ein: ')
namen.append(newItem)
namen.insert(1, 'Diana') # Fügt Diana an der Position 1 ein
namen.remove('Bob') # Entfernt Bob aus der Liste
del namen[0] # Entfernt den ersten Eintrag (Alice) aus der Liste
print(len(namen)) # Gibt die Anzahl der Namen in der Liste aus
print('Charlie' in namen) # Überprüft, ob Charlie in der Liste ist (True/False)
print(namen[1:len(namen)]) # Gibt alle Namen ab der Position 1 bis zum Ende der Liste aus
print(namen)'''

#Tupel------------------------------------------------------
# Diese sind unveranderlich (immutable)
'''tupelListe = (1, 2, 3, 'Hallo', True)
print(type(tupelListe)) # <class 'tuple'>
tupelListe[2] = 2.5 # Fehler: Tupel sind unveränderlich'''




#Schleifen-----------------------------------------------------
#While Schleife---------------------------------------------
'''einkaufsListe = []
entscheidung = 'h'

while entscheidung != 'b':
    entscheidung = input('Möchten Sie noch etwas hinzufügen (h)/entfernen(e)/anzeigen(a)/beenden(b) ? ')
    if(entscheidung == 'e'):
        item = input('Was möchten Sie von der Einkaufsliste entfernen? ')
        if(item in einkaufsListe):
            einkaufsListe.remove(item)
            print('item entfernt')
        else : print('item nicht gefunden')
    elif(entscheidung == 'a'):
        print('Einkaufsliste:' , einkaufsListe)
    elif entscheidung == 'h' : einkaufsListe.append(input('Was möchten Sie zur Einkaufsliste hinzufügen? '))'''

#Ubung: Ratespiel ------------------------------------------------------
'''from random import randint
zahl = randint(1, 100)
ratZahl = 0
versuche = 0
while ratZahl != zahl:
   ratZahl = int(input('Rate eine Zahl zwischen 1 und 100: '))
   versuche += 1
   if ratZahl < zahl:
       print('Zu niedrig! Versuche es erneut.')
   elif ratZahl > zahl:
       print('Zu hoch! Versuche es erneut.')
   else:
       print('Glückwunsch! Du hast die Zahl erraten.', ratZahl)
print(f'Du hast {versuche} Versuche gebraucht.')'''

#For Schleife------------------------------------------------------
'''liste = []
for element in range(3):
    item = input('Geben Sie einen Namen ein: ')
    liste.append(item)

for name in liste:
    print(f"  ⭐ {name}")'''


#Dictionary------------------------------------------------------
#Schlüssel-Wert-Paare
'''person = {
    'name': 'Alice',
    'alter': 30,
    'beruf': 'Entwicklerin',
    'hobbies': ['Lesen', 'Reisen', 'Kochen']
}

print(person['name']) # Alice
print(person['hobbies'][1]) # Reisen
print(person.keys()) # dict_keys(['name', 'alter', 'beruf', 'hobbies'])
print(person.values()) # dict_values(['Alice', 30, 'Entwicklerin', ['Lesen', 'Reisen', 'Kochen']])
person['alter'] = 31 # Aktualisiert das Alter
person.pop('beruf') # Entfernt den Beruf aus dem Dictionary'''


#Funktionen------------------------------------------------------
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


#Tic Tac Toe------------------------------------------------------
# Spielbrett erstellen
'''spielbrett = []

def brett_erstellen() :
    for i in range(3):
      zeile = [' ' for j in range(3)]
      spielbrett.append(zeile)
      
brett_erstellen()
# print(spielbrett)

#Spielbrett anzeigen
def brett_anzeigen() :
    for i, zeile in enumerate(spielbrett):
        
        print('|'.join(zeile))
        if i < len(spielbrett) -1 : print('-' * 5)
    
brett_anzeigen()

def kann_zug_machen(zeile, spalte):
    return spielbrett[zeile][spalte] == ' '

Züge = {
    'X': [],
    'O': []
}

hatGewonnen = False

def gewinner_pruefen(spieler):
    for zeile in range(3):
      if spielbrett[zeile][0] == spieler and spielbrett[zeile][1] == spieler and spielbrett[zeile][2] == spieler:
         return True
      if spielbrett[0][zeile] == spieler and spielbrett[1][zeile] == spieler and spielbrett[2][zeile] == spieler:
         return True
    
    if spielbrett[0][0] == spieler and spielbrett[1][1] == spieler and spielbrett[2][2] == spieler:
         return True
    if spielbrett[0][2] == spieler and spielbrett[1][1] == spieler and spielbrett[2][0] == spieler:
         return True
    return False
   
def spieler_zug(spieler):
    global hatGewonnen
    while True:
        zeile = int(input(f'Spieler {spieler}, gib die Zeilennummer (0-2) ein: '))
        spalte = int(input(f'Spieler {spieler}, gib die Spaltennummer (0-2) ein: '))

        if kann_zug_machen(zeile, spalte):
            Züge[spieler].append([zeile, spalte])
            spielbrett[zeile][spalte] = spieler
            brett_anzeigen()
            if len(Züge[spieler]) >= 3 :
              if gewinner_pruefen(spieler) : 
                 print(f'Spieler {spieler} hat gewonnen!') 
                 hatGewonnen = True
                 break
        else:
            print('Ungültiger Zug! Versuche es erneut.')
            continue

        spieler = 'X' if spieler == 'O' else 'O'


spieler_zug('X')

def ist_unentschieden() : 
  for zeile in spielbrett :
    if ' ' in zeile :
     return False
  
  return True
   
if not hatGewonnen and ist_unentschieden() : print('Unentshieden!')'''

#Exception-------------------------------------------------------------

'''try :
    ergebnis = 100/0
except ZeroDivisionError:
    print('Hey, du darfst nicht mit Zero dividieren !')'''

'''try :
    ergebnis = 100/ '0'
except TypeError:
    print('Typen sollen gleich sein !')
finally :
    print('Keinen Fehler gemacht!')'''

'''x = 5
if x >= 5:
    raise Exception('X soll nicht grosser oder gleich als 5 sein')'''


#Module-----------------------------------------------------------------
#wiederverwendbare Codeteile

'''import willkommen # Code der Datein zugreifen, ohne py
willkommen.empfang('Ankit')'''

#from math import sqrt #Nur spezifische Funktion importieren, anstatt ganzen Block zu importiern

