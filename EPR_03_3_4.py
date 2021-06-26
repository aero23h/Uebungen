

def wandler(numbers):
    number_complete = ""
    if numbers == "eins":
        number_complete = "1"
    elif numbers == "zwei":
        number_complete = "2"
    elif numbers == "drei":
        number_complete = "3"
    elif numbers == "vier":
        number_complete = "4"
    elif numbers == "fuenf":
        number_complete = "5"
    elif numbers == "sechs":
        number_complete = "6"
    elif numbers == "sieben":
        number_complete = "7"
    elif numbers == "acht":
        number_complete = "8"
    elif numbers == "neun":
        number_complete = "9"
    return number_complete


def main():
    complete = ""
    number_main = ""

    print("Bitte gebe eine zahl in Wörtern ein. Einzelne Zahlen getrennt durch Komma ohne Leerzeichen (1-9)")
    user_input = input("--> ")

    number_list = ["eins", "zwei", "drei", "vier", "fuenf", "sechs", "sieben", "acht", "neun"]
    for i in range(0, len(user_input)):
        if user_input[i] == ",":                                                                    #Komma überspringen
            continue
        number_main = number_main + user_input[i]                               #einzelnes Wort einer Variable zuordnen
        if number_main in number_list:
            complete += wandler(number_main)                                      #Wort über Funktion in Zahl umwandeln
            number_main = ""
        if i == len(user_input) - 1:                                       #Print der ganzen Zahlen am Ende der Eingabe
            print(complete)


if __name__ == '__main__':
    main()
