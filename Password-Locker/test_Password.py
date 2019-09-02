import unittest
from Password import User 
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Happy","Kawinzi","0712345678","hkawinzi@gmail.com") 
    
    def test_init(self):

        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.username,"hkawinzi@gmail.com")

    def test_save_user(self):
        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.username,"hkawinzi@gmail.com")
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        User.user_list = []
    
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def delete_user(self):
        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()
        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),2)
        User.user_list.remove(self) 

    def test_find_user_by_first_name(self):
        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com")
        test_user.save_user()

        found_user = User.find_by_first_name("Test")
        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com")
        test_user.save_user()

        user_exists = User.user_exists("Test")

        self.assertTrue(user_exists)

    def test_display_all_contact(self):
        self.assertEqual(User.display_users(),User.user_list)

    def test_copy_username(self):
        self.new_user.save_user()
        User.copy_username("0712345678")
        
        self.assertEqual(self.new_user.username,pyperclip.paste())
        
if __name__ == '__main__':
    unittest.main()