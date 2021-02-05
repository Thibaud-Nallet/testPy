import sys
sys.path.append("..")
from src.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_user_is_created(self):
        p = User("nallet", "thibaud", 1991)
        self.assertIsInstance(p, User)
    
    def test_annee_is_positive(self): 
        p = User("nallet", "thibaud", 1991)
        self.assertGreater(p.annee, 0)

if __name__ == '__main__': 
    unittest.main()