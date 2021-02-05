import sys
sys.path.append("..")
from src.user import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.p = User("nallet", "thibaud", 1991)

    #verif création d'un user
    def test_user_is_created(self):
        self.assertIsInstance(self.p, User)

    #name 
    def test_name_is_str(self): 
        self.assertIsInstance(self.p.name, str)
    
    def test_name_is_short(self): 
        self.assertGreater(len(self.p.name), 0)

    def test_name_is_long(self): 
        self.assertLess(len(self.p.name), 25)

    #firstname 
    def test_firstname_is_str(self): 
        self.assertIsInstance(self.p.firstname, str)
    
    def test_firstname_is_short(self): 
        self.assertGreater(len(self.p.firstname), 0)

    def test_firstname_is_long(self): 
        self.assertLess(len(self.p.firstname), 25)

    #Annnée
    def test_annee_is_positive(self): 
        self.assertGreater(self.p.annee, 0)

    def test_annee_is_int(self): 
        self.assertIsInstance(self.p.annee, int)

if __name__ == '__main__': 
    unittest.main()