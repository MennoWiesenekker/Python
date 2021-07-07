print("Let op, voer de invoer in met de aangegeven afkortingen. Deze code is hoofdlettergevoelig.")
print("Kies bij het invoeren uit [euro,dollar,gbp,dkk]")
def berekening(invoer,naar,bedrag):
    if invoer == "euro":
        if naar == "dollar":
            return "$" + str("{: .2f}".format(bedrag /100 *116))
        elif naar == "gbp":
            return "£" + str("{: .2f}".format(bedrag /100 *90))
        elif naar == "dkk":
            return "Kr: " + str("{: .2f}".format(bedrag /100 *735))
    elif invoer == "dollar":
        if naar == "euro":
            return "€" + str("{: .2f}".format(bedrag /100 *86))
        elif naar == "gbp":
            return "£" + str("{: .2f}".format(bedrag /100 *78))
        elif naar == "dkk":
            return "Kr: " + str("{: .2f}".format(bedrag /100 *640))
    elif invoer == "gbp":
        if naar == "euro":
            return "€" + str("{: .2f}".format(bedrag /100 *111))
        elif naar == "dollar":
            return "$" + str("{: .2f}".format(bedrag /100 *129))
        elif naar == "dkk":
            return "Kr: " + str("{: .2f}".format(bedrag /100 *826))
    elif invoer == "dkk":
        if naar == "euro":
            return "€" + str("{: .2f}".format(bedrag /100 *13))
        elif naar == "dollar":
            return "$" + str("{: .2f}".format(bedrag /100 *16))
        elif naar == "gbp":
            return "£" + str("{: .2f}".format(bedrag /100 *12))
    else:
        print("Controleer de ingevoerde gegevens op eventuele fouten.")

invoer= input(str("Invoer: "))
naar= input(str("Uitvoer: "))
bedrag= int(input("Bedrag in " +invoer + ":"))

print(str(bedrag), invoer + " in "+ naar , "is "+berekening(invoer,naar,bedrag))