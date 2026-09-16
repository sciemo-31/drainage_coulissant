#!/usr/bin/env python3
# p_2r3vi.py

def calculer_coulissant_2r3vi(choix, L):
    """
    Version optimisée du drainage pour un coulissant 2 rails 3 vantaux indépendants.
    Vantail extérieur au milieu (Choix 5). Appelé directement par main.py.
    """
    # 1. Initialisation des points de départ de calcul
    p_2a_1 = 160
    p_2a_2 = (L / 3) + 29.5 + (L / 3) - 59 + 80
    p_1a = (L / 3) + 29.5 + 80

    # 2. Configuration des cas selon la longueur L
    if L < 3000:
        nbr_1a, nbr_2a_1, nbr_2a_2 = 2, 3, 3
        axe_1a = (L / 3) - 59 - 80 - 80
        axe_2a_1 = ((L / 3) + 29.5 - 160 - 80) / 2
        axe_2a_2 = ((L / 3) + 29.5 - 160 - 80) / 2
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160\nD1->D2: {c}\nD2->D3: {c}\nD3->D4: 160\nD4->D5: {b}\nD5->D6: 160\nD6->D7: {c}\nD7->D8: {c}")

    elif 3000 <= L <= 4500:
        nbr_1a, nbr_2a_1, nbr_2a_2 = 3, 5, 5
        axe_1a = ((L / 3) - 59 - 80 - 80) / 2
        axe_2a_1 = ((L / 3) + 29.5 - 160 - 80) / 4
        axe_2a_2 = ((L / 3) + 29.5 - 160 - 80) / 4
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160\nD1->D2: {c}\nD2->D3: {c}\nD3->D4: {c}\nD4->D5: {c}\nD5->D6: 160\nD6->D7: {b}\nD7->D8: {b}\nD8->D9: 160\nD9->D10: {c}\nD10->D11: {c}\nD11->D12: {c}\nD12->D13: {c}")

    else:  # L > 4500
        nbr_1a, nbr_2a_1, nbr_2a_2 = 4, 6, 6
        axe_1a = ((L / 3) - 59 - 80 - 80) / 3
        axe_2a_1 = ((L / 3) + 29.5 - 160 - 80) / 5
        axe_2a_2 = ((L / 3) + 29.5 - 160 - 80) / 5
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160\nD1->D2: {c}\nD2->D3: {c}\nD3->D4: {c}\nD4->D5: {c}\nD5->D6: {c}\nD6->D7: 160\nD7->D8: {b}\nD8->D9: {b}\nD9->D10: {b}\nD10->D11: 160\nD11->D12: {c}\nD12->D13: {c}\nD13->D14: {c}\nD14->D15: {c}\nD15->D16: {c}")

    # 3. Affichage du résumé technique centralisé
    print("--------------------------------")
    print(f"Nombre de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a)}")
    print(f"Nombre de drainage 2a: {nbr_2a_1} - Entre-axe des 3 premiers 2a: {round(axe_2a_1)}")
    print(f"Nombre de drainage 2a: {nbr_2a_2} - Entre-axe des 3 derniers 2a: {round(axe_2a_2)}")
    print("--------------------------------")

    nbrdrainage = 1

    # Boucle 1 : Calcul pour la partie gauche de la traverse = 2a
    nbr2a = 1
    while p_2a_1 <= (L / 3) + 29.5 and nbr2a <= nbr_2a_1:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a_1)}")
        p_2a_1 += axe_2a_1
        nbr2a += 1
        nbrdrainage += 1

    # Boucle 2 : Calcul pour la partie centrale de la traverse = 1a
    nbr1a = 1
    while p_1a < (L / 3) + 29.5 + (L / 3) - 59 and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1

    # Boucle 3 : Calcul pour la partie droite de la traverse = 2a
    nbr2a = 1
    while p_2a_2 < L - 158 and nbr2a <= nbr_2a_2:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a_2)}")
        p_2a_2 += axe_2a_2
        nbr2a += 1
        nbrdrainage += 1

    # 4. Affichage des cotations non cumulées
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_1a, 2), round(axe_2a_1, 2))


# Bloc de test solo
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 5 Optimisé) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_2r3vi(choix=5, L=test_L)
