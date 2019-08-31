class User:
    user_list = []

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def find_by_number(cls, number):
        for user in cls.user_list:
            if user.phone_number == number:
                return user
