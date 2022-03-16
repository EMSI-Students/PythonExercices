a=int(input("entrez un premier nombre"))
b=int(input("entrez un deuxieme nombre"))
c=int(input("entrez un dernier nombre"))
if a==b==c :
    print("equilateral")
elif (a==b!=c) or (b==c!=a) or (c==a!=b):
    print("isocele")
else :
    print("scalene")