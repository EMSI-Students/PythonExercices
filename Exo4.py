cpt=0
x=int(input("Donnez la valeur"))
moy=None
somme=0
if x==0:
    print("Erreur")
else:
    while x!=0 :
        cpt+=1
        somme+=x
        x=int(input("Donnez une autre valeur"))
    moy=somme/cpt
    print("la moyenne est ",moy)

