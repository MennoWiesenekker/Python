#Menno Wiesenekker
#18-12-2020
#233884
#Deze code is een rekenmachine die steeds doorrekend met het eerste getal.
welkom = print("Welkom bij de rekenmachine, deze code zal constant doorrekenen met de uitkomst.")
stop = print("Om de rekenmachine af te sluiten voert u '=' in.")
def optellen(g1,g2):
    return g1 + g2

def min(g1,g2):
    return g1 * g2

def keer(g1,g2):
    return g1 * g2

def delen(g1,g2):
    return g1 / g2

doorgaan = True
#vragen om getal 1, dit staat uiten de loop zodat je hiermee kan doorwerken als je meerdere sommen wilt doen zoals:  (5+5)*3= 30
g1= int(input("Voer nummer een in: "))
while doorgaan == True:
    #vragen om de operator
    wat = input("Wat moet er gebeuren? kies uit[+ , - , * , :] ")
    #controleren of '=' is ingevuld, zo niet dan word de som uitgevoerd
    if wat == "=":
        print("uitkomst =", str(g1))
        print("Rekenmachine stopt, Totziens...")
        doorgaan = False
    else:
        #g2 staat buiten de stop loop zodat je niet nog een tweede getal moet invullen voor je code stopt, dit is puur gebruiksvriendelijkheid
        g2= int(input("Voer nummer twee in: "))
    #in deze hele if loop word de correcte opperator gekozen en de  uitkomst word bij g1 ingevuld
    if wat == "+":
        response = optellen(g1,g2)
        print(str(g1), "+", str(g2), "=", str(response))
        g1= response
    elif wat == "-":
        response = keer(g1,g2)
        print(str(g1), "-", str(g2), "=", str(response))
        g1= response
    elif wat == "*":
        response = keer(g1,g2)
        print(str(g1), "x", str(g2), "=", str(response))
        g1= response
    elif wat == ":":
        response = delen(g1,g2)
        print(str(g1), ":", str(g2), "=", str(response))
        g1= response
    else:
        #output als er een verkeerde operator word ingevuld.
        print("Vul een geldige input in, kies uit [+ , - , * , :]")