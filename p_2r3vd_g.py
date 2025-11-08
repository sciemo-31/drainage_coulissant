from choix import *

# Drainage 2 rails 3 vantaux dépendants
# def cas1():
p_1a = 160
p_2a_1 = (L/3)-6+80
p_2a_2 = (L/3)-6+(L/3)-41.5+80

nbr_1a_c1 = 2
nbr_2a_1_c1 = 3
nbr_2a_2_c1 = 3
axe_1a_c1 = (L/3)-6-80-160
axe_2a_1_c1 = ((L/3)-41.5-80-80)/2 #entre axe 2a partie centrale
axe_2a_2_c1 = ((L/3)+47.5-80-160)/2

def cotation_c1():
    a = 160  # départ entre secteur
    b = round(axe_1a_c1, 2)  # entre-axe 1a
    c = round(axe_2a_1_c1, 2)  # entre axe 2a partie centrale
    d = round(axe_2a_2_c1, 2)
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", a, "\nD3->D4:", c,
          "\nD4->D5:", c, "\nD5->D6:", a, "\nD6->D7;", d, "\nD7->D8:", d)

# def cas2():
nbr_1a_c2 = 3
nbr_2a_1_c2 = 5
nbr_2a_2_c2 = 5
axe_1a_c2 = ((L/3)-6-80-160)/2
axe_2a_1_c2 = ((L/3)-41.5-80-80)/4  # entre axe 2a partie centrale
axe_2a_2_c2 = ((L/3)+47.5-80-160)/4


def cotation_c2():
    a = 160  # départ entre secteur
    b = round(axe_1a_c2, 2)  # entre-axe 1a
    c = round(axe_2a_1_c2, 2)  # entre axe 2a partie centrale
    d = round(axe_2a_2_c2, 2)
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", b, "\nD3->D4:", a,
          "\nD4->D5:", c, "\nD5->D6:", c, "\nD6->D7;", c, "\nD7->D8:", c,
          "\nD8->D9:",a,"\nD9->D10:",d,"\nD10->D11:",d,"\nD11->D12:",d,"\nD12->D13:",d)

# def cas3():
nbr_1a_c3 = 4
nbr_2a_1_c3 = 6
nbr_2a_2_c3 = 6
axe_1a_c3 = ((L/3)-6-80-160)/3
axe_2a_1_c3 = ((L/3)-41.5-80-80)/5  # entre axe 2a partie centrale
axe_2a_2_c3 = ((L/3)+47.5-80-160)/5 #entre-axe sur le coté

def cotation_c3():
    a = 160  # départ entre secteur
    b = round(axe_1a_c3, 2)  # entre-axe 1a
    c = round(axe_2a_1_c3, 2)  # entre axe 2a partie centrale
    d = round(axe_2a_2_c3, 2)   #entre-axe sur le coté
    
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:", b, "\nD3->D4:", b,
          "\nD4->D5:", a, "\nD5->D6:", c, "\nD6->D7;", c, "\nD7->D8:", c,
          "\nD8->D9:", c, "\nD9->D10:", c, "\nD10->D11:", a, "\nD11->D12:", d, "\nD12->D13:", d,
          "\nD13->D14:", d, "\nD14->D15:", d, "\nD15->D16:", d)


if choix == 3 and L < 3000:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c1) + " - Entre-axe 1a: ", round(axe_1a_c1))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c1)+
          " - Entre-axe des 3 premiers 2a: ",  round(axe_2a_1_c1))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c1) + " - Entre-axe des 3 derniers 2a: ", round(axe_2a_2_c1))
    print("--------------------------------")
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= (L/3)+47.5 and nbr1a <= nbr_1a_c1:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c1
        nbr1a += 1
        nbrdrainage += 1
    #calcul pour la partie central = 2a
    nbr2a = 1
    while p_2a_1 < L-(L/3)+47.5 and nbr2a <= nbr_2a_1_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c1
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour les 2a
    nbr2a = 1
    while p_2a_2 < L-158 and nbr2a <= nbr_2a_2_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_2))
        p_2a_2 = p_2a_2 + axe_2a_2_c1
        nbr2a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c1()

elif choix == 3 and 3000 <= L <= 4500:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c2) +
          " - Entre-axe 1a: ", round(axe_1a_c2))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c2) +
          " - Entre-axe 2a: ", round(axe_2a_1_c2))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c2) +
          " - Entre-axe 2a: ", round(axe_2a_2_c2))
    print("--------------------------------")
    #calcul pour la partie gauche de la traverse = 1a
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= (L/3)-6 and nbr1a <= nbr_1a_c2:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c2
        nbr1a += 1
        nbrdrainage += 1
    # calcul pour la partie central de la traverse = 2a
    nbr2a = 1
    while p_2a_1 < L-(L/3)+47.5 and nbr2a <= nbr_2a_1_c2:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c2
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour la partie droite de la traverse = 2a
    nbr2a = 1
    while p_2a_2 < L-158 and nbr2a <= nbr_2a_2_c2:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_2))
        p_2a_2 = p_2a_2 + axe_2a_2_c2
        nbr2a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c2()


elif choix == 3 and L > 4500:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c3) +
          " - Entre-axe 1a: ", round(axe_1a_c3))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c3) +
          " - Entre-axe 2a: ", round(axe_2a_1_c3))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c3) +
          " - Entre-axe 2a: ", round(axe_2a_2_c3))
    print("--------------------------------")
    # calcul pour la partie gauche de la traverse = 1a
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= (L/3)-6 and nbr1a <= nbr_1a_c3:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c3
        nbr1a += 1
        nbrdrainage += 1
    # calcul pour la partie central de la traverse = 2a
    nbr2a = 1
    while p_2a_1 < L-(L/3)+47.5 and nbr2a <= nbr_2a_1_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c3
        nbr2a += 1
        nbrdrainage += 1
     # calcul pour la partie droite de la traverse = 2a
    nbr2a = 1
    while p_2a_2 < L-158 and nbr2a <= nbr_2a_2_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_2))
        p_2a_2 = p_2a_2 + axe_2a_2_c3
        nbr2a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c3()

