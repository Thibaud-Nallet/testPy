class User:
    def __init__(self, name, firstname, annee):
        self.name = name
        self.firstname = firstname
        self.annee = annee
    
    def __str__(self):
        return f"[Nom : {self.name} / Prenom : {self.firstname} / Annee : {self.annee}]"