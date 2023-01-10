from tankas import Tankas

tankas = Tankas()
tankas.generuoti_priesa()
while True:
    tankas.info()
    if tankas.ar_pabaiga():
        print("Baigėsi taškai. Žaidimo pabaiga")
        break
    pasirinkimas = input("Judėti į:\ns - šiaurę\np - pietūs\nv - vakarai\nr - rytai\nx - šūvis\ni - info\nr - rekordas\nb - išeiti iš žaidimo\n")
    if pasirinkimas == "s":
        tankas.siaure()
    if pasirinkimas == "p":
        tankas.pietus()
    if pasirinkimas == "v":
        tankas.vakarai()
    if pasirinkimas == "r":
        tankas.rytai()
    if pasirinkimas == "x":
        tankas.suvis()
    if pasirinkimas == "i":
        tankas.info()
    if pasirinkimas == "r":
        rekordas = tankas.gauti_rekorda()
        print(f"Rekordas: vardas - {rekordas['vardas']}, taškai - {rekordas['taskai']}")
    if pasirinkimas == "b":
        print("Viso gero")
        break
 #output
Process finished with exit code 0
