import turtle as tl
import random

def afficher_bateau(liste_coordonnees_bateau):
    """shows the 3 boats of player one"""

    for element in liste_coordonnees_bateau:
        tl.penup()
        tl.setposition(element[0] * 50, element[1] * 50)
        tl.pendown()
        tl.dot(30, "grey")


def definir_position_bateau_joueur():
    """asks player one to define the position of one of his boats (with the coordinates of the bow)"""

    liste_coordonnees_bateau = []
    xproue = -7
    yproue = -7
    orientation = ""

    # we ask player one the orientation of his boat
    while orientation != "H" and orientation != "V":
        orientation = input(
                "Veuillez choisir H pour représenter votre bateau Horizontalement ou V pour représenter votre bateau Verticalement : ")

    # if the boat is heading East, we fill up the list of coordinates of the boat
    if orientation == "H":
        while yproue < - 6 or yproue > 6:
            yproue = int(
                    input(
                        "A quelle latitude va naviguer votre bateau (entre -6 et +6) ? "))
        while xproue < -6 or xproue > 3:
            xproue = int(
                    input(
                        "A quelle longitude se trouve la proue de votre bateau (entre -6 et +3) ? "))
        for i in range(4):
            liste_coordonnees_bateau.append((xproue + i, yproue))

    # if the boat is heading North, we fill up the list of coordinatues of the boat
    if orientation == "V":
        while xproue < -6 or xproue > 6:
            xproue = int(
                    input(
                        "A quelle longitude va naviguer votre bateau (entre -6 et +6) ? "))
        while yproue < - 3 or yproue > 6:
            yproue = int(
                    input(
                        "A quelle latitude se trouve la proue votre bateau (entre -3 et +6) ? "))
        for i in range(4):
            liste_coordonnees_bateau.append((xproue, yproue - i))

    return liste_coordonnees_bateau


def definir_position_bateaux_ordinateur():
    """defines the positions of the computer's 3 boats"""

    liste_coordonnees_bateaux = [[(3, 0), (3, 1), (3, 2), (3, 3)],
                                 [(1, 2), (1, 3), (1, 4), (1, 5)],
                                 [(0, -1), (1, -1), (2, -1), (3, -1)]]

    return liste_coordonnees_bateaux


def demander_joueur_position_tir():
    """asks player one the coordinates for the hit"""

    # necessary to start the while loop
    xtir = -7
    ytir = -7

    print()
    while xtir < -6 or xtir > 6:
        xtir = int(input("longitude du tir (entre -6 et +6) ? "))
    while ytir < - 6 or ytir > 6:
        ytir = int(input("latitude du tir (entre -6 et +6) ? "))

    return (xtir, ytir)


def ordinateur_tire(score, liste_bon_tir, liste_mauvais_tir, liste_coordonnees_bateaux_joueur,
                    liste_touche_bateaux_joueur, liste_coordonnees_bateaux_ordinateur, liste_touche_bateaux_ordinateur):
    """when the computer hits, the score, the list of good hits and the list of bad hits are updated.
    If a boat is hit twice, it is sunk. The count of hits for a boat is recorded in liste_touche_bateaux_ordinateur."""

    x = random.randint(-6, 6)
    y = random.randint(-6, 6)
    resultat = ""

    # for each of the 3 boats
    for i in range(3):

        # if the coordinates hit one of the player's boats, the score and the list
        # of good hits are updated. If a boat is hit twice, it is sunk. The count of hits
        # for a boat is recorded in liste_touche_bateaux_joueur.
        if (x, y) in liste_coordonnees_bateaux_joueur[i]:
            if liste_touche_bateaux_joueur[i] == 0:
                score += 1
                liste_touche_bateaux_joueur[i] += 1
                resultat = "L'ordinateur a touché un bateau !"
                liste_bon_tir.append((x, y))
            elif liste_touche_bateaux_joueur[i] == 1:
                score += 10
                liste_touche_bateaux_joueur[i] += 1
                resultat = "L'ordinateur a coulé un bateau !"
                liste_bon_tir.append((x, y))

        # if the coordinates hit one of the computer's boat
        elif (x, y) in liste_coordonnees_bateaux_ordinateur[i]:
            if liste_touche_bateaux_ordinateur[i] == 0:
                score -= 1
                liste_touche_bateaux_ordinateur[i] += 1
                resultat = "L'ordinateur a touché un de ses bateaux !"
            elif liste_touche_bateaux_ordinateur[i] == 1:
                score -= 10
                liste_touche_bateaux_ordinateur[i] += 1
                resultat = "L'ordinateur a coulé un de ses bateaux !"

    # if the coordinates don't hit anything, the list of bad hits is updated
    if resultat == "":
            resultat = "Le tir de l'ordinateur est dans l'eau !"
            liste_mauvais_tir.append((x, y))

    print(resultat)

    return (score, liste_bon_tir, liste_mauvais_tir, liste_touche_bateaux_joueur, liste_touche_bateaux_ordinateur)


def joueur_tire(x, y, score, liste_bon_tir, liste_mauvais_tir, liste_coordonnees_bateaux_ordinateur, liste_touche_bateaux_ordinateur, liste_coordonnees_bateaux_joueur, liste_touche_bateaux_joueur):
    """when player one hits, the score, the list of good hits and the list of bad hits are updated.
    If a boat is hit twice, it is sunk. The count of hits for a boat is recorded in liste_touche_bateaux_ordinateur."""

    resultat = ""

    # for each of the 3 boats
    for i in range(3):

        # if the coordinates hit one of the computer's boats, the score and the list
        # of good hits are updated. If a boat is hit twice, it is sunk. The count of hits
        # for a boat is recorded in liste_touche_bateaux_ordinateur.
        if (x, y) in liste_coordonnees_bateaux_ordinateur[i]:
            if liste_touche_bateaux_ordinateur[i] == 0:
                score += 1
                liste_touche_bateaux_ordinateur[i] += 1
                resultat = "Vous avez touché un bateau !"
                liste_bon_tir.append((x, y))
            elif liste_touche_bateaux_ordinateur[i] == 1:
                score += 10
                liste_touche_bateaux_ordinateur[i] += 1
                resultat = "Vous avez coulé un bateau !"
                liste_bon_tir.append((x, y))

        # if the coordinates hit one of the player's boat
        elif (x, y) in liste_coordonnees_bateaux_joueur[i]:
            if liste_touche_bateaux_joueur[i] == 0:
                score -= 1
                liste_touche_bateaux_joueur[i] += 1
                resultat = "Vous avez touché un de vos bateaux !"
            elif liste_touche_bateaux_joueur[i] == 1:
                score -= 10
                liste_touche_bateaux_joueur[i] += 1
                resultat = "Vous avez coulé un de vos bateaux !"

    # if the coordinates don't hit anything, the list of bad hits is updated
    if resultat == "":
            resultat = "Votre tir est dans l'eau !"
            liste_mauvais_tir.append((x, y))

    print(resultat)

    return (score, liste_bon_tir, liste_mauvais_tir, liste_touche_bateaux_ordinateur, liste_touche_bateaux_joueur)


def afficher_resultats_tir_joueur(score, liste_bon_tir, liste_mauvais_tir):
    """prints the player one score and shows the hits in a turtle window"""

    print("VOTRE SCORE", score, "points.")

    if len(liste_bon_tir) != 0:
        tl.penup()
        tl.setposition(liste_bon_tir[-1][0] * 50,
                           liste_bon_tir[-1][1] * 50)
        tl.pendown()
        tl.dot(30, "orange")

    if len(liste_mauvais_tir) != 0:
        tl.penup()
        tl.setposition(liste_mauvais_tir[-1][0] * 50,
                           liste_mauvais_tir[-1][1] * 50)
        tl.pendown()
        tl.dot(30, "navy")


def afficher_resultats_tir_ordinateur(score, liste_bon_tir, liste_mauvais_tir):
    """prints the compute score and shows the hits in a turtle window"""

    print("SCORE DE L'ORDINATEUR", score, "points.")

    for i in range(len(liste_bon_tir)):
        tl.penup()
        tl.setposition(liste_bon_tir[i][0] * 50,
                           liste_bon_tir[i][1] * 50)
        tl.pendown()
        tl.dot(30, "red")

    for i in range(len(liste_mauvais_tir)):
        tl.penup()
        tl.setposition(liste_mauvais_tir[i][0] * 50,
                           liste_mauvais_tir[i][1] * 50)
        tl.pendown()
        tl.dot(30, "black")
