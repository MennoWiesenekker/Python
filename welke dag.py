def welkedag(dag,jaar):
    if jaar % 4 == 0:
        #Wel een schrikkeljaar
        if (31 > dag):
            print("Deze dag valt op "+str(dag)+" Januari.")
        elif (32 <= dag) and (60 > dag):
            print("Deze dag valt op "+str(dag - 31)+" Februari.")
        elif (61 <= dag) and (91 > dag):
            print("Deze dag valt op "+str(dag - 60)+" Maart.")
        elif (92 <= dag) and (122 > dag):
            print("Deze dag valt op "+str(dag - 90)+" April.")
        elif (122 <= dag) and (153 > dag):
            print("Deze dag valt op "+str(dag - 121)+" Mei.")
        elif (153 <= dag) and (183 > dag):
            print("Deze dag valt op "+str(dag - 152)+" Juni.")
        elif (183 <= dag) and (214 > dag):
            print("Deze dag valt op "+str(dag - 182)+" Juli.")
        elif (214 <= dag) and (245 > dag):
            print("Deze dag valt op "+str(dag - 213)+" Augustus.")
        elif (245<= dag) and (275> dag):
            print("Deze dag valt op "+str(dag - 244)+" September.")
        elif (275<= dag) and (306> dag):
            print("Deze dag valt op "+str(dag - 274)+" Oktober.")
        elif (306<= dag) and (336> dag):
            print("Deze dag valt op "+str(dag - 305)+" November.")
        elif (336<= dag) and (366> dag):
            print("Deze dag valt op "+str(dag - 335)+" December.")
        else:
            print("Ongeldig dagnummer, kies een getal tussen de 1 en de 366.")
    #Geen schrikkeljaar
    else:
        if (31 > dag):
            print("Deze dag valt op "+str(dag)+" Januari.")
        elif (32 <= dag) and (59 > dag):
            print("Deze dag valt op "+str(dag - 31)+" Februari.")
        elif (60 <= dag) and (90 > dag):
            print("Deze dag valt op "+str(dag - 59)+" Maart.")
        elif (91 <= dag) and (120 > dag):
            print("Deze dag valt op "+str(dag - 90)+" April.")
        elif (121 <= dag) and (152 > dag):
            print("Deze dag valt op "+str(dag - 120)+" Mei.")
        elif (153 <= dag) and (183 > dag):
            print("Deze dag valt op "+str(dag - 152)+" Juni.")
        elif (184 <= dag) and (215 > dag):
            print("Deze dag valt op "+str(dag - 183)+" Juli.")
        elif (216 <= dag) and (247 > dag):
            print("Deze dag valt op "+str(dag - 215)+" Augustus.")
        elif (244<= dag) and (273> dag):
            print("Deze dag valt op "+str(dag - 243)+" September.")
        elif (274<= dag) and (304> dag):
            print("Deze dag valt op "+str(dag - 273)+" Oktober.")
        elif (305<= dag) and (334> dag):
            print("Deze dag valt op "+str(dag - 304)+" November.")
        elif (335<= dag) and (365> dag):
            print("Deze dag valt op "+str(dag - 334)+" December.")
        elif (dag == 366):
            print("dag 366 bestaat niet, geen schrikkeljaar.")
        else:
            print("Ongeldig dagnummer, kies een getal tussen de 1 en de 366.")

#Input vraag
jaar = int(input("Vul een jaargetal in: "))
dag = int(input("Vul uw dag in in een geheel getal: "))

#uitvoer code
welkedag(dag,jaar)