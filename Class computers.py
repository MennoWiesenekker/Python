#Menno Wiesenekker
#233884
#07-01-2021
#Class computer code
class computer:
    def __init__(self,merk,systeem,model):
        self._merk = merk
        self._systeem = systeem
        self._model = model
        self._actief = False

    def boot(self):
        #controleren of hij al aan staat
        if self._actief == False:
            #code voor opstarten
            print(f"Welkom bij {self._merk} model {self._model}, {self._systeem}")
            self._actief = True
        else:
            #error message
            print("Error! Device is already on.")

    def shutdown(self):
        #code voor afsluiten van de pc
        if self._actief == True:
            print(f"{self._systeem} is shutting down...")
            self._actief = False

        else:
            print("Error! Can't shut down what isn't active.")
    
    def reboot(self):
        #code voor rebooten
        if self._actief == True:
            print("Rebooting...")
            computer.boot(self)
        else:
            print("Error! Can't reboot what isn't active.")

gamepc= computer('Radeon','Windows','GMX3')
werkpc= computer('Intel','Windows','WorkstX')
laptop= computer('Mac','MacOS','Macbook Pro 17')
gamepc.boot()
gamepc.reboot()
gamepc.shutdown()
werkpc.boot()
werkpc.reboot()
werkpc.shutdown()
laptop.boot()
laptop.reboot()
laptop.shutdown()