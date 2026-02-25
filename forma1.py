"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
import statistics
pilotak = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozszam = int(adatok[2])
        futamok = int(adatok[3])
        pilota = {'nev': nev, 'csapat': csapat, 'gyozszam': gyozszam, 'futamok': futamok}
        pilotak.append(pilota)

#1. feladat
print(f"1. A beolvasott fájlban összesen {len(pilotak)} versenyző szerepel.")

#2. feladat
legtobb_gyoz = pilotak[0]
for i in pilotak:
    if legtobb_gyoz["gyozszam"] < i["gyozszam"]:
        legtobb_gyoz = i
print(f"2. A legtöbb futamot nyert versenyző: {legtobb_gyoz["nev"]}")
#3.feladat
legkevesebb_gyoz = pilotak[0]
for i in pilotak:
    if legkevesebb_gyoz["gyozszam"] > i["gyozszam"]:
        legkevesebb_gyoz = i

legkevesebb_gyoz_2 = pilotak[0]        
for i in pilotak:
    if legkevesebb_gyoz_2["gyozszam"] >= i["gyozszam"]:
        legkevesebb_gyoz_2 = i
print(f"3. A legkevesebb futamot nyert versenyzők: {legkevesebb_gyoz["nev"]} és {legkevesebb_gyoz_2["nev"]}")
#4.feladat

legtobb_futam = pilotak[0]
for i in pilotak:
    if legtobb_futam["futamok"] < i["futamok"]:
        legtobb_futam = i

print(f"4. A legtöbb futamot teljesített versenyző: {legtobb_futam["nev"]}")
#5.feladat
print(f"5. Az átlagos futamszám: {statistics.mean(i["futamok"] for i in pilotak)}")


#6.feladat (szorg)
csapat_gyoz = {}

for pilota in pilotak:
    csapat = pilota['csapat']
    gyoz = pilota['gyozszam']

if csapat not in csapat_gyoz:
        csapat_gyoz[csapat] = gyoz
else:
        csapat_gyoz[csapat] += gyoz

legtobb_csapat = max(csapat_gyoz, key=csapat_gyoz.get)

print(f"***A legtöbb futamgyőzelmet szerző csapat: {legtobb_csapat}")