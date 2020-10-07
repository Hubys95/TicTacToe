"""Author: Jan Hubacek"""

ODDELOVAC = "=" * 40
ODDELOVAC_plocha = "-" * 9

print(ODDELOVAC)
print("Vítejte ve hře!")
print("Pravidla hry.")
print("Vítězem této hry je hráč, který jako první dokáže vytvořit nepřerušenou řadu třech svých značek.")
print("Ve vertikálním, horizontálním nebo diagonálním směru.")
print("Pojďme hrát!")

plocha = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]


def zobrazeni_herni_plochy():
    print(ODDELOVAC_plocha)
    print(plocha[0], "|", plocha[1], "|", plocha[2])
    print(ODDELOVAC_plocha)
    print(plocha[3], "|", plocha[4], "|", plocha[5])
    print(ODDELOVAC_plocha)
    print(plocha[6], "|", plocha[7], "|", plocha[8])
    print(ODDELOVAC_plocha)


hra_bezi = True
vitez = None
soucasny_hrac = "x"


def hra():
    zobrazeni_herni_plochy()
    while hra_bezi:
        tah()
        kontrola()
        zmena_hrace()
    if vitez == "o" or vitez == "x":
        print("Hráč", vitez, "vyhrává!")
    elif vitez is None:
        print("Remíza!")


def tah():
    print("Hráč", soucasny_hrac, "hraje.")
    try:
        pozice = int(input("Zvol číslo v rozmezí od 1 do 9.: ")) - 1

        while plocha[pozice] != " ":
            pozice = int(input("Prosím zvol jiné číslo.: ")) - 1

            while pozice not in range(0, 10):
                print("Prosím, vlož číslo v rozmezí od 1 do 9.")
                pozice = int(input("Zvol číslo v rozmezí od 1 do 9.: ")) - 1

    except ValueError:
        print("Prosím, vlož číslo.")
        return zmena_hrace()
    except IndexError:
        print("Prosím, vlož číslo v rozmezí od 1 do 9.")
        return zmena_hrace()

    plocha[pozice] = soucasny_hrac

    zobrazeni_herni_plochy()


def kontrola():
    vyhra()
    remiza()


def vyhra():
    global vitez
    vitez_radku = kontrola_radku()
    vitez_sloupce = kontrola_sloupce()
    vitez_diagonaly = kontrola_diagonaly()

    if vitez_radku:
        vitez = vitez_radku
    elif vitez_sloupce:
        vitez = vitez_sloupce
    elif vitez_diagonaly:
        vitez = vitez_diagonaly
 

def kontrola_radku():
    global hra_bezi
    radek1 = plocha[0] == plocha[1] == plocha[2] != " "
    radek2 = plocha[3] == plocha[4] == plocha[5] != " "
    radek3 = plocha[6] == plocha[7] == plocha[8] != " "
    if radek1 or radek2 or radek3:
        hra_bezi = False
    if radek1:
        return plocha[0]
    elif radek2:
        return plocha[3]
    elif radek3:
        return plocha[6]


def kontrola_sloupce():
    global hra_bezi
    sloupec1 = plocha[0] == plocha[3] == plocha[6] != " "
    sloupec2 = plocha[1] == plocha[4] == plocha[7] != " "
    sloupec3 = plocha[2] == plocha[5] == plocha[8] != " "
    if sloupec1 or sloupec2 or sloupec3:
        hra_bezi = False
    if sloupec1:
        return plocha[0]
    elif sloupec2:
        return plocha[1]
    elif sloupec3:
        return plocha[2]


def kontrola_diagonaly():
    global hra_bezi
    diagonala1 = plocha[0] == plocha[4] == plocha[8] != " "
    diagonala2 = plocha[2] == plocha[4] == plocha[6] != " "
    if diagonala1 or diagonala2:
        hra_bezi = False
    if diagonala1:
        return plocha[0]
    elif diagonala2:
        return plocha[2]


def remiza():
    global hra_bezi
    if not " " in plocha:
        hra_bezi = False


def zmena_hrace():
    global soucasny_hrac
    if soucasny_hrac == "x":
        soucasny_hrac = "o"
    elif soucasny_hrac == "o":
        soucasny_hrac = "x"


hra()
