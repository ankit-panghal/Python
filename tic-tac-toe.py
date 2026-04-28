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