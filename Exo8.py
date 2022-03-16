bina=int(input("entrez le nombre binaire"))


def BinToDec(bin): 
    bin1 = bin 
    deci, i, n = 0, 0, 0
    while(bin != 0): 
        dec = bin % 10
        deci = deci + dec * pow(2, i) 
        bin = bin//10
        i += 1
    print(deci)  

BinToDec(bina)   