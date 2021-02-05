from datetime import date

class User:
    def __init__(self, name, firstname, annee):
        assert name.isalnum(), "Attribut 'name' : doit être alphanumérique (a-z, A-Z et 0-9)"
        assert len(name) > 3 and len(name) < 25, "Attribut 'name' : nombre de caractères compris entre 3 et 25"
        assert firstname.isalnum(), "Attribut 'firstname' : doit être alphanumérique (a-z, A-Z et 0-9)"
        assert len(firstname) > 3 and len(firstname) < 25, "Attribut 'firstname' : nombre de caractères compris entre 3 et 25"
        assert isinstance(annee, int), "Attribut 'annee' : doit être un entier"
        assert annee > 1900 and annee < 2021, "Attribut 'annee' : doit être compris entre 1900 et 2021"

        self.name = name
        self.firstname = firstname
        self.annee = annee
    
    def __str__(self):
        date_day = date.today()
        age = date_day.year - self.annee

        return f"Bonjour {self.firstname} {self.name} Vous avez : {age} ans !"