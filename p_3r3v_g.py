from choix import *

# Drainage 3 rails 3 vantaux: vantail extérieur à droite
# def cas1():
p_3a = 160
p_2a = (L/3)+29.5+80
p_1a = (L/3)+29.5+(L/3)-59+80

nbr_1a_c1 = 3
nbr_2a_c1 = 4
nbr_3a_c1 = 4
axe_1a_c1 = ((L/3)+29.5-160-80)/2
axe_2a_c1 = ((L/3)-59-80-80)/3
axe_3a_c1 = ((L/3)+29.5-160-80)/3

def cotation_c1():
    a = 160  # départ entre secteur
    b = round(axe_1a_c1, 2)  # entre-axe 1a partie gauche
    c = round(axe_2a_c1, 2)  # entre axe 2a partie centrale
    d = round(axe_3a_c1,2)   # entre axe 3a partie droite   
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", b, "\nD3->D4:", a,
          "\nD4->D5:", c, "\nD5->D6:", c, "\nD6->D7:", c, "\nD7->D8:", a, "\nD4->D5:", d, "\nD5->D6:", d, "\nD6->D7:", d)

# def cas2():
nbr_1a_c2 = 4
nbr_2a_c2 = 5
nbr_3a_c2 = 5
axe_1a_c2 = ((L/3)+29.5-160-80)/3
axe_2a_c2 = ((L/3)-59-80-80)/4
axe_3a_c2 = ((L/3)+29.5-160-80)/4

def cotation_c2():
    a = 160  # départ entre secteur
    b = round(axe_1a_c2, 2)  # entre-axe 1a partie gauche
    c = round(axe_2a_c2, 2)  # entre axe 2a partie centrale
    d = round(axe_3a_c2, 2)   # entre axe 3a partie droite
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", b, "\nD3->D4:", b,
          "\nD4->D5:", a, "\nD5->D6:", c, "\nD6->D7:", c, "\nD7->D8:", c, "\nD8->D9:", c,
            "\nD9->D10:", a, "\nD10->D11:", d, "\nD11->D12:", d, "\nD12->D13:", d, "\nD13->D14:", d)

# def cas3():
nbr_1a_c3 = 5
nbr_2a_c3 = 6
nbr_3a_c3 = 6
axe_1a_c3 = ((L/3)+29.5-160-80)/4
axe_2a_c3 = ((L/3)-59-80-80)/5
axe_3a_c3 = ((L/3)+29.5-160-80)/5

def cotation_c3():
    a = 160  # départ entre secteur
    b = round(axe_1a_c3, 2)  # entre-axe 1a partie gauche
    c = round(axe_2a_c3, 2)  # entre axe 2a partie centrale
    d = round(axe_3a_c3, 2)   # entre axe 3a partie droite
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", b, "\nD3->D4:", b,
          "\nD4->D5:", b, "\nD5->D6:", a, "\nD6->D7:", c, "\nD7->D8:", c, "\nD8->D9:", c,
          "\nD9->D10:", c, "\nD10->D11:", c, "\nD11->D12:", a, "\nD12->D13:", d, "\nD13->D14:", d, "\nD14->D15:", d, "\nD15>D16:", d, "\nD16->D17:", d)


if choix == 6 and L < 4000:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c1) +
          " - Entre-axe 1a: ", round(axe_1a_c1))
    print("Nombre de drainage 2a: " + str(nbr_2a_c1) +
          " - Entre-axe des 2a: ",  round(axe_2a_c1))
    print("Nombre de drainage 3a: " + str(nbr_3a_c1) +
          " - Entre-axe des 3a: ", round(axe_3a_c1))
    print("--------------------------------")
    # calcul pour la partie gauche de la traverse = 3a
    nbrdrainage = 1
    nbr3a = 1
    while p_3a <= (L/3)+29.5 and nbr3a <= nbr_3a_c1:
        print("Drainage n°", nbrdrainage, "=> 3a :", round(p_3a))
        p_3a = p_3a + axe_3a_c1
        nbr3a += 1
        nbrdrainage += 1
    # calcul pour la partie centrale de la traverse pour les 2a
    nbr2a = 1
    while p_2a < (L/3)+29.5 + (L/3)-59 and nbr2a <= nbr_2a_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c1
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour la partie droite de la traverse = 1a
    nbr1a = 1
    while p_1a < L - 158 and nbr1a <= nbr_1a_c1:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c1
        nbr1a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c1()


elif choix == 6 and 4000 <= L <= 6000:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c2) +
          " - Entre-axe 1a: ", round(axe_1a_c2))
    print("Nombre de drainage 2a: " + str(nbr_2a_c2) +
          " - Entre-axe 2a: ", round(axe_2a_c2))
    print("Nombre de drainage 3a: " + str(nbr_3a_c2) +
          " - Entre-axe 3a: ", round(axe_3a_c2))
    print("--------------------------------")
# calcul pour la partie gauche de la traverse = 3a
    nbrdrainage = 1
    nbr3a = 1
    while p_3a <= (L/3)+29.5 and nbr3a <= nbr_3a_c2:
        print("Drainage n°", nbrdrainage, "=> 3a :", round(p_3a))
        p_3a = p_3a + axe_3a_c2
        nbr3a += 1
        nbrdrainage += 1
# calcul pour la partie centrale de la traverse pour les 2a
    nbr2a = 1
    while p_2a < (L/3)+29.5 + (L/3)-59 and nbr2a <= nbr_2a_c2:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c2
        nbr2a += 1
        nbrdrainage += 1
# calcul pour la partie droite de la traverse = 1a
    nbr1a = 1
    while p_1a < L-158 and nbr1a <= nbr_1a_c2:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c2
        nbr1a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c2()


elif choix == 6 and L > 6000:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c3) +
          " - Entre-axe 1a: ", round(axe_1a_c3))
    print("Nombre de drainage 2a: " + str(nbr_2a_c3) +
          " - Entre-axe 2a: ", round(axe_2a_c3))
    print("Nombre de drainage 3a: " + str(nbr_3a_c3) +
          " - Entre-axe 3a: ", round(axe_3a_c3))
    print("--------------------------------")
# calcul pour la partie gauche de la traverse = 3a
    nbrdrainage = 1
    nbr3a = 1
    while p_3a <= (L/3)+29.5 and nbr3a <= nbr_3a_c3:
        print("Drainage n°", nbrdrainage, "=> 3a :", round(p_3a))
        p_3a = p_3a + axe_3a_c3
        nbr3a += 1
        nbrdrainage += 1
# calcul pour la partie centrale de la traverse pour les 2a
    nbr2a = 1
    while p_2a < (L/3)+29.5 + (L/3)-59 and nbr2a <= nbr_2a_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c3
        nbr2a += 1
        nbrdrainage += 1
# calcul pour la partie droite de la traverse = 1a
    nbr1a = 1
    while p_1a < L-158 and nbr1a <= nbr_1a_c3:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c3
        nbr1a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c3()
