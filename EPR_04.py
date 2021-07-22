# EPR_04

import EPR_04_names
import random


def random_man():
    """set random name for male"""
    r_man = random.choice(EPR_04_names.man)
    return r_man


def random_woman():
    """set random name for woman"""
    r_woman = random.choice(EPR_04_names.woman)
    return r_woman


def random_lastname():
    """set random lastname"""
    r_lastname = random.choice(EPR_04_names.lastname)
    return r_lastname


def random_firstname():
    """set random firstname"""
    r_firstname = (random_woman(), random_man())
    r_firstname = random.choice(r_firstname)

    return r_firstname


def random_secondname():
    """probability second firstmane"""
    probability_secondname = [.1, .9]
    r_secondname = random_firstname(), None
    r_secondname = random.choices(r_secondname, probability_secondname)

    return r_secondname


def second_lastname():
    """probability second lastname"""
    probability_secondlastname = [.15, .85]
    lastlastname = random_lastname(), None
    lastlastname = random.choices(lastlastname, probability_secondlastname)

    return lastlastname


def titel():
    """probability for titel (Dr.)"""
    probability_dr = [.01, .99]
    titel_dr = "Dr. ", None
    titel_dr = random.choices(titel_dr, probability_dr)

    return titel_dr


def complete_name():
    """create a random name"""
    # execute functions for names
    firstname = ""
    lastname = ""
    x_random_secondname = random_secondname()
    x_random_firstname = random_firstname()
    x_random_lastname = random_lastname()
    x_random_lastlastname = second_lastname()
    x_titel = titel()

    # remove inequality
    while x_random_firstname == x_random_secondname:
        x_random_secondname = random_secondname()
        x_random_firstname = random_firstname()
    while x_random_lastlastname == x_random_lastname:
        x_random_lastlastname = random_secondname()

    # removing unnecessary characters
    x_random_lastname = str(str(x_random_lastname).translate({ord(i): None for i in "'[]()"}))
    x_random_lastlastname = str(str(x_random_lastlastname).translate({ord(i): None for i in "'[]()"}))
    x_random_firstname = str(str(x_random_firstname).translate({ord(i): None for i in "'[]()"}))
    x_random_secondname = str(str(x_random_secondname).translate({ord(i): None for i in "'[]()"}))
    x_titel = str(str(x_titel).translate({ord(i): None for i in "'[]()"}))

    # complete firstname
    if x_random_secondname == "None":
        firstname = x_random_firstname
    if x_random_secondname != "None":
        firstname = x_random_firstname + "-" + x_random_secondname
    elif x_titel == "Dr. ":
        firstname = "Dr. " + firstname

    # complete lastname
    if x_random_lastlastname == "None":
        lastname = x_random_lastname
    if x_random_lastlastname != "None":
        lastname = str(x_random_lastname + "-" + x_random_lastlastname)

    return firstname + " " + lastname


def streetname():
    probability_streetnames = [.1, .08, .07, .07, .07, .07, .06, .04, .04, .04]
    pick1 = random.choice(EPR_04_names.city_prefix)
    pick2 = random.choice(EPR_04_names.tree_prefix)
    pick3 = random.choice(EPR_04_names.flower_prefix)
    pick4 = random.choice(EPR_04_names.famous_prefix)
    pick5 = random.choices(EPR_04_names.street_names, probability_streetnames)
    all_picks = [pick1, pick2, pick3, pick4, pick5]
    random_prefix = random.choice(all_picks)

    # pick random suffix
    probability_suffix = [.78, .18, .02, .01, .01]
    random_suffix = random.choices(list(EPR_04_names.suffix_names), probability_suffix)
    random_suffix = str(random_suffix)

    # removing unnecessary characters
    random_prefix = str(str(random_prefix).translate({ord(i): None for i in "'[]()"}))
    random_suffix = str(str(random_suffix).translate({ord(i): None for i in "'[]()"}))

    # right style
    if random_prefix not in EPR_04_names.city_prefix:
        random_suffix = random_suffix[0].lower() + random_suffix[1:]  # first letter lowercase
    if random_prefix in EPR_04_names.city_prefix:
        random_prefix = random_prefix + " "

    return random_prefix + random_suffix


def housenumber():
    letters_a_f = random.choice("abcdef")
    letters_g_z = random.choice("ghijklmnopqrstuvwxyz")
    all_letters = letters_a_f + letters_g_z

    housenumber_1_20 = random.randint(1, 10)
    housenumber_21_60 = random.randint(11, 60)
    housenumber_61_100 = random.randint(61, 100)
    housenumber_101_200 = random.randint(101, 200)

    # probabilitys
    probability_letters = [.9, .1]
    probability_houseumbers = [.8, .15, .04, .01]
    probability_of_letter = [.2, .8]

    all_random_housenumbers = housenumber_1_20, housenumber_21_60, housenumber_61_100, housenumber_101_200
    final_housenumber = random.choices(all_random_housenumbers, probability_houseumbers)

    # setting housletter
    final_houseletter = random.choices(all_letters, probability_letters)
    final_houseletter = final_houseletter, None
    final_houseletter = random.choices(final_houseletter, probability_of_letter)

    # removing unnecessary characters
    final_houseletter = str(str(final_houseletter).translate({ord(i): None for i in "'[]()"}))
    final_housenumber = str(str(final_housenumber).translate({ord(i): None for i in "'[]()"}))

    # complete final housenumber
    if final_houseletter == "None":
        return final_housenumber
    else:
        return final_housenumber + final_houseletter


def main():
    count = 0
    while count != 1000:
        complete = complete_name(), streetname() + " " + housenumber()
        complete = str(str(complete).translate({ord(i): None for i in "'[]()"}))
        count += 1
        print(complete)


if __name__ == '__main__':
    main()
