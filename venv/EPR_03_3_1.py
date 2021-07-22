# EPR_03_3_1


def schnitt(x, y):
    durchschnitt = (int(y) + int(x)) / 2
    print("Der Durchschnitt ist gerundet:", int(durchschnitt))
    return int(durchschnitt)


def ziffern(number):
    number_first = 0
    number_last = 0
    count = 0
    for i in range(0, len(str(number))):
        count = count + 1
        if i == 0:
            if number < 0:
                number_first = str(number)[i+1]
                count = count - 1
            else:
                number_first = str(number)[i]
        elif i == len(str(number))-1:
            number_last = str(number)[i]
            print("erste Ziffer:", number_first + ",", "letzte Ziffer:", number_last + ",",
                  "und gesamte Anzahl Ziffern:", count)


def backwards(number):
    back = 0
    for j in range(len(str(number)), 0):
        back = str(back) + str(number)[j]
        print(back)


def main():
    eingabe1 = input("erste Zahl pls: ")
    eingabe2 = input("zweite Zahl pls: ")
    durchschnitt = schnitt(eingabe1, eingabe2)
    ziffern(durchschnitt)
    backwards(durchschnitt)


if __name__ == '__main__':
    main()