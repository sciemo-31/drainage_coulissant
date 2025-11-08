from choix import *

# def cas1():
p_2a = 160
p_1a = (L/2)+80
nbr_2a_c1 = 3
nbr_1a_c1 = 2
axe_2a_c1 = ((L/2)-80-160)/2
axe_1a_c1 = ((L/2)-80-160)
def cotation_c1():
    a = 160 #départ et entre secteur
    b = round(axe_2a_c1,2) #entre axe 2a partie gauche
    c = round(axe_1a_c1,2) #entre axe 1a partie droite
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:",
          b, "\nD3->D4:", a, "\nD4->D5:", c)

# def cas2():
nbr_2a_c2 = 5
nbr_1a_c2 = 3
axe_2a_c2 = ((L/2)-80-160)/4
axe_1a_c2 = ((L/2)-80-160)/2

def cotation_c2():
    a = 160  # départ et entre secteur
    b = round(axe_2a_c2, 2)  # entre axe 2a partie gauche
    c = round(axe_1a_c2, 2)  # entre axe 1a partie droite
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:",
          b, "\nD3->D4:", b, "\nD4->D5:", b, "\nD5->D6:",
          a, "\nD6->D7:", c, "\nD7->D8:", c)

# def cas3():
nbr_2a_c3 = 6
nbr_1a_c3 = 4
axe_2a_c3 = ((L/2)-80-160)/5
axe_1a_c3 = ((L/2)-80-160)/3


def cotation_c3():
    a = 160  # départ et entre secteur
    b = round(axe_2a_c3, 2)  # entre axe 2a partie gauche
    c = round(axe_1a_c3, 2)  # entre axe 1a partie droite
    print("=>D1: ", a, "\nD1->D2:", b, "\nD2->D3:",
          b, "\nD3->D4:", b, "\nD4->D5:", b, "\nD5->D6:",
          b, "\nD6->D7:", a, "\nD7->D8:", c, "\nD8->D9:", c, "\nD9->D10:", c)



if choix == 2 and L <= 2000:
    print("--------------------------------")
    print("Nbr de drainage 2a: " + str(nbr_2a_c1) + " - Entre-axe 2a: ", round(axe_2a_c1,2))
    print("Nbr de drainage 1a: " + str(nbr_1a_c1) + " - Entre-axe 1a: ", round(axe_1a_c1,2))
    print("--------------------------------")
    nbrdrainage = 1
    nbr2a = 1
    while p_2a <= L/2 and nbr2a <=nbr_2a_c1:
        print("Drainage n°", nbrdrainage , "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c1
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour les 1a
    nbr1a = 1
    while p_1a <= L-150 and nbr1a <= nbr_1a_c1:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c1
        nbr1a += 1
        nbrdrainage += 1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c1()

elif choix == 2 and 2000 <= L <= 3000:
    print("--------------------------------")
    print("Nbr de drainage 2a: " + str(nbr_2a_c2) +
          " - Entre-axe 2a: ", round(axe_2a_c2))
    print("Nbr de drainage 1a: " + str(nbr_1a_c2) +
          " - Entre-axe 1a: ", round(axe_1a_c2, 2))
    print("--------------------------------")
    nbrdrainage = 1
    nbr2a = 1
    while p_2a <= L/2 and nbr2a <= nbr_2a_c2:
        print("Drainage n°",nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c2
        nbr2a += 1
        nbrdrainage += 1
    #calcul pour les 1a
    nbr1a = 1
    while p_1a <= L-150 and nbr1a <= nbr_1a_c2:
        print("Drainage n°",nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c2
        nbr1a += 1
        nbrdrainage += 1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c2()
    
elif choix == 2 and L > 3000:
    print("--------------------------------")
    print("Nbr de drainage 2a: " + str(nbr_2a_c3) +
          " - Entre-axe 2a: ", round(axe_2a_c3))
    print("Nbr de drainage 1a: " + str(nbr_1a_c3) +
          " - Entre-axe 1a: ", round(axe_1a_c3, 2))
    print("--------------------------------")
    nbrdrainage = 1
    nbr2a = 1
    while p_2a <= L/2 and nbr2a <= nbr_2a_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c3
        nbr2a += 1
        nbrdrainage += 1
    # calcul pour les 1a
    nbr1a = 1
    while p_1a <= L-150 and nbr1a <= nbr_1a_c3:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c3
        nbr1a += 1
        nbrdrainage += 1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c3()