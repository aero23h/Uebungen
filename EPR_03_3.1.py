eingabe1 = input("erste Zahl pls: ")
eingabe2 = input("zweite Zahl pls: ")


def durchsschnitt(x, y):
    x = (int(y) + int(x)) / 2
    return x


def main():
    print("Der Durchsschnitt ist:", str(int(durchsschnitt(eingabe1, eingabe2))) + ",", "und deren type ist:",
          type(durchsschnitt(eingabe1, eingabe2)))


if __name__ == '__main__':
    main()
