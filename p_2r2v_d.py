#!/usr/bin/env python3
# p_2r2v_d.py

def calculer_coulissant_2r2v_d(choix, L):
    """
    Version optimisée du drainage pour un coulissant 2 rails 2 vantaux.
    Vantail extérieur à droite (Choix 2). Appelé directement par main.py.
    """
    # 1. Initialisation des points de départ de calcul
    p_2a = 160
    p_1a = (L / 2) + 80

    # 2. Configuration des cas selon la longueur L (Seuils à 2000 et 3000)
    if L <= 2000:
        nbr_2a, nbr_1a = 3, 2
        axe_2a = ((L / 2) - 80 - 160) / 2
        axe_1a = ((L / 2) - 80 - 160)
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: {b} \nD3->D4: 160 \nD4->D5: {c}")

    elif 2000 < L <= 3000:
        nbr_2a, nbr_1a = 5, 3
        axe_2a = ((L / 2) - 80 - 160) / 4
        axe_1a = ((L / 2) - 80 - 160) / 2
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: {b} \nD3->D4: {b} \nD4->D5: {b} \nD5->D6: 160 \nD6->D7: {c} \nD7->D8: {c}")

    else:  # L > 3000
        nbr_2a, nbr_1a = 6, 4
        axe_2a = ((L / 2) - 80 - 160) / 5
        axe_1a = ((L / 2) - 80 - 160) / 3
        
        def afficher_cotation(b, c):
            print(f"=>D1: 160 \nD1->D2: {b} \nD2->D3: {b} \nD3->D4: {b} \nD4->D5: {b} \nD5->D6: {b} \nD6->D7: 160 \nD7->D8: {c} \nD8->D9: {c} \nD9->D10: {c}")

    # 3. Affichage du résumé technique unique
    print("--------------------------------")
    print(f"Nbr de drainage 2a: {nbr_2a} - Entre-axe 2a: {round(axe_2a, 2)}")
    print(f"Nbr de drainage 1a: {nbr_1a} - Entre-axe 1a: {round(axe_1a, 2)}")
    print("--------------------------------")
    
    nbrdrainage = 1
    
    # 4. Boucle de calcul centralisée pour les 2a
    nbr2a = 1
    while p_2a <= L / 2 and nbr2a <= nbr_2a:
        print(f"Drainage n° {nbrdrainage} => 2a : {round(p_2a)}")
        p_2a += axe_2a
        nbr2a += 1
        nbrdrainage += 1
        
    # 5. Boucle de calcul centralisée pour les 1a
    nbr1a = 1
    while p_1a <= L - 150 and nbr1a <= nbr_1a:
        print(f"Drainage n° {nbrdrainage} => 1a : {round(p_1a)}")
        p_1a += axe_1a
        nbr1a += 1
        nbrdrainage += 1
        
    # 6. Affichage final des cotations non cumulées
    print("--------------------------------")
    print("Cotation non cumulée")
    afficher_cotation(round(axe_2a, 2), round(axe_1a, 2))


# Bloc de test autonome si exécuté directement
if __name__ == "__main__":
    print("--- MODE TEST SOLO (Choix 2 Optimisé) ---")
    test_L = int(input("Entrez une longueur de traverse (mm) : "))
    calculer_coulissant_2r2v_d(choix=2, L=test_L)
