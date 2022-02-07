from itertools import starmap
import random
#Ez a könyv tár ahol a szavak vannak
könyvtár = ['alma','körte','eper','banán','szőlő','lángos','macska', "sajt_burger", "aranyhal", "rendőrség", "űrhajos", "telefon_betyár", "idő_utazó", "palacsinta", "szezám_mag", "vidámpark", "világtalálkozó", "felvillanyoz","erőmű" ,"univerzum", "nap_rendszer", "ventilátor", "szomszéd", "véreb", " kefir", " szalonna", "karóra", "skorpió", "vipera", "róka", "szellem", "szekrény", "kastély", "kemence", "kávéföző", "naplemente", "karfiol", "kantár", "kaptár", "bolt", "holdkor", "karosszéria", "karosszék", "káposzta", "karantén", "szölő", "szem", "szabolycs", "kapcsolat", "katasztrófa", "akasztófa", "távirányitó", "teveidimár", "teleszkop", "kályha", "kamion""hógolyó", "oroszlán", "istálló", "orvosság", "sintér", "hazugság", "közönséges", "apró", "keskeny","testvér", "vélemény", "tanács","vitorla","manapság", "tábortüz", "csöndes", "varázsló", "gyüjt", "kémkedik", "földnyelv", "villám", "zöldfülű","kellemetlen", "elpusztít", "földöntúli", "parancs", "légy", "veterán", "martalóc","szabotázs" ]
kiesett = []


#Itt vannak megadva az adatok
number1 = False
folytat = True
start = True
tovabb = False
nehezseg = True
talal = 0
tip = 3
elet = 3
szam = 0


#Menű rész
while start:
    print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
    print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
    print('\nÜdvözlünk a játékban! ', end='\n')
    print('\n>Start<')
    print('Info\n')
    menustart = str(input('\nKérlek válaszd ki hova szereznél tovább menni: '))
    print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
    print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
    if menustart == 'start' or menustart == 'Start':
        print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
        print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
        print('Hát akkor sok sikert')
        nehezseg = True
        start = False
    elif menustart == 'info' or menustart == 'Info':
        tovabb = True
        while tovabb:
            print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
            print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
            print('\nA játék elkezdésekor a játékos kap a nehézségi foktol fügöen addot menyiségü szavakat.\nEzekböl a szavakból a számíto gép kiválaszt 1 szót amit a játékosnak kell kitalálnia.\n')
            page = str(input('<Tovább>\t<Vissza>: '))
            if page in {'tovább','Tovább','tovabb','Tovabb'}:
                print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
                print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')    
                print('\nA játékosnak 3 lehetősege van kitalálnija a szót vagy különbben veszít.\nViszon rendelkezésére ál 3 segitség amivel rá tippelhet az egyik szó/szavak kezdő betűjére.\n')
                page = str(input('<Tovább>\t<Vissza>: '))
            elif page in {'vissza','Vissza'}:
                print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
                print('oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo')
                tovabb = False
            else:
                print('!!!!!!!!!!!!!!!!!!!!!')
                print('Nem értelmezhető parancs!! Vissza a fő menübe.')
                print('!!!!!!!!!!!!!!!!!!!!!')
                tovabb = False
    else:
        print('!!!!!!!!!!!!!!!!!!!!!')
        print('Nem értelmezhető parancs :(')
        print('!!!!!!!!!!!!!!!!!!!!!')

while nehezseg:
    
    print('\nKönyü\t','Közepes','Nehéz\n')
    
    #Könyü nehézségi fok
    nehezfok = str(input('Válaszd ki a nehézségi fokot: '))
    if nehezfok in {'könyü','Könyü','easy','Easy'}:
        for j in range(1):
            gyumolcsok = ['', '', '', '', '']
            for i in range(5):
                huzott = random.choice(könyvtár)
                k = 0
                while k < 5:
                    if gyumolcsok[k] == huzott:
                        huzott = random.choice(könyvtár)
                        k = 0
                    else:
                        k += 1
                        
                gyumolcsok[i] = huzott
        randgyum = random.choice(gyumolcsok)
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('\nKiválasztottad a Könyü\t nehézségi fokot\n')
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('Jó szorakozást ;)')
        nehezseg = False

    #Közepes nehézségi fok
    elif nehezfok in {'közepes','Közepes','normal','Normal'}:
        for j in range(1):
            gyumolcsok = ['', '', '', '', '', '', '', '', '', '']
            for i in range(10):
                huzott = random.choice(könyvtár)
                k = 0
                while k < 5:
                    if gyumolcsok[k] == huzott:
                        huzott = random.choice(könyvtár)
                        k = 0
                    else:
                        k += 1
                        
                gyumolcsok[i] = huzott
        randgyum = random.choice(gyumolcsok)
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('\nKiválasztottad a \tKözepes\t nehézségi fokot\n')
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('Jó szorakozást ;)')
        nehezseg = False

    #Nehéz nehézségi fok
    elif nehezfok in {'nehéz','Nehéz','hard','Hard'}:
        for j in range(1):
            gyumolcsok = ['', '', '', '', '', '', '', '', '', '', '\n', '', '', '', '', '', '', '', '', '' ]
            for i in range(20):
                huzott = random.choice(könyvtár)
                k = 0
                while k < 5:
                    if gyumolcsok[k] == huzott:
                        huzott = random.choice(könyvtár)
                        k = 0
                    else:
                        k += 1
                        
                gyumolcsok[i] = huzott
        randgyum = random.choice(gyumolcsok)
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('\nKiválasztottad a \tNehéz\t nehézségi fokot\n')
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('Jó szorakozást ;)')
        nehezseg = False


    else:
        for j in range(1):
            gyumolcsok = ['', '', '', '', '', '', '', '', '', '']
            for i in range(10):
                huzott = random.choice(könyvtár)
                k = 0
                while k < 5:
                    if gyumolcsok[k] == huzott:
                        huzott = random.choice(könyvtár)
                        k = 0
                    else:
                        k += 1
                        
                gyumolcsok[i] = huzott
        randgyum = random.choice(gyumolcsok)
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('\nKiválasztottad a \tKözepes\t nehézségi fokot\n')
        print('_--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--__--(OoO)--_')
        print('Jó szorakozást ;)')
        nehezseg = False



    
while folytat:
    
    print('---------------------')
    print('Segítségeid száma: ',tip)
    print('Élet',elet)
    print(gyumolcsok)    
    #Választási opció
    print('T\_o_/TT\_o_/TT\_o_/TT\_o_/TT\_o_/TT\_o_/T')
    
    valasz = input('\nVálasz mi következő lépés(segítség = 1/tippelés = 2): ')
    
    print('\nT\_o_/TT\_o_/TT\_o_/TT\_o_/TT\_o_/TT\_o_/T')
    #Ez a program rész felel a tipnél lévő kódra
    if valasz == "1" and tip > 0:
        number1 = True    
        while number1:    
            print('---------------------')
            #Ez írja ki menyi tipped maradt hátra
            print('Tipeid száma: ',tip)
            igennem = str(input('Szeretnéd e igénybe venni egy segítséget?(i/n): '))
            if igennem == 'i':
                tip = tip - 1
                print('---------------------')
                #Itt ki írja mik voltak az előző tippeid
                print(gyumolcsok)
                print('Ezek voltak az elözö tippek: ',kiesett)
                #Itt kérbe egy betűt a program
                bekertbetutip = str(input('Kérem az egyik szó kis kezdő betűjét: '))
                if tip > 0:
                    for szo in gyumolcsok:
                        if szo[0] == bekertbetutip and randgyum[0] != bekertbetutip:
                            print('---------------------')
                            kiesett.append(bekertbetutip)
                            print('Ez/Ezek a szavak estek ki: ', kiesett)
                            number1 = False
                        elif randgyum[0] == bekertbetutip:
                            print('...')
                else:
                    print('!!!!!!!!!!!!!!!!!!!!!')
                    print('Sajnálom de elfogytak a segitségeid :(')
                    print('!!!!!!!!!!!!!!!!!!!!!')
                    number1 = False
            elif igennem == 'n':
                number1 = False
            else:
                print('!!!!!!!!!!!!!!!!!!!!!')
                print('Ilyen nemlétezik')
                print('!!!!!!!!!!!!!!!!!!!!!')
    elif valasz == "2":
        print('...')
    elif valasz == "69420":
        print('\nCheat code activeted ;)\n')
        print('\n',randgyum,'\n')

    else:
        print('nem létező szám')
        number1 = False
    print('---------------------')
    #Itt kéri be a találgatáshoz való szót
    gyumtip = str(input('Válaszon egy gyümölcsöt az alábiak közül: '))       
    
    if elet <= 0:#Ez akkor jön fel ha az életed elérte a 0-át
        print('Sajnálom elfogytak az életeid. :(')
        print('A szó nem volt más mint: ',randgyum)
        folytat = False
        print('Enyi probálkozásból',talal)
        print('Élet',elet)
    elif gyumtip == randgyum:#Ez akkor jön fel ha sikerült ki találnod a szót
        print('---------------------')
        print('Gratulálok eltaláltad a gyümölcsöt')
        print('A szó nem volt más mint: ',randgyum)
        folytat = False
        talal = talal + 1
        print('Enyiböl sokerült ki találnod',talal)
        print('Élet',elet)
    else:#Ez a kód akkor jön fel ha rossz szót írsz be
        talal = talal + 1
        elet = elet - 1
        print('Nem talált hehe')
        print('Élet',elet)
        kiesett.append(gyumtip)






















'''
#Itt választja ki a program a szavakat amikböl majd kell választanod
    for j in range(1):
        gyumolcsok = ['', '', '', '', '', '']
        for i in range(6):
            huzott = random.choice(könyvtár)
            k = 0
            while k < 5:
                if gyumolcsok[k] == huzott:
                    huzott = random.choice(könyvtár)
                    k = 0
                else:
                    k += 1
                    
            gyumolcsok[i] = huzott
    #Itt választ ki a program egy szót
    randgyum = random.choice(gyumolcsok)
    #print(randgyum)
'''















'''
for i in range(nehezseg):
    for j in range(nehezseg):
        if i != j:
            print(end='\n')           
        else:
            gyumolcsok = []
            gyumolcsok.append(random.choice(könyvtár))

randgyum = random.choice(gyumolcsok)
'''
'''
gyumolcsok = []
gyumolcsok.clear()
while (len(gyumolcsok) < nehezseg):
    gyumolcsok.append(random.choice(könyvtár))
    randgyum = random.choice(gyumolcsok)
'''
'''
while nehezseg >= szam:
    gyumi = random.choice(könyvtár)
    gyumolcsok.append(gyumi)
    szam = szam + 1
randgyum = random.choice(gyumolcsok)
'''