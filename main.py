import feladatok
lista=[12, 21,56,32,-5,-23,35]

print("Első feladat.")
db:int=feladatok.fel1(lista)
print(f"A pozitív számok száma: {db}")

print("Második feladat.")
ossz:int=feladatok.fel2(lista)
print(f"A negatív számok összege: {ossz}")

print("Harmadik feladat.")
atlag:float=feladatok.fel3(lista)
print(f"Az 5-tel osztható számok átlaga: {atlag}")