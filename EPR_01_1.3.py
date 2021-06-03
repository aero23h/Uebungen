eingabe = input("Gebe bitte eine  aussagenlogische Formel in Form ('Bool' 'Verknüpfung' 'Bool') ein: ")

i = 0
j = 0
z = ""
x = ""
y = ""
ergebnis = ""

for i in range(0, len(eingabe)):                                    #erstes Wort
    if eingabe[i] == chr(32):
        x = eingabe[0:i]
        break
for j in range(i+1, len(eingabe)):                                  #zweites Wort
    if eingabe[j] == chr(32):
        y = eingabe[i+1:j]
        z = eingabe[j+1:]                                           #letztes Wort
        break

if x == "True":                                                     #variablen zu Bool
    x = True
elif x == "False":
    x = False

if z == "False":
    z = False
elif z == "True":
    z = True

if y == "and":                                                      #finale Rechnung
    ergebnis = x and z
if y == "or":
    ergebnis = x or z

print("Das Ergebnis deiner Formel ist:", ergebnis)

