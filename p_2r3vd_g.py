#!/usr/bin/env python3
# p_2r3vd_g.py

def calculer_coulissant_2r3vd_g(choix, L):
    """
    Version optimisée du drainage pour un coulissant 2 rails 3 vantaux dépendants.
    Côté gauche (Choix 3). Appelé directement par main.py.
    """
    # 1. Initialisation des points de départ de calcul
    p_1a = 160
    p_2a_1 = (L / 3) - 6 + 80
    p_2a_2 = (L / 3) - 6 + (L / 3) - 41.5 + 80

    # 2. Configuration des cas selon la longueur L
    if L < 3000:
        nbr_1a, nbr_2a_1, nbr_2a_2 = 2, 3, 3
        axe_1a = (L / 3) - 6 - 80 - 160
        axe_2a_1 = ((L / 3) - 41.5 - 80 - 80) / 2
        axe_2a_2 = ((L / 3) + 47.5 - 80 - 160) / 2
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: 160\nD3->D4: {c}\nD4->D5: {c}\nD5->D6: 160\nD6->D7; {d}\nD7->D8: {d}")

    elif 3000 <= L <= 4500:
        nbr_1a, nbr_2a_1, nbr_2a_2 = 3, 5, 5
        axe_1a = ((L / 3) - 6 - 80 - 160) / 2
        axe_2a_1 = ((L / 3) - 41.5 - 80 - 80) / 4
        axe_2a_2 = ((L / 3) + 47.5 - 80 - 160) / 4
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: {b}\nD3->D4: 160\nD4->D5: {c}\nD5->D6: {c}\nD6->D7; {c}\nD7->D8: {c}\nD8->D9: 160\nD9->D10: {d}\nD10->D11: {d}\nD11->D12: {d}\nD12->D13: {d}")

    else:  # L > 4500
        nbr_1a, nbr_2a_1, nbr_2a_2 = 4, 6, 6
        axe_1a = ((L / 3) - 6 - 80 - 160) / 3
        axe_2a_1 = ((L / 3) - 41.5 - 80 - 80) / 5
        axe_2a_2 = ((L / 3) + 47.5 - 80 - 160) / 5
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: {b}\nD3->D4: {b}\nD4->D5: 160\nD5->D6: {c}\nD6->D7; {c}\nD7->D8: {c}\nD8->D9: {c}\nD9->D10: {c}\nD10->D11: 160\nD11->D12: {d}\nD12->D13: {d}\nD13->D14: {d}\nD14->D15: {d}\nD15->D16: {d}")

    # 3. Affichage du résumé technique centralisé
    print("--------------------------------")
    print(f"Nombre de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a)}")
    print(f"Nombre de drainage 2a: {nbr_2a_1} - Entre-axe des premiers 2a: {round(axe_2a_1)}")
    print(f"Nombre de drainage 2a: {nbr_2a_2} - Entre-axe des derniers 2a: {round(axe_2a_2)}")
    print("--------------------------------")

    # 4. Facteurs de calcul centralisés
    nbrdrainage = 1

    # Boucle 1 : Calcul pour la partie gauche de la traverse = 1a
    nbr1a = 1
    limite_1a = (L / 3) + 47.5 if L < 3000 else (L / 3) - 6
    while p_1a <= limite_1a and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1

    # Boucle 2 : Calcul pour la partie centrale = 2a
    nbr2a = 1
    while p_2a_1 < L - (L / 3) + 47.5 and nbr2a <= nbr_2a_1:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a_1)}")
        p_2a_1 += axe_2a_1
        nbr2a += 1
        nbrdrainage += 1

    # Boucle 3 : Calcul pour la partie droite = 2a
    nbr2a = 1
    while p_2a_2 < L - 158 and nbr2a <= nbr_2a_2:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a_2)}")
        p_2a_2 += axe_2a_2
        nbr2a += 1
        nbrdrainage += 1

    # 5. Affichage des cotations non cumulées
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_1a, 2), round(axe_2a_1, 2), round(axe_2a_2, 2))


# Bloc de test solo
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 3 Optimisé) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_2r3vd_g(choix=3, L=test_L)
