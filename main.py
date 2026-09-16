#!/usr/bin/env python3
# main.py

# 1. Importation des fonctions de calcul depuis chaque script
try:
    from p_2r2v_g import calculer_coulissant_2r2v_g    # Choix 1
    from p_2r2v_d import calculer_coulissant_2r2v_d    # Choix 2
    from p_2r3vd_g import calculer_coulissant_2r3vd_g  # Choix 3
    from p_2r3vd_d import calculer_coulissant_2r3vd_d  # Choix 4
    from p_2r3vi import calculer_coulissant_2r3vi      # Choix 5
    from p_3r3v_g import calculer_coulissant_3r3v_g    # Choix 6
    from p_3r3v_d import calculer_coulissant_3r3v_d    # Choix 7
except ImportError as e:
    print(f"⚠️ Erreur d'importation : Un des fichiers de calcul est manquant.\nDétail : {e}")

def afficher_menu():
    """Affiche le menu de sélection des coulissants Technal"""
    print("\n=================== CONFIGURATEUR TECHNAL ===================")
    print("Valable pour les coulissants Technal")
    print("Choix 1: 2 rails, 2 vantaux, vantail extérieur à gauche")
    print("Choix 2: 2 rails, 2 vantaux, vantail extérieur à droite")
    print("----------------------------------------------------------------")
    print("Choix 3: 2 rails, 3 vantaux dépendants, vantail extérieur à gauche")
    print("Choix 4: 2 rails, 3 vantaux dépendants, vantail extérieur à droite")
    print("----------------------------------------------------------------")
    print("Choix 5: 2 rails, 3 vantaux indépendants, vantail extérieur au milieu")
    print("----------------------------------------------------------------")
    print("Choix 6: 3 rails, 3 vantaux, vantail extérieur à gauche")
    print("Choix 7: 3 rails, 3 vantaux, vantail extérieur à droite")
    print("================================================================")

def main():
    afficher_menu()
    
    # Saisie sécurisée des données utilisateur
    try:
        choix = int(input("Choisir le type de coulissant (1 à 7) : "))
        if choix < 1 or choix > 7:
            print("❌ Erreur : Le choix doit être compris entre 1 et 7.")
            return
            
        L = int(input("Indiquer la longueur de la Traverse (en mm) : "))
        if L <= 0:
            print("❌ Erreur : La longueur doit être un nombre positif.")
            return
            
    except ValueError:
        print("❌ Erreur : Veuillez entrer un nombre entier valide.")
        return

    print(f"\nLancement du calcul pour le Choix {choix} (Traverse L = {L} mm)...")

    # 2. Structure d'aiguillage (Match/Case disponible depuis Python 3.10)
    match choix:
        case 1:
            calculer_coulissant_2r2v_g(choix, L)
        case 2:
            calculer_coulissant_2r2v_d(choix, L)
        case 3:
            calculer_coulissant_2r3vd_g(choix, L)
        case 4:
            calculer_coulissant_2r3vd_d(choix, L)
        case 5:
            calculer_coulissant_2r3vi(choix, L)
        case 6:
            calculer_coulissant_3r3v_g(choix, L)
        case 7:
            calculer_coulissant_3r3v_d(choix, L)
        case _:
            print("Option non reconnue.")

if __name__ == "__main__":
    main()
