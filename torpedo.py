from ast import Not
import random

#fügvényünk ez határozza meg az oszlop kordinátáját
def kordinata_felderitas(felhasz,dic):
    for x in dic:
        if felhasz == x:
            felhasz = dic.get(x)
    return felhasz




#könyvtár inen szedjük az oszlop kordinátáját
kordinata = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
}



'''
tábla
véletlen helyen legyen egy elenfél
találgatás (A,1) alapján
tábla sor része betük szerintí rendezés
'''

nagysagg = int(input('Mekkora legyen a tábla?(max 10): '))
if nagysagg >= 10 or nagysagg < 3:
    nagysagg = 3
    print('\nHelytelen szám! Alap értelmezett át álitva 3-ra')

talalat = 1

ran_i = random.randint(0,nagysagg)
ran_j = random.randint(0,nagysagg)

while True:

    #kordináta x(oszlop)
    felhasznalo_kordinata_x = input('Kérem a oszlop kordinátát(A,B,C,stb...): ').upper().strip()

    felhasznalo_kordinata_x = kordinata_felderitas(felhasznalo_kordinata_x,kordinata)

    #kordináta y(sor)
    felhasznalo_kordinata_y = int(input('Kérem a sor kordinátát(1,2,3,stb...): '))

    if felhasznalo_kordinata_y >= nagysagg:
        felhasznalo_kordinata_y = 0
        print('Nem lehet nagyobb a megadott nagyságnál! Alap értelmezett meg ad va 1-re')

    print('OoOoOoOoOoOoOoOoOoOoOoOoOoOoOo\n')
    
    if ran_i == felhasznalo_kordinata_y and ran_j == felhasznalo_kordinata_x:
        print('  Gratulálok elsüjeztetted az elenséges hajót \n')
        print(f'\n  Enyi találatból {talalat}')
        break

    print(f'Találat: {talalat}\n')

    #az oszlopban az ABC kirajzolása
    betuk = ['. ','A ','B ','C ','D ','E ','F ','G ','H ','I ']
    c = 0

    for b in betuk:
        if c <= nagysagg:
            print(b,end='')
            c += 1
    print('')



    # A konkrét map kirajzolása
    szamlalo = 0

    for i in range(nagysagg):
        print(szamlalo ,end=' ')
        
        
        for j in range(nagysagg):
            
            if i == felhasznalo_kordinata_y and j == felhasznalo_kordinata_x:
                print('X ',end='')
            
            else:
                print('O ',end='')
        
        
        szamlalo = szamlalo + 1
        print()
    
    talalat += 1





















































