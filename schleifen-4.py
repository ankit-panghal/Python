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