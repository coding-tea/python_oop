

class conseiller:
    def __init__(self, matricule, nom, prenom, codecomplexe, nombreVisites, codeSecret):
        self._matricule = matricule
        self._nom = nom
        self._prenom = prenom
        self._codecomplexe = codecomplexe
        self._nombreVisites = nombreVisites
        self._codeSecret = codeSecret

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