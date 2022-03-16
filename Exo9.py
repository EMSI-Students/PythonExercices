from pickle import TRUE
nbrListe  = []

while TRUE :
    n=input("entrez votre nom")
    if n=="" :
        break
    else :
        nbrListe.append(n)

new_list = [] 
for i in nbrListe : 
    if i not in new_list: 
        new_list.append(i) 

print(new_list)