addiert = 0
quadrozahl = 0
stop = False
test = False
positiv = False
counter = 0
jo = True
lauf = True

zahl = input("Gebe bitte eine natürliche Zahl ein: ")


while test or positiv is False:
    try:                                                                                #Test ob Zahl Integer ist
        int(zahl)
        test = True
        zahl = int(zahl)
        if zahl <= 0:                                                                   #Test ob Zahl negativ ist
            zahl = input("Gebe bitte eine NATÜRLICHE ZAHL (positive Ganzzahl) ein: ")
            zahl = str(zahl)
        elif zahl > 0:
            positiv = True
            zahl = str(zahl)
    except ValueError:                                                                  #Zahl kein Integer
        test = False
        zahl = input("Gebe bitte eine NATÜRLICHE ZAHL (positive Ganzzahl) ein: ")
    if test and positiv is True:
        break

zahl = str(zahl)
while stop is False:
    for i in range(0, len(str(zahl))):
        quadrozahl = zahl[i]
        quadriert = int(quadrozahl) ** 2                                                #Berechnung
        addiert = addiert + quadriert
        if i == len(str(zahl)) - 1:
            zahl = str(addiert)
            addiert = 0
            counter = counter + 1
            #if zahl == "4":                             #weitere möglichkeit ohne betrachten der Iterationen
            #   counter = counter + 1
            #  print("Das Endergebnis ist:", zahl + ", und somit nicht fröhlich.")
            # stop = True
            if zahl == "1":
                print("Das Endergebnis ist:", zahl + ", und somit fröhlich.")
                stop = True
            elif counter == 100:
                print("Algorithmus wurde nach 100 Iterationen abgebrochen. Das Ergebnis ist somit nicht Fröhlich")

