import pyperclip


class User:
    users_list = []

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username

    def save_user(self):
        User.users_list.append(self)

   

class Credentials:
    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):
        current_user = ''
        for user in User.credentials_list:
            if (user.username == username and user.password == password):
                current_user = user.username
        return current_user
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username

    @classmethod
    def find_by_first_name(cls, name):
        for credential in cls.credentials_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exists(cls, name):
        for user in cls.credentials_list:
            if user.first_name == first_name:
                    return True

        return False

    @classmethod
    def display_users(cls):
        return cls.credentials_list

    @classmethod
    def copy_username(cls, name):
        user_found = User.find_by_first_name(name)
        pyperclip.copy(user_found.username)


    @classmethod
    def find_by_first_name(cls, name):
        for user in cls.credentials_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def credential_exists(cls, name):
        for user in cls.credentials_list:
            if user.first_name == first_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def copy_credential(cls, name):
        user_found = User.find_by_first_name(name)
        pyperclip.copy(user_found.username)

        
    def save_credentials(self):
        Credentials.credentials_list.append(self)
        
    @classmethod
    def display_credentials(cls,user_name):
        credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                credentials_list.append(credential)
        return credentials_list
    
    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_credentials(cls,account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def find_credentials(cls,account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
