import random 
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

def fel4():
    fejiras_lista=[]
    i:int=0
    while(i<10):
        erme:int=int(random.random()*2)+1
        if(erme==2):
            fejiras_lista.append("Írás")
        elif(erme==1):
            fejiras_lista.append("Fej")
        i+=1
    return fejiras_lista

def fel4_2(fejiras_lista):
    i:int=0
    fej:int=0
    while(i<len(fejiras_lista)):
        if(fejiras_lista[i]=="Fej"):
            fej+=1
        i+=1
        
    return fej


def fel5():
    dobas_lista=[]
    i:int=0
    while(i<200):
        dobas:int=int(random.random()*7)+1
        if(dobas==1):
            dobas_lista.append(1)
        elif(dobas==2):
            dobas_lista.append(2)
        elif(dobas==3):
            dobas_lista.append(3)
        elif(dobas==4):
            dobas_lista.append(4)
        elif(dobas==5):
            dobas_lista.append(5)
        else:
            dobas_lista.append(6)
        i+=1

    return dobas_lista


def fel5_2(dobas_lista):
    i:int=0
    egy:int=0
    ketto:int=0
    harom:int=0
    negy:int=0
    ot:int=0
    hat:int=0
    while(i<len(dobas_lista)):
        if(dobas_lista[i]==1):
            egy+=1
        elif(dobas_lista[i]==2):
            ketto+=1
        elif(dobas_lista[i]==3):
            harom+=1
        elif(dobas_lista[i]==4):
            negy+=1
        elif(dobas_lista[i]==5):
            ot+=1
        elif(dobas_lista[i]==6):
            hat+=1
        i+=1
        
    return egy, ketto, harom, negy, ot, hat

