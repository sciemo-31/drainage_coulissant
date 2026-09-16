#!/usr/bin/env python3
# p_3r3v_g.py

def calculer_coulissant_3r3v_g(choix, L):
    """
    Version optimisée du drainage pour un coulissant 3 rails 3 vantaux.
    Vantail extérieur à gauche (Choix 6).
    """
    # 1. Initialisation des points de départ de calcul
    p_3a = 160
    p_2a = (L / 3) + 29.5 + 80
    p_1a = (L / 3) + 29.5 + (L / 3) - 59 + 80

    # 2. Détermination des axes et variables selon la longueur L
    if L < 4000:
        nbr_1a, nbr_2a, nbr_3a = 3, 4, 4
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 2
        axe_2a = ((L / 3) - 59 - 80 - 80) / 3
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 3
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: {b}\nD3->D4: 160\nD4->D5: {c}\nD5->D6: {c}\nD6->D7: {c}\nD7->D8: 160\nD8->D9: {d}\nD9->D10: {d}\nD10->D11: {d}")

    elif 4000 <= L <= 6000:
        nbr_1a, nbr_2a, nbr_3a = 4, 5, 5
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 3
        axe_2a = ((L / 3) - 59 - 80 - 80) / 4
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 4
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: {b}\nD3->D4: {b}\nD4->D5: 160\nD5->D6: {c}\nD6->D7: {c}\nD7->D8: {c}\nD8->D9: {c}\nD9->D10: 160\nD10->D11: {d}\nD11->D12: {d}\nD12->D13: {d}\nD13->D14: {d}")

    else:  # L > 6000
        nbr_1a, nbr_2a, nbr_3a = 5, 6, 6
        axe_1a = ((L / 3) + 29.5 - 160 - 80) / 4
        axe_2a = ((L / 3) - 59 - 80 - 80) / 5
        axe_3a = ((L / 3) + 29.5 - 160 - 80) / 5
        
        def afficher_cotation(b, c, d):
            print(f"=>D1: 160\nD1->D2: {b}\nD2->D3: {b}\nD3->D4: {b}\nD4->D5: {b}\nD5->D6: 160\nD6->D7: {c}\nD7->D8: {c}\nD8->D9: {c}\nD9->D10: {c}\nD10->D11: {c}\nD11->D12: 160\nD12->D13: {d}\nD13->D14: {d}\nD14->D15: {d}\nD15->D16: {d}\nD16->D17: {d}")

    # 3. Affichage du résumé technique unique
    print("--------------------------------")
    print(f"Nombre de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a)}")
    print(f"Nombre de drainage 2a: {nbr_2a} - Entre-axe des 2a: {round(axe_2a)}")
    print(f"Nombre de drainage 3a: {nbr_3a} - Entre-axe des 3a: {round(axe_3a)}")
    print("--------------------------------")

    # 4. Facteurs de calcul (les boucles ne sont écrites qu'une seule fois)
    nbrdrainage = 1

    # Partie gauche = 3a
    nbr3a = 1
    while p_3a <= (L / 3) + 29.5 and nbr3a <= nbr_3a:
        print(f"Drainage n° {nbrdrainage} => 3a : {round(p_3a)}")
        p_3a += axe_3a
        nbr3a += 1
        nbrdrainage += 1

    # Partie centrale = 2a
    nbr2a = 1
    while p_2a < (L / 3) + 29.5 + (L / 3) - 59 and nbr2a <= nbr_2a:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a)}")
        p_2a += axe_2a
        nbr2a += 1
        nbrdrainage += 1

    # Partie droite = 1a
    nbr1a = 1
    while p_1a < L - 158 and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1

    # 5. Affichage des cotations
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_1a, 2), round(axe_2a, 2), round(axe_3a, 2))


# Bloc de test autonome
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 6 Optimisé) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_3r3v_g(choix=6, L=test_L)
