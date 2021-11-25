import random


def demander_lvl():
        nb_donner_str = input(f"Choisissez un niveau de 1 à 3 : ")
        try:
            nb_donner_int = int(nb_donner_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez. ")
            return demander_lvl()
        else:
            if nb_donner_int < 1 or nb_donner_int > 3:
                print(f"ERREUR: Le nombre doit être entre 1 et 3. Réessayez.")
                return demander_lvl()
        return nb_donner_int


def demander_nombre(nombre_type):
    nb_donner_str = input(f"Choisissez {nombre_type} : ")
    try:
        nb_donner_int = int(nb_donner_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre. Réessayez. ")
        return demander_nombre(nombre_type)
    else:
        if nb_donner_int < 1:
            print(f"ERREUR: Le nombre doit être supérieur à 0. Réessayez.")
            return demander_nombre(nombre_type)
    return nb_donner_int


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    c = random.randint(0, LVL-1)
    user_rep_int = "baise ses morts"
    while user_rep_int == "baise ses morts":
        if c == 0:
            rep = a + b
            user_rep = input(f"Calculez {a} + {b} : ")
        elif c == 2:
            rep = a * b
            user_rep = input(f"Calculez {a} x {b} : ")
        else:
            rep = a - b
            user_rep = input(f"Calculez {a} - {b} : ")
        try:
            user_rep_int = int(user_rep)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre entier. Réessayez.")
    if rep == user_rep_int:
        return True
    return False


NOMBRE_MIN = 1
NOMBRE_MAX = demander_nombre("le nombre maximal que vous trouverez dans les opérations")
NOMBRE_QUESTION = demander_nombre("le nombre de questions qui vous sera posées")
LVL = demander_lvl()

nbPoints = 0
for i in range(0, NOMBRE_QUESTION):
    print(f"Question n°{i+1} sur {NOMBRE_QUESTION}")
    if poser_question():
        print("Bonne réponse.")
        nbPoints += 1
    else:
        print("Mauvaise réponse.")
    print()

print(f"Score : {nbPoints} / {NOMBRE_QUESTION}")

if nbPoints == 0:
    print("Révisez vos math !")
elif nbPoints == NOMBRE_QUESTION:
    print("Excellent !")
elif nbPoints >= int(NOMBRE_QUESTION/2):
    print("Pas mal.")
else:
    print("Peut mieux faire.")


input()
