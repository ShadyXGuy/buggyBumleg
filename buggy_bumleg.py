def checkForBUM(tal, bumtal):
    if tal % bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False

BumDefined = False
while BumDefined == False:
    bum = input('Vælg et bumtal: ')
    if bum.isdigit() and int(bum) > 0:
        bum = int(bum)
        BumDefined = True

tur = 1

for i in range(1, 51):
    valg = input('Tal eller bum? ')
    print (i)
    if checkForBUM(i, bum):
        korrekt = 'bum'
    else:
        korrekt = str(i)

    # Kontroller spillerens indtastning
    if valg == korrekt:
        print('Korrekt!')
    else:
        print('Forkert!')

    # Skift spiller
    if tur == 1:
        tur = 2
    else:
        tur = 1
