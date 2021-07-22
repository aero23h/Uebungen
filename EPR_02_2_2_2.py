# EPR_02_2_2_2


eingabe = input("Bitte gebe eine ganzzahlige Zahl ein: ")

eingabe = int(eingabe)
addiert = 0
median = 0
arit = 0

if eingabe < 0:                                                         # wenn Eingabe negativ ist
    for i in range(eingabe, 0 + 1):
        addiert = addiert - i
        arit = addiert / eingabe
        median = arit

if eingabe > 0:                                                         # wenn Eingabe posiiv ist
    for i in range(1, eingabe + 1):
        addiert = addiert + i
        arit = addiert / eingabe
        median = arit

if median == int(median):                                               # kommas entfernen
    median = int(median)

if arit == int(arit):
    arit = int(arit)

print("Der Arithmetische Mittelwert ist:", arit, "und der Median:", median)
