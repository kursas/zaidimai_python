#1 etapas
#Klasė: Tankas
#Metodai: pirmyn, atgal, kairėn, dešinėn, šūvis, info, ...
#Kintamieji turi:
#saugoti tanko koordinates,
#saugoti tanko kryptį,
#saugoti šūvių skaičių į kiekvieną kryptį.
#Tankas gali judėti pirmyn (į Šiaurę), dešinėn (į Rytus), atgal (į Pietus),
# kairėn (į Vakarus) per vieną poziciją. Pvz. „tankas pajuda kairėn“,
# tai reiškia jis pasisuko 90 laipsnių ir pajudėjo per vieną vienetą į Vakarus.
#Tankas gali šaudyti tik ta kryptimi, į kurią jis yra pasisukęs.
#Metodas info() turi parodyti:
##kokios yra jo koordinatės,
#kiek iš viso atliko šūvių
#kiek atliko šūvių į kiekvieną kryptį atskirai.
#Visas tanko ir informacijos valdymas turi būti
# atliktas konsolėje (grafinio interfeiso nereikia).
# Tam reikės sukurti meniu ir priimti vartotojo nurodymus.
# Veiksmai turi būti atliekami (kviečiami metodai) tol, kol vartotojas
# nesustabdys programos (pavyzdžiui, pasirinkęs tam tikrą meniu punktą).
#2 etapas
#Patobulinkite programą taip, kad koordinačių sistemoje būtų generuojamas taikinys.
# Tanko užduotis - atsidurti tinkamoje pozicijoje ir reikiama kryptimi,
# kad iššovus būtų fiksuojamas pataikymas. Tankui pataikius,
# konsolėje matome užrašą "pataikei" ir tuoj pat sugeneruojamas naujas taikinys.
#3 etapas
#Sugalvokite taškų sistemą, pvz pradedama su 100 taškų,
# už pataikymus galima skirti 50 taškų, už kiekvieną pavažiavimą
# nubraukti 10 taškų. Sumuoti pataikymus. Pasibaigus taškams programa parodo,
# kiek numušta taikinių, ir pasibaigia. Galbūt galima saugoti high scores - pasibaigus
# įvedamas vardas ir žaidėjas su numuštų taikinių skaičiumi įrašomas į topus. Topus galbūt galima pažiūrėti
# su komanda 'top'. Sugalvokite kokių nors savo patobulinimų, sėkmės :)
from random import randint
import pickle

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]
        self.priesas_x = 0
        self.priesas_y = 0
        self.priesai = 0
        self.taskai = 100

    def nupiesti_lauka(self):
        print("- - - - - - - - - - -")
        for y in range(5,-6, -1):
            for x in range(-5, 6):
                if self.y == y and self.x == x:
                    print(f"0 ", end="")
                elif self.priesas_y == y and self.priesas_x == x:
                    print(f"X ", end="")
                elif y == 0 or x == 0:
                    print(f"+ ", end="")
                else:
                    print(f". ", end="")
            print()
        print("- - - - - - - - - - -")

    def gauti_rekorda(self):
        try:
            with open('rekordas.pkl', 'rb') as file:
                rekordas = pickle.load(file)
        except:
            print("Nėra tokio failo")
            with open("rekordas.pkl", 'wb') as failas:
                rekordas = {"vardas": "demo", "taskai": 0}
                pickle.dump(rekordas, failas)
        return rekordas

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self.taskai -= 10

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self.taskai -= 10

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self.taskai -= 10

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self.taskai -= 10

    def _tikrinti_pataikyma(self):
        if self.x == self.priesas_x and self.kryptis == "Š" and self.y < self.priesas_y:
            return True
        if self.x == self.priesas_x and self.kryptis == "P" and self.y > self.priesas_y:
            return True
        if self.y == self.priesas_y and self.kryptis == "V" and self.x > self.priesas_x:
            return True
        if self.y == self.priesas_y and self.kryptis == "R" and self.x < self.priesas_x:
            return True
        return False

    def generuoti_priesa(self):
        self.priesas_x = randint(-5, 5)
        self.priesas_y = randint(-5, 5)

    def suvis(self):
        if self.kryptis == "Š":
            self.suviai[0] += 1
        if self.kryptis == "P":
            self.suviai[1] += 1
        if self.kryptis == "V":
            self.suviai[2] += 1
        if self.kryptis == "R":
            self.suviai[3] += 1
        if self._tikrinti_pataikyma():
            print("PATAIKEI!")
            self.priesai += 1
            self.generuoti_priesa()
            self.taskai += 50

    def irasyti_rekorda(self):
        vardas = input("Įrašykite savo vardą")
        rekordas = {"vardas": vardas, "taskai": self.priesai}
        try:
            with open("rekordas.pkl", 'wb') as failas:
                pickle.dump(rekordas, failas)
        except:
            print("Nepavyko įrašyti rekordų failo")

    def ar_pabaiga(self):
        if self.taskai <= 0:
            if self.gauti_rekorda()['taskai'] < self.priesai:
                print(f"Naujas rekordas: {self.priesai}")
                self.irasyti_rekorda()
            return True
        return False

    def info(self):
        print(f"Koordinatės: X: {self.x}, Y: {self.y}")
        print(f"Priešas: X: {self.priesas_x}, Y: {self.priesas_y}")
        print(f"Kryptis: {self.kryptis}")
        print(f"Taškai: {self.taskai}")
        print("--------------------------")
        print(f"Šūviai: {self.suviai}")
        print(f"Nušauti tankai: {self.priesai}")
        self.nupiesti_lauka()
        
  #output
  Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: Š
Taškai: 100
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
s
Koordinatės: X: 0, Y: 1
Priešas: X: -1, Y: 4
Kryptis: Š
Taškai: 90
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . 0 . . . . . 
+ + + + + + + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
p
Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: P
Taškai: 80
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
v
Koordinatės: X: -1, Y: 0
Priešas: X: -1, Y: 4
Kryptis: V
Taškai: 70
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + 0 + + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
r
Nėra tokio failo
Rekordas: vardas - demo, taškai - 0
Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: R
Taškai: 60
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
š
Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: R
Taškai: 60
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
i
Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: R
Taškai: 60
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Koordinatės: X: 0, Y: 0
Priešas: X: -1, Y: 4
Kryptis: R
Taškai: 60
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + 0 + + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
r
Rekordas: vardas - demo, taškai - 0
Koordinatės: X: 1, Y: 0
Priešas: X: -1, Y: 4
Kryptis: R
Taškai: 50
--------------------------
Šūviai: [0, 0, 0, 0]
Nušauti tankai: 0
- - - - - - - - - - -
. . . . . + . . . . . 
. . . . X + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
+ + + + + + 0 + + + + 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
. . . . . + . . . . . 
- - - - - - - - - - -
Judėti į:
s - šiaurę
p - pietūs
v - vakarai
r - rytai
x - šūvis
i - info
r - rekordas
b - išeiti iš žaidimo
b
Viso gero

Process finished with exit code 0
