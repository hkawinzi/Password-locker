import unittest
from Password import User 
from Password import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Happy","Kawinzi","12345678","hkawinzi@gmail.com") 
    
    def test_init(self):

        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.password,"12345678")
        self.assertEqual(self.new_user.username,"hkawinzi@gmail.com")

    def test_save_user(self):
        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.password,"12345678")
        self.assertEqual(self.new_user.username,"hkawinzi@gmail.com")
        self.new_credential.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)

class TestCreditals(unittest.TestCase):
    def setUp(self):
        self.new_account = Credentials("Happy","Kawinzi","12345678","hkawinzi@gmail.com") 
    
    def test_init(self):

        self.assertEqual(self.new_user.first_name,"Happy")
        self.assertEqual(self.new_user.last_name,"Kawinzi")
        self.assertEqual(self.new_user.password,"12345678")
        self.assertEqual(self.new_user.username,"hkawinzi@gmail.com")

    def tearDown(self):
        Credentials.credentials_list = []
    
    def test_save_multiple_credentials(self):
        self.new_user.save_credentials()
        test_account = Credentials("Test","user","12345678","test@user.com") 
        test_account.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def delete_credentials(self):
        self.new_credential.save_credentials()
        test_account = Credentials("Test","user","12345678","test@user.com") # new user
        test_account.save_credentials()
        self.new_credential.delete_credentials()# Deleting a user object
        self.assertEqual(len(Credentials.credentials_list),2)
        Credentials.credentials_list.remove(self) 

    def test_find_credential_by_first_name(self):
        self.new_credential.save_credentials()
        test_account = Credentials("Test","user","11223344","test@user.com")
        test_account.save_credentials()

        found_credential = Credentials.find_by_first_name("Test")
        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        self.new_credential.save_credentials()
        test_account = Credentials("Test","user","11223344","test@user.com")
        test_account.save_credentials()

        credential_exists = Credentials.credential_exists("Test")

        self.assertTrue(user_exists)

    def test_display_all_credentials(self):
        self.assertEqual(Credentials.display_credentials_list()

    def test_copy_username(self):
        self.new_credential.save_credentials()
        Credentials.copy_username("12345678")
        
        self.assertEqual(self.new_credential.username,pyperclip.paste())

    def test_save_credentials(self):
        self.new_account.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
        self.new_account.save_credentials()
        test_account = Credentials("Happy","Kawinzi","12345678","hkawinzi@gmail.com") #new credential
        test_account.save_credentials()
        
        self.new_account.delete_credentials() #deleting a credential(account) object
        self.assertEqual(len(Credentials.credentials_list),1)
        
if __name__ == '__main__':
    unittest.main()