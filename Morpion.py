import random

def afficher_grille(grille):
    """Affiche la grille de jeu."""
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 10)

def creer_grille(taille):
    """Crée une grille de jeu vide."""
    grille = []
    for _ in range(taille):
        ligne = []
        for _ in range(taille):
            ligne.append(" ")
        grille.append(ligne)
    return grille

def poser_pion(grille, symbole, ligne, colonne):
    """Place un pion à l'emplacement spécifié sur la grille."""
    grille[ligne][colonne] = symbole

def verifier_victoire(grille, symbole):
    """Vérifie si le joueur a gagné."""
    taille = len(grille)
    # Vérification des lignes
    for ligne in grille:
        if all(pion == symbole for pion in ligne):
            return True
    # Vérification des colonnes
    for i in range(taille):
        if all(grille[j][i] == symbole for j in range(taille)):
            return True
    # Vérification des diagonales
    if all(grille[i][i] == symbole for i in range(taille)) or \
       all(grille[i][taille-1-i] == symbole for i in range(taille)):
        return True
    return False

def tour_joueur(grille, joueur):
    """Gère le tour du joueur."""
    print("Tour du joueur", joueur)
    while True:
        colonne = int(input("Saisir une colonne (0, 1, 2) : "))
        ligne = int(input("Saisir une ligne (0, 1, 2) : "))
        if grille[ligne][colonne] == " ":
            poser_pion(grille, joueur, ligne, colonne)
            return
        else:
            print("Case occupée, veuillez choisir une autre case.")

def tour_ordi(grille, symbole_ordi):
    """Gère le tour de l'ordinateur."""
    print("Tour de l'ordinateur")
    taille = len(grille)
    while True:
        colonne = random.randint(0, taille - 1)
        ligne = random.randint(0, taille - 1)
        if grille[ligne][colonne] == " ":
            poser_pion(grille, symbole_ordi, ligne, colonne)
            return

def recommencer():
    """Propose de recommencer le jeu."""
    while True:
        choix = input("Voulez-vous recommencer ? (oui/non) : ").lower()
        if choix == "oui":
            return True
        elif choix == "non":
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")

def morpion():
    """Fonction principale du jeu."""
    print("Bienvenue dans le Super Morpion !")
    while True:
        niveau = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        symboles = ['X', 'O']  # Symboles du joueur et de l'ordinateur
        symbole_ordi = 'O'  # Symbole de l'ordinateur
        tour = 0
        while True:
            afficher_grille(niveau)
            if tour % 2 == 0:
                tour_joueur(niveau, symboles[0])
                if verifier_victoire(niveau, symboles[0]):
                    afficher_grille(niveau)
                    print("Le joueur a gagné !")
                    break
            else:
                tour_ordi(niveau, symbole_ordi)
                if verifier_victoire(niveau, symbole_ordi):
                    afficher_grille(niveau)
                    print("L'ordinateur a gagné !")
                    break
            if all(pion != " " for ligne in niveau for pion in ligne):
                afficher_grille(niveau)
                print("Match nul !")
                break
            tour += 1
        if not recommencer():
            print("Merci d'avoir joué !")
            break

morpion()
