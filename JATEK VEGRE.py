import random
gondolt = random.randint(1,100)

print("Gondoltam egy számot 1 és 100 között. \nTaláld ki!")
tip = 0
tipszam = 0
while gondolt != tip:
    tip = int(input("A szám amire gondoltál az: "))
    tipszam +=1
    if tip < gondolt:
        print("Kicsi")
    elif tip > gondolt:
            print("Nagy") 
print("Talált")
print("A tipeléseid száma", tipszam)
'''
while gondolt != tip:
    tip = int(input("A szám amire gondoltál az: "))
    if tip < gondolt:
        print("Kicsi")
    elif tip > gondolt:
            print("Nagy")  
    else:
        print("Talált")

kesz=False
while not kesz:
    tip = int(input("A szám amiregondoltál az: "))
    if tip < gondolt:
        print("Kicsi")
    elif tip > gondolt:
            print("Nagy")  
    else:
        print("Talált 2.")
        kesz=True

while True:
    tip = int(input("A szám amiregondoltál az: "))
    if tip < gondolt:
        print("Kicsi")
    elif tip > gondolt:
            print("Nagy")  
    else:
        print("Talált 3.")
        break
'''

