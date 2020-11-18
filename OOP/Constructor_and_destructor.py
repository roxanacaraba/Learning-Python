class Apartament:

    def __init__(self, numar_camere, suprafata, pret):

        self.numar_camere = numar_camere
        self.suprafata = suprafata
        self.pret = pret

    def printfunct(self):

        print("Constructorul a creat un apartament cu " + str(self.numar_camere) + " camere, cu o suprafata de " + str(self.suprafata) + " metri patrati si un pret de " + str(self.pret) + " $.")

    def __del__(self):
        print("Destructorul a sters apartamentul. ")

apartament = Apartament( 3, 60 , 82000)
apartament.printfunct()
del apartament