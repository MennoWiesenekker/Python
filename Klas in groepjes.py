import random
doorgaan = 5
doorgaan2 = 4
groepje = 1
klas= ["Kaya","Debbie","Laurence","Robbin","Mariska","Rick","Kalle","Wilke","Thomas K","Tim","Menno","Jonathan","Sem","Jan", "willem","Damiël","Nimue","Rowin","Thomas E","Edzer","Simon","Mathijs","Ate-Jan"]
while doorgaan >0:

    print("GROEPJE "+str(groepje)+":")
    while doorgaan2 >0:
        leerling= random.choice(klas)
        klas.remove(leerling)
        print(leerling)
        doorgaan2 = doorgaan2 - 1
    groepje = groepje + 1
    doorgaan = doorgaan - 1
    doorgaan2 = doorgaan2 = 4