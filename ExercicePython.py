"""EXERCICE 01"""

'''def Function():
    x = float(input("Entrer la longueur du premier cote "))
    y = float(input("Entrer la longueur du Deuxieme cote "))
    z = float(input("Entrer la longueur du Troisieme cote "))
    if x==y and x==z and y==z:
        print('Triangle equilateral')
    elif x!=y and x!=z and y!=z:
        print('Triangle scalene')
    else:
        print('Triangle isocele')

"""EXERCICE 02"""

Function() '''
'''def Function2():
    s = 0
    i = 0
    x = int(input())
    while x!=0:    
        s += x
        i += 1
        x = int(input())
    if i == 0:
        print('Error')    
    else: return s/i

n = Function2()
print('la moyenne est ',n)'''

"""EXERCICE 03"""

"""def FunctionInt():
    List = []
    while True:
        x = int(input())
        if not x:
            List2 = []
            for i in range(len(List)): 
                List2.append(min(List))
                List.remove(min(List))
            return List2    
        else:
            List.append(x)


NvList = FunctionInt()
print(NvList) """

"""EXERCICE 04"""

'''def DecToBin(N):
    List = []
    while N!=0:
        List.insert(0,N%2)
        N = N//2
    List.insert(0,0)    
    return List

List = DecToBin(30)
print(List)'''

"""EXERCICE 05"""

'''def BinToDec(List):
    n = len(List)
    S = 0
    for i in List:
        S += (i * (2** (n-1)))
        n -= 1
    print(S)    

List = [0,1,1,1,1,0]
BinToDec(List)'''



''' EXERCICE 01 SERIE 02 

from ast import Continue
from random import randint, random
from string import ascii_letters
from typing import List


def get_alphabet():
    S = ""
    for i in range(97,123):
        S += chr(i)
    return S

s = get_alphabet()
print(s)

def  is_pangramme(stringPar):
    s = get_alphabet()
    for i in s:
        if i in stringPar:
            Continue
        else:
            return False
            exit
    return True'''
'''
print(is_pangramme("abc defg hijklmno pqrstuv wxyz"))                
'''

''' EXERCICE 04 SERIE 02 

def ordinalDate(Jour,Mois,Annee):
    s = Jour
    for i in range(Mois):
        s += 30    
    print(f"Le jour {s} / l'annee {Annee}")

ordinalDate(1,1,2022)'''


''' EXERCICE 06 SERIE 02 
import random

def Random_Password():
    Length = random.randint(7,10)
    s = ""
    for i in range(Length+1):
        j = random.randrange(33,126)
        s += chr(j)
    return s

print(Random_Password())   ''' 


''' EXERCICE 07 SERIE 02 
def GET_ALPHABET():
    S = ""
    for i in range(65,91):
        S += chr(i)
    return S


def Password_valide(Password):
    ListCarSp = "%#:$*"
    LettresMin = get_alphabet()
    LettresMaj = GET_ALPHABET()
    if len(Password) >= 8:
        if LettresMin in Password:
            if LettresMaj in Password:
               if ListCarSp in Password:
                   return True
               else: return False 
            else: return False
        else: return False                           
    else: return False

print(Password_valide("a$Afegfvk21"))'''

'''A partir de l'exercice 9'''

'''Exercice 09 Serie 02'''

def hex2int(Number):
    if(Number.isdigit()):
        number = int(Number)
        if(number >= 0 and number <= 9):
            return number
        else:
            return 'Error'    
    else:
        if Number == 'A' or Number =='a':
            return 10
        elif Number == 'B' or Number =='b':
            return 11    
        elif Number == 'C' or Number =='c':
            return 12
        elif Number == 'D' or Number =='d':
            return 13
        elif Number == 'E' or Number =='e':
            return 14
        elif Number == 'F' or Number =='f':
            return 15  
        else:
            return 'Error'              

print(hex2int('11'))
''' Il existe deja une fct qui permet de convertir un integer en hex  ====  hex() '''


''' Exercice 10 Serie 02'''
def DecToBase(N,Base):
    List = []
    while N!=0:
        List.insert(0,N%Base)
        N = N//Base
    return List    
    
def NumberBase(Number,Base):
    if(Base == 2):
        List = DecToBase(Number,Base)
        return List
    elif(Base == 8):
        List = DecToBase(Number,Base)
        return List
    elif(Base ==16):
        List =  DecToBase(Number,Base)   
        return List
    else:    
        return 'Error'

'''Exercice 11 Serie 02 '''
def PlusReduit(Num,Den):
    Number = Num % Den
    while True:
        

