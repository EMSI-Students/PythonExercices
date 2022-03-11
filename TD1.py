#--------------cryptage de César-------------------------
from ast import Not, While
from pickle import FALSE


def CdC(Text,n):
    S=""
    for i in Text:
        if 65<=ord(i)+n<=90:
            S+=(chr(ord(i)+n))
        elif 97<=a<=122:
            S+=(chr(ord(i)+n))
        elif 90<ord(i)+n<97:
            S+=(chr(ord(i)+n-26))
        else:
            S+=(chr(ord(i)+n-26))
    print(S)
#--------------BinToDec----------------------------------
def BinToDec(Text):
    print(int(Text,2))
#--------------DecToBin----------------------------------
def DecToBin(N):
    Text=""
    while N!=0:
        Text=str(N%2)+Text
        N=int(N//2)
    print(Text)
#--------------1fois-------------------------------------
def UneFois():
    List=[]
    while True:
        i=str(input())
        if i=="":
            break
        elif i not in List:
            List.append(i)
    for i in List:
        print(i)
#--------------Tri--------------------------------------
def Tri():
    List1,List2=[],[]
    while True:
        i=input()
        if i=="":
            break
        i=float(i)
        if i>=0:
            List2.append(i)
        else:
            List1.append(abs(i))
    List1.sort(reverse=True)
    List2.sort()
    for i in List1:
        print(-int(i))
    for i in List2:
        print(int(i))
#--------------estSousListe--------------------------------------
def estSousListe(L,S):
    i,Val=L.index(S[0]),True
    if len(S)>len(L)-i:
        return(False)
    for j in range(len(S)):
        if S[j]!=L[i+j]:
            Val=False
    return(Val)
#--------------SousListe--------------------------------------
def SousListe(L):
    def Calc(L):
        n = len(L)
        masks = [1 << i for i in range(n)]
        for i in range(1 << n):
            yield [ss for mask, ss in zip(masks, L) if i & mask]
    print(list(Calc(L)))
#--------------DictKeys--------------------------------------
def inverseRelation(dic,val):
    key_list = list(dic.keys())
    val_list = list(dic.values())
    S=[]
    for i in val_list:
        if i==val:
            S.append(val_list.index(i))
    for i in S:
        print(key_list[i])
#--------------SousListe--------------------------------------
def OldPhone(Val):
    S=[]
    dic={1:".,?!:",2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ",0:" "}
    for i in Val:
        for j in range(0,len(dic)):
            if i in list(dic.values())[j]:
                print(S.append([j+1,list(dic.values())[j].index(i)+1]))
    for i in range(len(S)):
        for j in range(S[i][1]):
            if S[i][0]==10:
                print(" ")
            else:
                print(S[i][0],end="")
