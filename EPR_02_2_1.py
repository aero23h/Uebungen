# EPR_02_2_1


import random

wuerfe = 0
zahl = 0
x = True

# variante mit Break

while x is True:
    zahl = random.randint(-9, 9)                                                    # random Zahl
    wuerfe = wuerfe + 1
    if zahl != -9 and zahl != 3:
        print("Es wurde die Zahl", zahl, "geworfen. Wurf:", str(wuerfe))            # random Wurf
    elif zahl == -9 or zahl == 3:
        if wuerfe == 1:
            print("Die Zahl", zahl, "wurde nach EINEM Wurf getroffen.")             # erster Wurf ein Treffer
        elif wuerfe > 1:
            print("Die Zahl", zahl, "wurde nach", wuerfe, "Würfen getroffen.")      # Treffer mit Wuerfen >1
        break


# variante ohne Break

'''
while zahl != 3 and zahl != -9:
    zahl = random.randint(-9, 9)                                                    # random Zahl
    wuerfe = wuerfe + 1
    if zahl != -9 and zahl != 3:
        print("Es wurde die Zahl", zahl, "geworfen. Wurf:", str(wuerfe))            # random Wurf
    elif zahl == -9 or zahl == 3:
        if wuerfe == 1:
            print("Die Zahl", zahl, "wurde nach EINEM Wurf getroffen.")             # erster Wurf ein Treffer
        elif wuerfe > 1:
            print("Die Zahl", zahl, "wurde nach", wuerfe, "Würfen getroffen.")      # Treffer mit Wuerfen >1
'''