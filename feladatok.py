'''lista
lista[12, 21,56,32,-5,-23,35]
Az alábbi metodusok  paraméterként kapják a fenti listát
1.Hány pozitív szám van benne
2.mennyi a negatív számok összege
3.mennyi az 5tel osztható számok átlaga'''

def fel1(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        print(lista[i])
        if(lista[i]>0):
            db+=1
        i+=1
        
    return db

def fel2(lista):
    i:int=0
    ossz:int=0
    while(i<len(lista)):
        print(lista[i])
        if(lista[i]<0):
            ossz+=lista[i]
        i+=1
        
    return ossz

def fel3(lista):
    i:int=0
    db:int=0
    osszeg:int=0
    while(i<len(lista)):
        if(lista[i]%5==0):
            osszeg+=lista[i]
            db+=1
        i+=1
    atlag:float=osszeg/db
    return atlag

