import pyperclip
class User:
    user_list = []

    def __init__(self, first_name, last_name, phone_number, username):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.username = username

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def find_by_first_name(cls, name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exists(cls,name):
        for user in cls.user_list:
            if user.first_name == first_name:
                    return True

        return False

    @classmethod
    def display_users(cls):
        return cls.user_list

    @classmethod
    def copy_username(cls,name):
        user_found = User.find_by_first_name(name)
        pyperclip.copy(user_found.username)
