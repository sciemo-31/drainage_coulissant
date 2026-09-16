#!/usr/bin/env python3
# p_3r3v_d.py

def calculer_coulissant_3r3v_d(choix, L):
    """
    Version optimisée du drainage pour un coulissant 3 rails 3 vantaux.
    Vantail extérieur à droite (Choix 7). Appelé directement par main.py.
    """
    # 1. Initialisation des points de départ de calcul
    p_1a = 160
    p_2a = (L / 3) + 29.5 + 80
    p_3a = (L / 3) + 29.5 + (L / 3) - 59 + 80

    # 2. Configuration des cas selon la longueur L (Seuils spécifiques à 4000 et 6000)
    if L < 4000:
        nbr_1a, nbr_2a, nbr_3a = 3, 4, 4
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 2
        axe_2a = ((L / 3) - 59 - 80 - 80) / 3
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 3
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {d}\nD2->D3: {d}\nD3->D4: {d}\nD4->D5: 160\nD5->D6: {c}\nD6->D7: {c}\nD7->D8: {c}\nD8->D9: 160\nD9->D10: {b}\nD10->D11: {b}")

    elif 4000 <= L <= 6000:
        nbr_1a, nbr_2a, nbr_3a = 4, 5, 5
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 3
        axe_2a = ((L / 3) - 59 - 80 - 80) / 4
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 4
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {d}\nD2->D3: {d}\nD3->D4: {d}\nD4->D5: {d}\nD5->D6: 160\nD6->D7: {c}\nD7->D8: {c}\nD8->D9: {c}\nD9->D10: {c}\nD10->D11: 160\nD11->D12: {b}\nD12->D13: {b}\nD13->D14: {b}")

    else:  # L > 6000
        nbr_1a, nbr_2a, nbr_3a = 5, 6, 6
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 4
        axe_2a = ((L / 3) - 59 - 80 - 80) / 5
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 5
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {d}\nD2->D3: {d}\nD3->D4: {d}\nD4->D5: {d}\nD5->D6: {d}\nD6->D7: 160\nD7->D8: {c}\nD8->D9: {c}\nD9->D10: {c}\nD10->D11: {c}\nD11->D12: {c}\nD12->D13: 160\nD13->D14: {b}\nD14->D15: {b}\nD15->D16: {b}\nD16->D17: {b}")

    # 3. Affichage du résumé technique unique
    print("--------------------------------")
    print(f"Nombre de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a)}")
    print(f"Nombre de drainage 2a: {nbr_2a} - Entre-axe des 2a: {round(axe_2a)}")
    print(f"Nombre de drainage 3a: {nbr_3a} - Entre-axe des 3a: {round(axe_3a)}")
    print("--------------------------------")

    # 4. Facteurs de calcul centralisés
    nbrdrainage = 1

    # Boucle 1 : Calcul pour la partie gauche de la traverse = 1a
    nbr1a = 1
    while p_1a <= (L / 3) + 29.5 and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1

    # Boucle 2 : Calcul pour la partie centrale de la traverse pour les 2a
    nbr2a = 1
    while p_2a < (L / 3) + 29.5 + (L / 3) - 59 and nbr2a <= nbr_2a:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a)}")
        p_2a += axe_2a
        nbr2a += 1
        nbrdrainage += 1

    # Boucle 3 : Calcul pour la partie droite de la traverse = 3a
    nbr3a = 1
    while p_3a < L - 158 and nbr3a <= nbr_3a:
        print(f"Drainage n° {nbrdrainage} => 3a : {round(p_3a)}")
        p_3a += axe_3a
        nbr3a += 1
        nbrdrainage += 1

    # 5. Affichage des cotations non cumulées
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_1a, 2), round(axe_2a, 2), round(axe_3a, 2))


# Bloc de test autonome si exécuté directement
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 7 Optimisé) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_3r3v_d(choix=7, L=test_L)
