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

#List Comprehension--------------------------------------------
'''zahlen = [2,3,5,7,9]
neuZahlen = [i*5 for i in zahlen] 
print(neuZahlen) #[10, 15, 25, 35, 45]

groesserZahlen = [i for i in zahlen if i > 5]
print(groesserZahlen) #[7, 9]

blocks = [
    {"type": "text", "text": "Hallo"},
    {"type": "tool_use", "text": "..."},
    {"type": "text", "text": "Welt"},
]

texte = [b["text"] for b in blocks if b["type"] == "text"] # texte = ["Hallo", "Welt"]'''


#Tupel------------------------------------------------------
# Diese sind unveranderlich (immutable)
'''tupelListe = (1, 2, 3, 'Hallo', True)
print(type(tupelListe)) # <class 'tuple'>
tupelListe[2] = 2.5 # Fehler: Tupel sind unveränderlich'''


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

#Set----------------------------------------------------------------
'''zahlen = {1, 2, 3, 3, 2}  # → {1, 2, 3}
zahlen.add(4)
zahlen & {2, 4, 6}        # Schnittmenge → {2, 4}'''
