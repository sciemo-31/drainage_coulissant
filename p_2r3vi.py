from choix import *

# Drainage 2 rails 3 vantaux indépendants
# def cas1():
p_2a_1 = 160
p_2a_2 = (L/3)+29.5+(L/3)-59+80
p_1a = (L/3)+29.5+80

nbr_1a_c1 = 2
nbr_2a_1_c1 = 3
nbr_2a_2_c1 = 3
axe_1a_c1 = (L/3)-59-80-80
axe_2a_1_c1 = ((L/3)+29.5-160-80)/2
axe_2a_2_c1 = ((L/3)+29.5-160-80)/2

def cotation_c1():
    a = 160  # départ entre secteur
    b = round(axe_1a_c1, 2)  # entre-axe 1a au centre
    c = round(axe_2a_1_c1, 2)  # entre axe 2a partie gauche et droite
    print("=>D1: ",a,"\nD1->D2:",c,"\nD2->D3:",c,"\nD3->D4:",a,"\nD4->D5:",b,"\nD5->D6:",a,"\nD6->D7:",c,"\nD7->D8:",c)

# def cas2():
nbr_1a_c2 = 3
nbr_2a_1_c2 = 5
nbr_2a_2_c2 = 5
axe_1a_c2 = ((L/3)-59-80-80)/2
axe_2a_1_c2 = ((L/3)+29.5-160-80)/4
axe_2a_2_c2 = ((L/3)+29.5-160-80)/4

def cotation_c2():
    a = 160  # départ entre secteur
    b = round(axe_1a_c2, 2)  # entre-axe 1a au centre
    c = round(axe_2a_1_c2, 2)  # entre axe 2a partie gauche et droite
    print("=>D1: ", a, "\nD1->D2:", c, "\nD2->D3:", c, "\nD3->D4:", c,
          "\nD4->D5:", c, "\nD5->D6:", a, "\nD6->D7:", b, "\nD7->D8:", b,"\nD8->D9:",a,"\nD9->D10:",c,"\nD10->D11:",c,"\nD11->D12:",c,"\nD12->D13:",c)

# def cas3():
nbr_1a_c3 = 4
nbr_2a_1_c3 = 6
nbr_2a_2_c3 = 6
axe_1a_c3 = ((L/3)-59-80-80)/3
axe_2a_1_c3 = ((L/3)+29.5-160-80)/5
axe_2a_2_c3 = ((L/3)+29.5-160-80)/5
def cotation_c3():
    a = 160  # départ entre secteur
    b = round(axe_1a_c2, 2)  # entre-axe 1a au centre
    c = round(axe_2a_1_c2, 2)  # entre axe 2a partie gauche et droite
    print("=>D1: ", a, "\nD1->D2:", c, "\nD2->D3:", c, "\nD3->D4:", c,
          "\nD4->D5:", c, "\nD5->D6:", c, "\nD6->D7:", a, "\nD7->D8:", b, "\nD8->D9:", b, "\nD9->D10:", b, "\nD10->D11:", a, "\nD11->D12:", c, "\nD12->D13:", c, "\nD13->D14:", c, "\nD14->D15:", c, "\nD15->D16:", c)


if choix == 5 and L < 3000:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c1) +
          " - Entre-axe 1a: ", round(axe_1a_c1))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c1) +
          " - Entre-axe des 3 premiers 2a: ",  round(axe_2a_1_c1))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c1) +
          " - Entre-axe des 3 derniers 2a: ", round(axe_2a_2_c1))
    print("--------------------------------")
    # calcul pour la partie gauche de la traverse = 2a
    nbrdrainage = 1
    nbr2a = 1
    while p_2a_1 <= (L/3)+29.5 and nbr2a <= nbr_2a_1_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c1
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour la partie centrale de la traverse pour les 1a
    nbr1a = 1
    while p_1a < (L/3)+29.5 + (L/3)-59 and nbr1a <= nbr_1a_c1:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c1
        nbr1a += 1
        nbrdrainage += 1
    # calcul pour la partie droite de la traverse = 2a
    nbr2a = 1
    while p_2a_2 < L- 158 and nbr2a <= nbr_2a_2_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_2))
        p_2a_2 = p_2a_2 + axe_2a_2_c1
        nbr2a += 1
        nbrdrainage += 1
    # Cotation non cumulée
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c1()
    

elif choix == 5 and 3000 <= L <= 4500:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c2) +
          " - Entre-axe 1a: ", round(axe_1a_c2))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c2) +
          " - Entre-axe 2a: ", round(axe_2a_1_c2))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c2) +
          " - Entre-axe 2a: ", round(axe_2a_2_c2))
    print("--------------------------------")
# calcul pour la partie gauche de la traverse = 2a
    nbrdrainage = 1
    nbr2a = 1
    while p_2a_1 <= (L/3)+29.5 and nbr2a <= nbr_2a_1_c2:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c2
        nbr2a += 1
        nbrdrainage += 1
# calcul pour la partie centrale de la traverse pour les 1a
    nbr1a = 1
    while p_1a < (L/3)+29.5 + (L/3)-59 and nbr1a <= nbr_1a_c2:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c2
        nbr1a += 1
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
    
    


elif choix == 5 and L > 4500:
    print("--------------------------------")
    print("Nombre de drainage 1a: " + str(nbr_1a_c3) +
          " - Entre-axe 1a: ", round(axe_1a_c3))
    print("Nombre de drainage 2a: " + str(nbr_2a_1_c3) +
          " - Entre-axe 2a: ", round(axe_2a_1_c3))
    print("Nombre de drainage 2a: " + str(nbr_2a_2_c3) +
          " - Entre-axe 2a: ", round(axe_2a_2_c3))
    print("--------------------------------")
# calcul pour la partie gauche de la traverse = 2a
    nbrdrainage = 1
    nbr2a = 1
    while p_2a_1 <= (L/3)+29.5 and nbr2a <= nbr_2a_1_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a_1))
        p_2a_1 = p_2a_1 + axe_2a_1_c3
        nbr2a += 1
        nbrdrainage += 1
# calcul pour la partie centrale de la traverse pour les 1a
    nbr1a = 1
    while p_1a < (L/3)+29.5 + (L/3)-59 and nbr1a <= nbr_1a_c3:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c3
        nbr1a += 1
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
    
