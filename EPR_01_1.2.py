eingabe = input("Wie viel Punkte hast du? ")

while not 0 <= int(eingabe) <= 15:
    print("Bitte nur Notenpunkte zwischen 1 und 15 eingeben")
    eingabe = input("Wie viel Punkte hast du nun? ")

note = (17 - int(eingabe)) / 3
note = int(note.__round__(0))
if 1 <= int(eingabe) <= 15:
    if int(eingabe) % 3 == 1:
        print("Deine Note ist:", str(note) + "-")
    elif int(eingabe) % 3 == 0:
        print("Deine Note ist:", str(note) + "+")
    else:
        print("Deine Note ist:", str(note))

if int(eingabe) == 0:
    print("Deine Note ist:", str(note))
