#!/usr/bin/env python3
# p_2r2v_g.py (Valable aussi pour p_2r2v_d.py)

def calculer_coulissant_2r2v_g(choix, L):
    """
    Version optimisée du drainage pour un coulissant 2 rails 2 vantaux.
    Choix 1 (Gauche) ou Choix 2 (Droite). Appelé directement par main.py.
    """
    # 1. Initialisation des points de départ de calcul
    p_1a = 160
    p_2a = (L / 2) + 80

    # 2. Configuration des cas selon la longueur L (Seuils spécifiques à 2000 et 3000)
    if L <= 2000:
        nbr_1a, nbr_2a = 2, 3
        axe_1a = (L / 2) - 80 - 160
        axe_2a = ((L / 2) - 80 - 160) / 2
        
        def afficher_cotation(b, d):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: 160 \nD3->D4: {d} \nD4->D5: {d}")

    elif 2000 < L <= 3000:
        nbr_1a, nbr_2a = 3, 5
        axe_1a = ((L / 2) - 80 - 160) / 2
        axe_2a = ((L / 2) - 80 - 160) / 4
        
        def afficher_cotation(b, d):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: {b} \nD3->D4: 160 \nD4->D5: {d} \nD5->D6: {d} \nD6->D7: {d} \nD7->D8: {d}")

    else:  # L > 3000
        nbr_1a, nbr_2a = 4, 6
        axe_1a = ((L / 2) - 80 - 160) / 3
        axe_2a = ((L / 2) - 80 - 160) / 5
        
        def afficher_cotation(b, d):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: {b} \nD3->D4: {b} \nD4->D5: 160 \nD5->D6: {d} \nD6->D7: {d} \nD7->D8: {d} \nD8->D9: {d} \nD9->D10: {d}")

    # 3. Affichage du résumé technique unique
    print("--------------------------------")
    print(f"Nbr de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a, 2)}")
    print(f"Nbr de drainage 2a: {nbr_2a} - Entre-axe 2a: {round(axe_2a, 2)}")
    print("--------------------------------")
    
    nbrdrainage = 1
    
    # 4. Boucle de calcul centralisée pour les 1a
    nbr1a = 1
    while p_1a <= L / 2 and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a, 2)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1
        
    # 5. Boucle de calcul centralisée pour les 2a
    nbr2a = 1
    while p_2a <= L - 150 and nbr2a <= nbr_2a:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a, 2)}")
        p_2a += axe_2a
        nbr2a += 1
        nbrdrainage += 1
        
    # 6. Affichage final des cotations non cumulées
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_1a, 2), round(axe_2a, 2))


# Bloc de test autonome si exécuté directement
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 1/2) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_2r2v_g(choix=1, L=test_L)
