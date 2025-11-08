from choix import *

#def cas1():
p_1a = 160
p_2a = (L/2)+80
nbr_1a_c1 = 2
nbr_2a_c1 = 3
axe_1a_c1 = (L/2)-80-160
axe_2a_c1 = ((L/2)-80-160)/2
def cotation_c1():
    a = 160
    b = round(axe_1a_c1, 2)
    c = 160
    d = round(axe_2a_c1, 2)
    e = round(axe_2a_c1, 2)
    f = 160
    print("=>D1: ",a,"\nD1->D2:",b,"\nD2->D3:",c,"\nD3->D4:",d,"\nD4->D5:",e)

#def cas2():
nbr_1a_c2 = 3
nbr_2a_c2 = 5
axe_1a_c2 = ((L/2)-80-160)/2
axe_2a_c2 = ((L/2)-80-160)/4
def cotation_c2():
    a = 160
    b = round(axe_1a_c2, 2)
    c = round(axe_1a_c2, 2)
    d = 160
    e = round(axe_2a_c2, 2)
    f = round(axe_2a_c2, 2)
    g = round(axe_2a_c2, 2)
    h = round(axe_2a_c2, 2)
    print("=>D1:", a, "\nD1->D2:", b, "\nD2->D3:", c, "\nD3->D4:", d, "\nD4->D5:", e,"\nD5->D6:", f,"\nD6->D7:", g,"\nD7->D8:", h)

#def cas3():
nbr_1a_c3 = 4
nbr_2a_c3 = 6
axe_1a_c3 = ((L/2)-80-160)/3
axe_1a_c3 = round(axe_1a_c3,2)
axe_2a_c3 = ((L/2)-80-160)/5
axe_2a_c3 = round(axe_2a_c3,2)
#def cotation_c3():
   #for drainage in ["=>D1: 160","D1->D2: " ,axe_1a_c3, axe_1a_c3, axe_1a_c3, "160", axe_2a_c3, axe_2a_c3, axe_2a_c3, axe_2a_c3, axe_2a_c3]:
       #print (drainage)
def cotation_c3():
    print("=>D1: 160", "\nD1->D2:",axe_1a_c3, "\nD2->D3:",axe_1a_c3,"\nD3->D4:",axe_1a_c3,"\nD4->D5: 160",
          "\nD5->D6:",axe_2a_c3,"\nD6->D7:",axe_2a_c3,"\nD7->D8:",axe_2a_c3,"\nD8->D9:",axe_2a_c3,"\nD9->D10:",axe_2a_c3)


if choix == 1 and L <= 2000:
    print("--------------------------------")
    print("Nbr de drainage 1a: " + str(nbr_1a_c1) + " - Entre-axe 1a: ", round(axe_1a_c1,2))
    print("Nbr de drainage 2a: " + str(nbr_2a_c1) + " - Entre-axe 2a: ", round(axe_2a_c1,2))
    print("--------------------------------")
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= L/2 and nbr1a <= nbr_1a_c1:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a, 2))
        p_1a = p_1a + axe_1a_c1
        nbr1a += 1
        nbrdrainage +=1
# calcul pour les 2a
    nbr2a = 1
    while p_2a <= L-150 and nbr2a <= nbr_2a_c1:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c1
        nbr2a += 1
        nbrdrainage +=1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c1()


    

elif choix == 1 and 2000 <= L <= 3000:
    print("--------------------------------")
    print("Nbr de drainage 1a: " + str(nbr_1a_c2) +
          " - Entre-axe 1a: ", round(axe_1a_c2,2))
    print("Nbr de drainage 2a: " + str(nbr_2a_c2) +
          " - Entre-axe 2a: ", round(axe_2a_c2, 2))
    print("--------------------------------")
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= L/2 and nbr1a <= nbr_1a_c2:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c2
        nbr1a +=1
        nbrdrainage +=1
    #calcul pour les 2a
    nbr2a = 1
    while p_2a <= L-150 and nbr2a <= nbr_2a_c2:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c2
        nbr2a += 1
        nbrdrainage +=1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c2()


elif choix == 1 and L > 3000:
    print("--------------------------------")
    print("Nbr de drainage 1a: " + str(nbr_1a_c3) +
      " - Entre-axe 1a: ", round(axe_1a_c3, 1))
    print("Nbr de drainage 2a: " + str(nbr_2a_c3) +
          " - Entre-axe 2a: ", round(axe_2a_c3,1))
    print("--------------------------------")
    nbrdrainage = 1
    nbr1a = 1
    while p_1a <= L/2 and nbr1a <= nbr_1a_c3:
        print("Drainage n°", nbrdrainage, "=> 1a :", round(p_1a))
        p_1a = p_1a + axe_1a_c3
        nbr1a += 1
        nbrdrainage += 1
    # calcul pour les 1a
        nbr2a = 1
    while p_2a <= L-150 and nbr2a <= nbr_2a_c3:
        print("Drainage n°", nbrdrainage, "=> 2a :", round(p_2a))
        p_2a = p_2a + axe_2a_c3
        nbr2a += 1
        nbrdrainage += 1
    print("--------------------------------")
    print("Cotation non cumulée")
    cotation_c3()
    
