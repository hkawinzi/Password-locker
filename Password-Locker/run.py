from Password import User
def create_user(fname,lname,number,username):
    new_user = User(fname,lname,number,username)
    return new_user

def save_user(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def find_user(name):
    return User.find_by_first_name(name)

def check_existing_users(name):
    return User.user_exists(name)

def display_user():
    return User.display_users()
    