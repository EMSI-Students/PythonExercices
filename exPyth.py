

# moyenne d'une collection de valeurs entrées#
L = []
i=0
val=1
while val!=0:
    if val!=0:
        val=float(input(f"Type a value {i+1} "))
        L.append(val)
        i=i+1
    else:
        break

somme=0
for k in L:
    somme+=k

Moy=somme/(i-1)
print(f"La moyenne : {Moy}")



         #BINAIRE EN DECIMAL#
def binaryToDec(n):
    return int(n,2)
print (binaryToDec('1100'))



 #TYPE DU TRIANGLE#

L1= float(input("Entrer la longueur 1 du triangle \n"))
L2= float(input("Entrer la longueur 2 du triangle \n"))
L3= float(input("Entrer la longueur 3 du triangle \n"))

if L1==L2 and L2==L3:
    print("Le triangle est equilatéral \n")
elif L1==L2 and L3!=L2 or L2==L3 and L1!=L2 or L1==L3 and L2!=L1:
    print("Le triangle est isocèle \n")
else:
    print("Le triangle est scalène \n")  



# DECIMAL EN BINAIRE #
def DecToBin(number):
        if number >= 1:
            DecToBin(number // 2)
            print (number % 2) 

DecToBin(12)

#Fonctions sur les listes des nombres#

def listInt():
    List = []
    while True:
     x = int(input())
     if not x:
            List1 = []
     for i in range(len(List)):
            List1.append(min(List))
            List.remove(min(List))
            return List1   
     else:
        List.append(x)

newL = listInt()
#print("insert values")
print(newL) 

#ispangram#
import string

def ispangram(str):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabets:
		if char not in str.lower():
			return False
	return True

string = 'The five boxing wizards jump quickly'
if(ispangram(string) == True):
	print("Yes it's a pangram")
else:
	print("No it's not a pangram")
          
   #datetime#	
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day)		
