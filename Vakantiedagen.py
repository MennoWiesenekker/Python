Totaal= 25
doorgaan = True
while doorgaan == True:
    CAO = str(input("Wilt u gebruik maken van de oude of nieuwe CAO? [oud/nieuw] "))
    if CAO == "o":
        x= 2
        v= 5
        doorgaan = False
    elif CAO == "n":
        x= 3
        v= 6
        doorgaan = False
    else:
        print("voer 'o' in voor 'oud' en 'n' in voor 'nieuw.'")
leeftijd = int(input("Hoe oud bent u? "))
dienstjaren = int(input("Hoe veel jaar bent u al in dienst? "))
if dienstjaren > 25 and dienstjaren <40:
    Totaal = Totaal + x
elif dienstjaren > 40:
    Totaal = Totaal + v

if leeftijd > 45 and leeftijd < 55:
    Totaal = Totaal + 1
elif leeftijd > 56 and leeftijd < 67:
    Totaal = Totaal + 2
    
print("U heeft recht op "+str(Totaal) +" vakantiedagen.")