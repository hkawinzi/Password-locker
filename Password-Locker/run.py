#!/usr/bin/env python3.6
from Password import User


def create_user(fname, lname, password, username):
    new_user = User(fname, lname, password, username)
    return new_user

def save_user(user):
    user.save_user()


def del_user(user):
    user.delete_user()


def find_user(name):
    return User.find_by_first_name(name)


def check_existing_users(name):
    return User.user_exists(name)


def display_users():
    return User.display_users()


def main():
    print("Use these short codes to continue with signing up : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")
    short_code = input().lower()
    if short_code == 'cu':
            print("New user")
            print("-"*10)
            print ("First name ....")
            f_name = input()
            print("Last name ...")
            l_name = input()
            print("password ...")
            p_number = input()
            print("username ...")
            e_name = input()
            save_user(create_user(f_name,l_name,p_number,e_name)) # create and save new user.
            print ('\n')
            print(f"New user {f_name} {l_name} {e_name} created")
            print ('\n')
    elif short_code == 'du':
            if display_users():
                    print("Here is a list of all your users")
                    print('\n')
                    for user in display_users():
                            print(f"{user.first_name} {user.last_name} .....{user.password}")
                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any users saved yet")
                    print('\n')
    elif short_code == 'fu':
            print("Enter the first name you want to search for")
            search_first_name = input()
            if check_existing_users(search_first_name):
                    search_user = find_user(search_first_name)
                    print(f"{search_user.first_name} {search_user.last_name}")
                    print('-' * 20)
                    print(f"password.......{search_user.first_name}")
                    print(f"username.......{search_user.email}")
            else:
                    print("That user does not exist")
    elif short_code == "ex":
            print("Bye .......")
            # break
    else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()