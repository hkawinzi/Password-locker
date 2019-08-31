import unittest
from Password import User 

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Happy","Kawinzi","0712345678","hkawinzi@gmail.com") 
    
    def test_init(self):

        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"hkawinzi@gmail.com")

if __name__ == '__main__':
    unittest.main()