#készítsünk egy 100 elemű 50 és 500 közötti számokat tartalmazó listát
'''
import random
szamlista = []
for szam in range(100):
    szamlista.append(random.randint(50, 500))
print(szamlista)
'''
#összegzés tétele
#Tétel: Adott egy N elemű számsorozat. Határozzuk meg a sorozat elemeinek összegét!
#Algoritmus:
# Eljárás összegzés(N,A[],S)
# S:=0
# Ciklus i:1-től N-ig
    # S:=f(S;A[i]) //S=S+A[i]
#ciklus vége eljárás vége
'''
szumma1 = sum(szamlista)
N = len(szamlista)
s = 0
for i in range(0,N,2):
    if szamlista[i] %2 == 0:
        s+= szamlista[i]
print(s)
'''

import random
def  osszegzes(sor):
    szum = 0
    for j in sor:
        szum+=j
    return szum

szmlista = []
for szam in range(100):
    szmlista.append(random.randint(1000, 5000))
print(szmlista)
print(f"A sorozat összege: {osszegzes(szmlista)}\n és átlaga {osszegzes(szmlista)/len(szmlista)}")
print(f"összeg sajátfüggvénnyel: {sum(szmlista)}n")

#Szelsőérték keresés tétele:Adott egy N elemű sorozat hatzározzuk meg a sorozat legnagyobb illetve legkisebb értékű elemét.
#szélső értk (A)
#maxi = 1
#ciklus 1 = 2-től N-ig 1 lépéssel
    #ha A[maxi]<A[i] akkor
    #maxi = i elágazás vége
#ciklus vége
#eljárás vége
def legnagy(sor):
    maxi = 0
    for i in range(1,len(sor)):
        if sor[maxi]<sor[i]:
            maxi = i
    return maxi
print(f"sor sorozat legnagyobb eleme a {szmlista[legnagy(szmlista)]} amely a {legnagy(szmlista)}. helyen található")
def legkis(sor):
    kicsi = 0
    for i in range(1,len(sor)):
        if sor[kicsi]>sor[i]:
            kicsi = i
    return kicsi
print(f"sor sorozat legkisebb eleme a {szmlista[legkis(szmlista)]} amely a {legkis(szmlista)}. helyen található")
#megszámlálás tétele: adott egy N elemű sorozat, sorozat elemein értelmezett T tulajdonság,
#határozzuk meg, hogy hány T tulajdonságú elem van a sorozatban.
#db = 0
#ciklus i = 1-től N-ig 1 lépéssel
#Ha A[i] T tul akkor
#db = db+1
#elágazás vége
#ciklus vége
#eljárás vége
def megszamolparos(sor):
    parosdarab = 0
    for szam in sor:
        if szam % 2 == 0:       #T tulajdonság
            parosdarab += 1     #parosdarab = parosdarab + 1
    return parosdarab


def megszamolparos(sor):
    parosdarab = 0
    for szam in sor:
        if   3000 > szam > 2000 :
            parosdarab += 1      
    return parosdarab
print(megszamolparos)
#eldöntés tétele: adott egy N elemű sorozat, a sorozat elemein értelmezett T tulajdonság.
#határozzuk meg, hogy van-e a sorozatban T tulajdonságú elem.
#i = 1
#ciklus amíg i<=N és A[i] NEM T tul
    #i = i + 1
#ciklus vége
#ha i<=N akkor van
#különben nincs
#eljárás vége
#eljárás vége
#Feladat: Van-e a sorozatban páros szám
def VanParos(A):
    N = len(A)
    i = 0
    while i < N and A [i] % 2 != 0:
        i += 1 #i = i + 1
    if i < N :
        return True
    else:
        return False
if VanParos(szmlista):
    print("A sorozatban VAN páros szám")
else:
    print("A sorozatban NINCS páros szám")

#Lottó sorsolást 5-ös lottó
NyeroSzamok = []
while len(NyeroSzamok)<= 5:
    nyszam =



'''
for i in range(5):
    NyeroSzamok.append(random.randint(1,91))
print(NyeroSzamok)
'''    

