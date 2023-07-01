

class conseiller:
    def __init__(self, matricule ='', nom='', prenom='', codecomplexe='', nombreVisites='', codeSecret=''):
        try :
            if len(codeSecret) <= 3:
                raise Exception('codeSecret must be more than 3 character')
            self._matricule = matricule
            self._nom = nom
            self._prenom = prenom
            self._codecomplexe = codecomplexe
            self._nombreVisites = nombreVisites
            self._codeSecret = codeSecret
        except Exception as error:
            print('Error! ', error)

    @property
    def matricule(self):
        return self.matricule
    
    @matricule.setter
    def matricule(self, newMatricule):
        self.matricule = newMatricule

    @property
    def nom(self):
        return self.nom
    
    @nom.setter
    def nom(self, newNom):
        self.nom = newNom

    def __str__(self):
        return f'matricule {self.matricule} nom {self.nom}'