import turtle as tl
import fonctions as fn

# fenêtre turtle
tl.setup(800, 800, 100, 100)
tl.bgcolor("#adc2eb")
tl.title("Bataille navale")
tl.hideturtle()
tl.bgpic("fond_ecran.png")
tl.update()

"""
# création du background avant d'effectuer une capture écran
# axe des abscisses
tl.penup()
tl.goto(-400, 0)
tl.pendown()
tl.forward(tl.window_width())

# axe des ordonnées
tl.penup()
tl.goto(0, -400)
tl.setheading(90)
tl.pendown()
tl.forward(tl.window_width())

# axes horizontaux
tl.penup()
tl.pencolor("blue")
tl.goto(-400, -150)
tl.setheading(0)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-400, -100)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-400, -50)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-400, 50)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-400, 100)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-400, 150)
tl.pendown()
tl.forward(tl.window_width())

# axes verticaux
tl.penup()
tl.goto(-150, -400)
tl.setheading(90)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-100, -400)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(-50, -400)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(50, -400)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(100, -400)
tl.pendown()
tl.forward(tl.window_width())

tl.penup()
tl.goto(150, -400)
tl.pendown()
tl.forward(tl.window_width())

# 1er cercle
tl.penup()
tl.pencolor("red")
tl.goto(0, -50)
tl.setheading(0)
tl.pendown()
tl.circle(50)

# 2ème cercle
tl.penup()
tl.goto(0, -100)
tl.pendown()
tl.circle(100)

# 3ème cercle
tl.penup()
tl.goto(0, -150)
tl.pendown()
tl.circle(150)
tl.penup()
"""

print("\n############################")
print("      BATAILLE NAVALE")
print("############################\n")

print("Vous allez placer 3 bateaux dans l'océan indien. Vous devez choisir la position de chaque bateau, en indiquant les coordonnées de la proue."
      " Chaque bateau sera représenté Verticalement ou Horizontalement. L'ordinateur va "
      "également positionner 3 bateaux dans l'océan indien, et il vous faudra trouver leurs coordonnées à l'aide d'obus."
      " Vous disposez au total de 20 obus.")

# we initialize the scores of player one and the computer
score_ordinateur = 0
score_joueur = 0

# we initialize the list of coordinates of player one's hits
liste_bon_tir_joueur = []
liste_mauvais_tir_joueur = []
liste_touche_bateaux_joueur = [0, 0, 0]

# we initialize the list of coordinates of the computer's hits
liste_bon_tir_ordinateur = []
liste_mauvais_tir_ordinateur = []
liste_touche_bateaux_ordinateur = [0, 0, 0]

# we define positions for the 3 computer's boats
liste_coordonnees_bateaux_ordinateur = fn.definir_position_bateaux_ordinateur()

# development mode
# for i in range(3):
    # fn.afficher_bateau(liste_coordonnees_bateaux_ordinateur[i])

# we define positions for the 3 player's boats and show them
liste_coordonnees_bateaux_joueur = [[], [], []]
for i in range(3):
    print("\n=== Vous allez définir la position de votre bateau numéro", i + 1, "===")
    liste_coordonnees_bateaux_joueur[i] = fn.definir_position_bateau_joueur()

for i in range(3):
    fn.afficher_bateau(liste_coordonnees_bateaux_joueur[i])

# the game lasts 20 hits
for i in range(20):
    # we ask player one the coordinates of the next hit
    (xtir, ytir) = fn.demander_joueur_position_tir()

    # player one hits and we print the results
    (score_joueur, liste_bon_tir_joueur, liste_mauvais_tir_joueur, liste_touche_bateaux_ordinateur, liste_touche_bateaux_joueur) = \
        fn.joueur_tire(xtir, ytir, score_joueur, liste_bon_tir_joueur, liste_mauvais_tir_joueur, liste_coordonnees_bateaux_ordinateur, liste_touche_bateaux_ordinateur, liste_coordonnees_bateaux_joueur, liste_touche_bateaux_joueur)
    fn.afficher_resultats_tir_joueur(score_joueur, liste_bon_tir_joueur, liste_mauvais_tir_joueur)

    # the compute hits and we print the results
    (score_ordinateur, liste_bon_tir_ordinateur, liste_mauvais_tir_ordinateur, liste_touche_bateaux_joueur, liste_touche_bateaux_ordinateur) = \
        fn.ordinateur_tire(score_ordinateur, liste_bon_tir_ordinateur, liste_mauvais_tir_ordinateur, liste_coordonnees_bateaux_joueur, liste_touche_bateaux_joueur, liste_coordonnees_bateaux_ordinateur, liste_touche_bateaux_ordinateur)
    fn.afficher_resultats_tir_ordinateur(score_ordinateur, liste_bon_tir_ordinateur, liste_mauvais_tir_ordinateur)

# final scores
print("\n############################")
print("           RESULTATS")
print("############################\n")
fn.afficher_resultats_tir_joueur(score_joueur, liste_bon_tir_joueur, liste_mauvais_tir_joueur)
fn.afficher_resultats_tir_ordinateur(score_ordinateur, liste_bon_tir_ordinateur, liste_mauvais_tir_ordinateur)

# we close the turtle window
tl.exitonclick()
