eingabe = input("Wie viel Punkte hast du? ")

while not 0 <= int(eingabe) <= 15:                                      #Eingabe nicht 1-15
    print("Bitte nur Notenpunkte zwischen 1 und 15 eingeben")
    eingabe = input("Wie viel Punkte hast du nun? ")

note = (17 - int(eingabe)) / 3                                          #Umrechnung
note = int(note.__round__(0))

while int(note) < 4:                                                    #Bestanden
    if 1 <= int(eingabe) <= 15:
        if int(eingabe) % 3 == 1:
            print("Deine Note ist:", str(note) + "-" + ", du hast bestanden :)")
            break
        elif int(eingabe) % 3 == 0:
            print("Deine Note ist:", str(note) + "+" + ", du hast bestanden :)")
            break
        else:
            print("Deine Note ist:", str(note) + ", du hast bestanden :)")
    break

while int(note) >= 4:                                                   #Nicht bestanden
    if 0 <= int(eingabe) <= 15:
        if int(eingabe) % 3 == 1:
            print("Deine Note ist:", str(note) + "-" + ", du hast leider nicht bestanden :(")
            break
        elif int(eingabe) % 3 == 0:
            print("Deine Note ist:", str(note) + "+" + ", du hast leider nicht bestanden :(")
            break
        if int(eingabe) == 0:
            print("Deine Note ist:", str(note) + ", du hast leider nicht bestanden :(")
            break
        else:
            print("Deine Note ist:", str(note) + ", du hast leider nicht bestanden :(")
    break

