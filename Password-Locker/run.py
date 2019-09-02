from Password import User
def create_user(fname,lname,number,username):
    new_user = User(fname,lname,number,username)
    return new_user

def save_user(user):
    user.save_user()