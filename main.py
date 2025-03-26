# Personal Finance Project - Luke Murdock, Alishya Xavier, Alec George
# Alishya Xavier, Main File

from file_handler import read_file, write_file
from entry_tracking import entry_tracking
from budget import budget
from goals import goal_menu
from currency import convert


def menu(): # Introduces the program and then lets the user choose one of the options
    print("\nWelcome to this Personal Finance Program, where you can track entries, budget, and make savings goals.")
    while True:
        choice = input("\nWhat would you like to do:\n1. Entry track\n2. Budget\n3. Savings goal\n4. Currency Converter\n5. Log out\nChoice: ")
        if choice == '1':
            entry_tracking()
        elif choice == '2':
            budget()
        elif choice == '3':
            goal_menu()
        elif choice == '4':
            convert()
        elif choice == '5':
            print("You have logged out")
            break     
        else:
            print("That is not an option. Please try again...")

def sign_in():
    user_profiles = read_file()
    for user in user_profiles:
        user["Active"] = False
    while True:
        sign_in_choice = input("\nWhat would you like to do:\n1. Log in\n2. Sign up\n3. Exit\nChoice: ")
        if sign_in_choice == '1':
            user_name = input('Username: ')
            password = input('Password: ')
            for ind, user in enumerate(user_profiles):
                if user_name == user['Name'] and password == user['Password']:
                    user_profiles[ind]["Active"] = True
                    write_file(user_profiles)
                    print('You have logged in!')
                    menu()
                else:
                    print('Either the username or password is incorrect.')
                    continue
        elif sign_in_choice == '2':
            sign_up_user_name = input('Username: ')
            sign_up_password = input('Password: ')
            profile = {
                "Name": sign_up_user_name,
                "Password": sign_up_password,
                "Income": [],
                "Expense": [],
                "Goals": [],
                "Active": False,}
            write_file(user_profiles.append(profile))
            print("Created New Profile") #Now they go back and can go log in to that account

        elif sign_in_choice == '3':
            print('\nThank you for using your Personal Finance Program!\n\n\n')
            exit()
        else:
            print('That is not an option. Try again...')
            
            
#We should figure out user index so that we can know which user is signed in etc.
    # We can either put it through parameters, put it on the file and use a function to find the signed in user, or global it somehow
# Get rid of Budget on file
print("\n\nPersonal Finance Program")
sign_in()