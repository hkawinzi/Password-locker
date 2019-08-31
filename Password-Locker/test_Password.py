import unittest
from User import User 

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_User = User("James","Muriuki","0712345678","james@ms.com") # create contact object
    
    def test_init(self):
