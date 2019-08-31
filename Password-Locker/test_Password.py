import unittest
from User import User 

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_User = User("Happy","Kawinzi","0712345678","hkawinzi@gmail.com") 
    
    def test_init(self):

        self.assertEqual(self.new_User.first_name,"Happy")
        self.assertEqual(self.new_User.last_name,"Kawinzi")
        self.assertEqual(self.new_User.phone_number,"0712345678")
        self.assertEqual(self.new_User.email,"hkawinzi@gmail.com")

if __name__ == '__main__':
    unittest.main()