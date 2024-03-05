import random

def afficher_grille(grille):
    """Affiche la grille de jeu."""
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * (4 * len(ligne) - 1))

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

def choisir_pion():
    """Permet au joueur de choisir son pion."""
    print("Choisissez votre pion :")
    choix = input("Tapez '1' pour l'étoile ou '2' pour le cœur : ").upper()
    while choix not in ['1', '2']:
        print("Choix invalide. Veuillez choisir entre l'étoile (1) et le cœur (2).")
        choix = input("Tapez '1' pour l'étoile ou '2' pour le cœur : ").upper()
    
    if choix == '1':
        print("Vous avez choisi l'étoile ⭐️.")
        return '⭐️', '❤️'
    else:
        print("Vous avez choisi le cœur ❤️.")
        return '❤️', '⭐️'

def tour_joueur(grille, symbole_joueur):
    """Gère le tour du joueur."""
    print("A vous de jouer")
    while True:
        colonne = int(input("Saisissez une colonne (0, 1, 2, ...) : "))
        ligne = int(input("Saisissez une ligne (0, 1, 2, ...) : "))
        if grille[ligne][colonne] == " ":
            poser_pion(grille, symbole_joueur, ligne, colonne)
            return
        else:
            print("Case occupée, veuillez choisir une autre case.")

def tour_ordi_facile(grille, symbole_ordi):
    """Gère le tour de l'ordinateur pour le niveau facile."""
    print("Au Tour de l'ordinateur")
    taille = len(grille)
    while True:
        colonne = random.randint(0, taille - 1)
        ligne = random.randint(0, taille - 1)
        if grille[ligne][colonne] == " ":
            poser_pion(grille, symbole_ordi, ligne, colonne)
            return

def tour_ordi_moyen(grille, symbole_ordi):
    """Gère le tour de l'ordinateur pour le niveau moyen."""
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = symbole_ordi
                if verifier_victoire(grille, symbole_ordi):
                    return
                else:
                    grille[i][j] = " "
    tour_ordi_facile(grille, symbole_ordi)

def jouer_coup_gagnant(grille, symbole_ordi):
    """Vérifie si l'ordinateur peut gagner en un coup et joue ce coup."""
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = symbole_ordi
                if verifier_victoire(grille, symbole_ordi):
                    return True
                grille[i][j] = " "
    return False

def bloquer_joueur(grille, symbole_ordi, symbole_joueur):
    """Vérifie si le joueur peut gagner en un coup et bloque ce coup."""
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = symbole_joueur
                if verifier_victoire(grille, symbole_joueur):
                    grille[i][j] = symbole_ordi
                    return True
                grille[i][j] = " "
    return False

def tour_ordi_difficile(grille, symbole_ordi, symbole_joueur):
    """Gère le tour de l'ordinateur pour le niveau difficile."""
    # Vérifier si l'ordinateur peut gagner au prochain coup
    if jouer_coup_gagnant(grille, symbole_ordi):
        return
    # Vérifier si l'ordinateur doit bloquer le joueur
    if bloquer_joueur(grille, symbole_ordi, symbole_joueur):
        return
    # Si aucune des situations ci-dessus ne se produit, jouer de manière stratégique
    tour_ordi_moyen(grille, symbole_ordi)

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
        taille = int(input("Choisissez la taille de la grille (par exemple, 3 pour une grille de 3x3) : "))
        symbole_joueur, symbole_ordi = choisir_pion()
        niveau = creer_grille(taille)
        niveau_difficulte = int(input("Choisissez le niveau de difficulté du jeu (1: Facile, 2: Moyen, 3: Difficile) : "))
        tour = 0


        while True:
            afficher_grille(niveau)
            if tour % 2 == 0:
                tour_joueur(niveau, symbole_joueur)
                if verifier_victoire(niveau, symbole_joueur):
                    afficher_grille(niveau)
                    print("Vous avez remporté la partie. Félicitations !")
                    break
            else:
                if niveau_difficulte == 1:
                    tour_ordi_facile(niveau, symbole_ordi)
                elif niveau_difficulte == 2:
                    tour_ordi_moyen(niveau, symbole_ordi)
                elif niveau_difficulte == 3:
                    tour_ordi_difficile(niveau, symbole_ordi, symbole_joueur)
                

                if verifier_victoire(niveau, symbole_ordi):
                    afficher_grille(niveau)
                    print("On apprend peu par la victoire mais beaucoup par la défaite !")
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
