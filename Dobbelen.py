import random
doorgaan = 5
Beurt = 1
totaal = 0
dobbelsteen= ["1","2","3","4","5","6"]
Vraag = input(str("Wil je dobbelen? [j/n]"))
if Vraag == "j":
    while doorgaan >0:
        Gooi = random.choice(dobbelsteen)
        print("Beurt " +str(Beurt) +"= "+str(Gooi))
        totaal = totaal + int(Gooi)
        doorgaan = doorgaan - 1
        Beurt = Beurt + 1
        if doorgaan == 0:
            print("Totaal= "+str(totaal))
            dgvraag= input(str("Nog een keer? [j/n]"))
            if dgvraag == "j":
                doorgaan = doorgaan + 5
                totaal = totaal = 0
                Beurt = Beurt = 1
            else:
               print("Bedankt voor het gebruiken van de dobbeler!")

    
else:
    print("Totziens!")