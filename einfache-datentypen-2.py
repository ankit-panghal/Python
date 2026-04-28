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