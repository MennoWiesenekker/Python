import random
getal = random.randint(1,100)
pogingen = 0
doorgaan = True

print("Welkom bij gok het getal, probeer het getal tussen de 1 en de 100 binnen zo min mogelijk pogingen te raden!")
while doorgaan == True:
    gok = int(input("Mijn gok voor het getal is: "))
    pogingen = pogingen + 1
    if gok == getal:
        if pogingen == 1:
            print("Super fantastisch, Je hebt het getal in 1 keer geraden!")
            doorgaan = False
        elif pogingen >= 2 and pogingen <= 4:
            print("Fantastisch, je hebt het getal in "+str(pogingen)+" keer geraden!")
            doorgaan = False
        elif pogingen >= 5 and pogingen <= 7:
            print("Prima, je hebt het getal in "+str(pogingen)+" keer geraden!")
            doorgaan = False
        elif pogingen >= 8 and pogingen <= 12:
            print("Goed, je hebt het getal in "+str(pogingen)+" keer geraden!")
            doorgaan = False
        elif pogingen >= 13 and pogingen <= 20:
            print("Goed, je hebt het getal in "+str(pogingen)+" keer geraden! Probeer de volgende keer of je het sneller kunt.")
            doorgaan = False

    else:
        if gok < getal:
            print("Nummer "+str(gok)+" is kleiner dan het getal.")
        elif gok > getal:
            print("Nummer "+str(gok)+" is groter dan het getal.")