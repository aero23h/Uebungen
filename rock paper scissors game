# EPR_03_3_3

import random
import time
import EPR_03_3_3_2                                 # import des Nebenprogramms (Funktionen für Brunnen und Streichholz)
t1 = 1
t05 = 0.5
t08 = 0.8


def ssp_s():                                                                                   # Spielerinput: Schere(s)
    random.shuffle(possibilities)
    computer_input = possibilities[0]
    if computer_input == "s":
        time.sleep(t1)
        print("Computer's Wahl: Schere" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Unentschieden!")
    elif computer_input == "r":
        time.sleep(t1)
        print("Computer's Wahl: Stein" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Verloren!")
    elif computer_input == "p":
        time.sleep(t1)
        print("Computer's Wahl: Papier" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Gewonnen!")


def ssp_r():                                                                                    # Spielerinput: Stein(r)
    random.shuffle(possibilities)
    computer_input = possibilities[0]
    if computer_input == "s":
        time.sleep(t1)
        print("Computer's Wahl: Schere" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Gewonnen!")
    elif computer_input == "r":
        time.sleep(t1)
        print("Computer's Wahl: Stein" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Unentschieden!")
    elif computer_input == "p":
        time.sleep(t1)
        print("Computer's Wahl: Papier" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Verloren!")
    elif computer_input == "w":
        time.sleep(t1)
        print("Computer's Wahl: Brunnen" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Verloren!")
    elif computer_input == "m":
        time.sleep(t1)
        print("Computer's Wahl: Streichholz" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Gewonnen!")


def ssp_p():                                                                                   # Spielerinput: Papier(p)
    random.shuffle(possibilities)
    computer_input = possibilities[0]
    if computer_input == "s":
        time.sleep(t1)
        print("Computer's Wahl: Schere" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Verloren!")
    elif computer_input == "r":
        time.sleep(t1)
        print("Computer's Wahl: Stein" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Gewonnen!")
    elif computer_input == "p":
        time.sleep(t1)
        print("Computer's Wahl: Papier" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Unentschieden!")
    elif computer_input == "w":
        time.sleep(t1)
        print("Computer's Wahl: Brunnen" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Gewonnen!")
    elif computer_input == "m":
        time.sleep(t1)
        print("Computer's Wahl: Streichholz" + "(" + computer_input + ")")
        time.sleep(t08)
        print("Du hast Verloren!")


possibilities = ["s", "r", "p", "w", "m"]


def main():
    again_right = False
    go = False
    game = True
    again = True
    print("Komm! Wir spielen Schere, Stein, Papier :)")
    time.sleep(t05)
    print("Möchtest du dir vorher noch die Regeln durchlesen?\n"                 # Frage ob Regeln geziegt werden sollen
          "Ja(y)\n"
          "Nein(n)")
    rules = input("\n--> ")
    if rules == "y":                                                                             # Aufzählung der Regeln
        print("-Schere schneidet Papier")
        time.sleep(t1)
        print("-Schere schneidet Streichholz")
        time.sleep(t1)
        print("-Papier umwickelt Stein")
        time.sleep(t1)
        print("-Papier bedeckt Brunnen")
        time.sleep(t1)
        print("-Stein macht Schere Stumpf")
        time.sleep(t1)
        print("-Stein macht Streichholz kaputt")
        time.sleep(t1)
        print("-Schere fällt in Brunnen")
        time.sleep(t1)
        print("-Stein fällt in Brunnen")
        time.sleep(t1)
        print("-Streicholz schwimmt im Brunnen")
        time.sleep(t1)
        print("-Streichholz verbrennt Papier")
        time.sleep(t05)
        print("\nna dann legen wir mal los :)\n")
        time.sleep(t1)

    while game and again is True:
        again_right = False
        print("Bitte Wähle aus:\n"                                                           # erste Auswahl 
              "Schere(s)\n"
              "Stein(r)\n"
              "Papier(p)\n"
              "Brunnen(w)\n"
              "Schtreichholz(m)\n"
              "Spiel beenden(e)")
        player_input = input("\n--> ")

        if player_input == "e":                                                             # Spiel beenden
            time.sleep(t05)
            print("Game Over")
            game = False
            break

        if player_input not in possibilities:                                           # Schleife zur korrekten Eingabe
            go = False
            while go is False:
                print("Bitte Wähle aus:\n"
                      "Schere(s)\n"
                      "Stein(r)\n"
                      "Papier(p)\n"
                      "Brunnen(w)\n"
                      "Schtreichholz(m)\n"
                      "Spiel beenden(e)")
                time.sleep(t08)
                player_input = input("\n-->")
                if player_input == "e":                                                      # Spiel beenden
                    time.sleep(t05)
                    print("Game Over")
                    game = False
                    break

                if player_input in possibilities:
                    go = True

        if player_input == "s":                                                       # aufrufen der Funktion für Schere
            ssp_s()
        if player_input == "r":                                                        # aufrufen der Funktion für Stein
            ssp_r()
        if player_input == "p":                                                       # aufrufen der Funktion für Papier
            ssp_p()
        if player_input == "w":                                                      # aufrufen der Funktion für Brunnen
            EPR_03_3_3_2.ssp_w()
        if player_input == "m":                                                  # aufrufen der Funktion für Streichholz
            EPR_03_3_3_2.ssp_m()

        while again_right is False and game is True:                                    # Schleife zur korrekten Eingabe
            time.sleep(t08)
            print("\nnochmal?\n"                                       # Abfrage ob noch eine Runde gespielt werden soll
                  "ja(y)\n"
                  "Nein(n)")
            time.sleep(t08)
            again_input = input("\n--> ")
            if again_input == "y":
                again_right = True
                again = True
            elif again_input == "n":
                time.sleep(t05)
                print("Okey, Tschüss :)")
                again_right = True
                again = False


if __name__ == '__main__':
    main()
