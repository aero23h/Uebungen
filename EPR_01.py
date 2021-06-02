eingabe = eval(input("Bitte gebe eine Ganzzahl ein "))

teilbarkeit3 = 0
teilbarkeit5 = 0
teilbarkeit7 = 0
gerade = 0

if eingabe % 3 == 0:
    teilbarkeit3 = True

if eingabe % 5 == 0:
    teilbarkeit5 = True

if eingabe % 7 == 0:
    teilbarkeit7 = True

if eingabe % 2 == 0:
    gerade = True

while teilbarkeit7 or teilbarkeit5 or teilbarkeit3 is True:
    if teilbarkeit3 and teilbarkeit5 and teilbarkeit7 is True:              #Teilbarkeit 3, 5 und 7
        if teilbarkeit3 and teilbarkeit5 and teilbarkeit7 and gerade is True:
            print(eingabe, "ist durch 3, 5 und 7 teilbar und gerade")
        else:
            print(eingabe, "ist durch 3, 5 und 7 teilbar und ungerade")
        break
    if teilbarkeit3 and teilbarkeit5 is True:                               #Teilbarkeit 3 und 5
        if teilbarkeit3 and teilbarkeit5 and gerade is True:
            print(eingabe, "ist durch 3 und 5 teilbar und gerade")
        else:
            print(eingabe, "ist durch 3 und 5 teilbar und ungerade")
        break
    if teilbarkeit3 and teilbarkeit7 is True:                               #Teilbarkeit 3 und 7
        if teilbarkeit3 and teilbarkeit7 and gerade is True:
            print(eingabe, "ist durch 3 und 7 teilbar und gerade")
        else:
            print(eingabe, "ist durch 3 und 7 teilbar und ungerade")
        break
    if teilbarkeit5 and teilbarkeit7 is True:                               #Teilbarkeit 5 und 7
        if teilbarkeit5 and teilbarkeit7 and gerade is True:
            print(eingabe, "ist durch 5 und 7 teilbar und gerade")
        else:
            print(eingabe, "ist durch 5 und 7 teilbar und ungerade")
        break
    if teilbarkeit3 is True:                                                #Teilbarkeit 3
        if teilbarkeit3 and gerade is True:
            print(eingabe, "ist durch 3 teilbar und gerade")
        else:
            print(eingabe, "ist nur durch 3 teilbar und ungerade")
        break
    if teilbarkeit5 is True:                                                #Teilbarkeit 5
        if teilbarkeit5 and gerade is True:
            print(eingabe, "ist durch 5 teilbar und gerade")
        else:
            print(eingabe, "ist nur durch 5 teilbar und ungerade")
        break
    if teilbarkeit7 is True:                                                #Teilbarkeit 7
        if teilbarkeit7 and gerade is True:
            print(eingabe, "ist durch 7 teilbar und gerade")
        else:
            print(eingabe, "ist nur durch 7 teilbar und ungerade")
        break
else:
    if gerade is True:
        print(eingabe, "ist weder durch 3, 5 oder 7 teilbar aber gerade")
    else:
        print(eingabe, "ist weder durch 3, 5 oder 7 teilbar und ungerade")