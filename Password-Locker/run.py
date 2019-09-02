from Password import User


def create_user(fname, lname, number, username):
    new_user = User(fname, lname, number, username)
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


def main():
    print("What is your first name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                print(
                    "Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")

                short_code = input().lower()

                if short_code == 'cu':
                    print("New user")
                    print("-"*10)

                    print("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("username ...")
                    u_name = input()

                    # create and save new user.
                    save_users(create_user(f_name, l_name, p_number, u_name))
                    print('\n')
                    print(f"New User {f_name} {l_name} created")
                    print('\n')

                elif short_code == 'du':

                    if display_users():
                        print("Here is a list of all your users")
                        print('\n')

                        for user in display_users():
                            print(
                                f"{user.first_name} {user.last_name} .....{user.phone_number}")

                        print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

                elif short_code == 'fu':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_users(search_number):
                        search_user = find_user(search_number)
                        print(f"{search_user.first_name} {search_user.last_name}")
                        print('-' * 20)

                        print(f"Phone number.......{search_user.phone_number}")
                        print(f"username.......{search_user.email}")
                    else:
                        print("That user does not exist")

                elif short_code == "ex":
                    print("Bye .......")
                    break
                else:
                    print("I really didn't get that. Please use the short codes")

if __name__ = '__main__':
    main()
