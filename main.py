hodnoty = open('hodnoty.txt').read().splitlines()
hodnoty = [tmp.split() for tmp in hodnoty]
smer = [(tmp[0], int( tmp[1]) ) for tmp in hodnoty]
hloubka = 0
delka = 0



if __name__ == '__main__':
    h, d = 0, 0

    for smery,vzdalenost in smer:
        if smery == 'forward':
            delka = delka + vzdalenost
        elif smery == 'down':
            hloubka = hloubka + vzdalenost
        elif smery == 'up':
            hloubka = hloubka - vzdalenost

    print(hloubka*delka)


