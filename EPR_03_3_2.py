'''x = 7                                            #Teil ohne Funktion
string = ""
for x in range(x, 18, 2):
    print("x is ", x)
    string += " " + str(x)
    x += 2
    print("Now, x is ", x)
    print("All previous numbers: ", string)'''

def funktion(x, y):
    x = int(x)
    y = int(y)
    string = ""
    for x in range(7, x, y):
        print("x is ", x)
        string += " " + str(x)
        x += 2
        print("Now, x is ", x)
        print("All previous numbers: ", string)


def main():
    lenght = input("Wie lange soll das Programm laufen?: ")
    steps = input("in welchen Schritten soll das Programm laufen?: ")
    funktion(lenght, steps)


if __name__ == '__main__':
    main()
