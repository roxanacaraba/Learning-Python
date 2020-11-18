#Single level inheritence

class Student:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

class Carnet(Student):

    def __init__(self,nume, varsta, institutie_invatamant, specializare):
        self.institutie_invatamant = institutie_invatamant
        self.specializare = specializare

        Student.__init__(self, nume, varsta)

    def print(self):
        print("Studentul cu numele " + self.nume + " e inmatriculat la specializarea " + self.specializare)


carnet_student1= Carnet("Andrei Ionescu", 20, " UMF", "BFKT")
carnet_student1.print()

# Multiple inheritence:

class Animale:

    def __init__(self, rasa, tip):
        self.rasa = rasa
        self.tip = tip

class Pasari:

    def __init__(self, nume):
        self.nume = nume

class ZOO(Animale, Pasari):

    def __init__(self, rasa, tip, nume, numar_total_animale):
        self.numar_total_animale = numar_total_animale
        Animale.__init__(self, rasa, tip)
        Pasari.__init__(self, nume)

    def print(self):
        print("This zoo has " + str(self.numar_total_animale) + " animals: " + self.tip + " " + self.rasa + " and " + self.nume + " birds")

zoo= ZOO("dogs", "wilds", "flamingo", 12)
zoo.print()

# Multilevel Inferitence

class ALfabet:

    def __init__(self, litera):
        self.litera = litera

class Cuvinte(ALfabet):

    def __init__(self, litera, cuvant_care_incepe_cu_litera):
        self.cuvant_care_incepe_cu_litera = cuvant_care_incepe_cu_litera
        ALfabet.__init__(self, litera)

class Propozitie(Cuvinte):

    def __init__(self, litera, cuvant_care_incepe_cu_litera , propozitie_care_incepe_cu_cuvant):
        self.propozitie_care_incepe_cu_cuvant = propozitie_care_incepe_cu_cuvant
        ALfabet.__init__(self, litera)
        Cuvinte.__init__(self,litera, cuvant_care_incepe_cu_litera)

    def print(self):
        print(self.propozitie_care_incepe_cu_cuvant)

propozitie = Propozitie("A", "Alfabet", "Alfabetul formeaza cuvinte care formeaza propozitii")
propozitie.print()