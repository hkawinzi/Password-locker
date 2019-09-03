#!/usr/bin/env python3.6
from Password import User
import string


def create_user(fname, lname, password, username):
    new_user = User(fname, lname, password, username)
    return new_user


def save_user(user):
    User.save_user(user)


def del_user(user):
    user.delete_user()


def verify_user(username, password):
    verifying_user = Credentials.verify_user(username, password)
    return verifying_user


def check_existing_users(name):
    return User.user_exists(name)


def generate_password(self):
    password = Credentials.generate_password(self)
    return password


def display_users(user_name):
    return User.display_Credential(user_name)


def main():
    print("Use these short codes to continue with signing up : cu - create a new user, li - log in, du - display users, fu -find a user, ex -exit the user list ")
    short_code = input().lower()
    if short_code == 'cu':
        print("New user")
        print("-"*10)
        print("First name ....")
        fname = input()
        print("Last name ...")
        lname = input()
        print("password ...")
        password = input()
        print("username ...")
        username = input()
        # create and save new user.
        save_user(create_user(fname, lname, password, username))
        print('\n')
        print(f"New user {fname} {lname}  created")
        print('\n')

    elif short_code == 'li':
        print('\n')
        print("Enter your details below to log in:")
        print('\n')

        user_name = input("Enter your user_name: ")
        print("-" * 10)
        password = input("Enter your password: ")
        print("-" * 10)
        user_exists = verify_user(user_name, password)
        if user_exists == user_name:

            print('\n')
            print(f"Welcome back {user_name}. Please choose an option.")

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

            while True:
             print("-"*10)
             print("Use the following codes: cre - create new credentials, dis - display credentials, fin - find credentials by account_name, del - delete credentials, ex - exit")
            nav_code = input().lower()

            if nav_code == 'cre':
                print("Enter credentials(account name,username,and password) below: ")
                account_name = input(
                    "Enter the account\'s name e.g Instagram: ")
                username = input(
                    "Enter your username for the account you have provided: ")
                while True:
                    print(
                        "Use these short codes: gen - generate a new password, exis - enter an existing password, ex - exit")
                    pass_choice = input()

                    if pass_choice == 'exis':
                        password = input("Enter your existing password: ")
                        break

                    elif pass_choice == 'gen':
                        password = generate_password(alphabet)
                        break

                    elif pass_choice == 'ex':
                        break

    elif short_code == "ex":
        print("Bye .......")
        # break
    else:
        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
