# EPR_00_03


eingabe = eval(input("Gebe eine maximal fuensstellige Zahl ein "))
eingabe = int(eingabe)
laenge = len(str(eingabe))
vorkommastelle = eingabe//1000
rest = eingabe % 1000
x = eingabe
while laenge > 5:
    print("Bitte nur eine maximal FUENFSTELLIGE Zahl eingeben!")
    eingabe = eval(input("Gebe nun eine maximal fuensstellige Zahl ein "))
    laenge = len(str(eingabe))

while laenge < 6:
    if laenge == 1:
        print(str(eingabe), "mit Tausendertrennzeichen ist:", "0.00" + str(eingabe))
        x = "0.00" + str(eingabe)
    elif laenge == 2:
        print(str(eingabe), "mit Tausendertrennzeichen ist:", "0.0" + str(eingabe))
        x = "0.0" + str(eingabe)
    elif laenge == 3:
        print(str(eingabe), "mit Tausendertrennzeichen ist:", "0." + str(eingabe))
        x = "0." + str(eingabe)
    elif laenge == 4 or 5:
        print(str(eingabe), "mit Tausendertrennzeichen ist:", str(vorkommastelle) + "." + str(rest))
        x = str(vorkommastelle) + "." + str(rest)
    break

if eingabe % 2 == 0:
    print(str(x), "ist eine gerade Zahl")
else:
    print(str(x), "ist eine ungerade Zahl")

if eingabe % 7 == 3:
    print(str(x), "ist durch 7 mit einem Rest von 3 Teibar")
else:
    print(str(x), "ist NICHT durch 7 mit einem Rest von 3 Teibar")