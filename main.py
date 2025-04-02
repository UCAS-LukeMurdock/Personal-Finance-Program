# Personal Finance Project - Luke Murdock, Alishya Xavier, Alec George
# Alishya Xavier, Main File

from file_handler import read_file, write_file
from entry_tracking import entry_tracking
from budget import budget
from goals import goal_menu
from currency import convert


def menu(): # Introduces the program and then lets the user choose one of the options
    
    while True:
        choice = input("\nWhat would you like to do:\n1. Track entries\n2. Budget\n3. Savings goals\n4. Currency Converter\n5. Log out\nChoice: ").strip()
        if choice == '1':
            entry_tracking()
            pass
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
        sign_in_choice = input("\nWhat would you like to do:\n1. Log in\n2. Sign up\n3. Quit\nChoice: ").strip()
        if sign_in_choice == '1':
            found = False
            user_name = input('Username: ').strip()
            password = input('Password: ').strip()
            for ind, user in enumerate(user_profiles):
                if user_name == user['Name'] and password == user['Password']:
                    user_profiles[ind]["Active"] = True
                    write_file(user_profiles)
                    print('\nYou have logged in!')
                    found = True
                    menu()
            if found == False:
                print('\nEither the username or password is incorrect.')
                continue
        elif sign_in_choice == '2':
            sign_up_user_name = input('Username: ').strip()
            sign_up_password = input('Password: ').strip()
            profile = {
                "Name": sign_up_user_name,
                "Password": sign_up_password,
                "Income": [],
                "Expense": [],
                "Goals": [],
                "Active": False,}
            user_profiles.append(profile)
            write_file(user_profiles)
            print("\nCreated New Profile") #Now they go back and can go log in to that account

        elif sign_in_choice == '3':
            print('\n\nThank you for using your Personal Finance Program!\n\n\n')
            exit()
        else:
            print('That is not an option. Try again...')
            
            
print("\n\n\nWelcome to this Personal Finance Program, where you can track entries, budget, and make savings goals.")
sign_in()
