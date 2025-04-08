# Personal Finance Project - Luke Murdock, Alishya Xavier, Alec George
# Alishya Xavier, Main File

from file_handler import read_file, write_file, remove_user
from entry_tracking import entry_tracking
from budget import budget
from goals import goal_menu
from currency import convert
from calculator import calc


def menu(): # Introduces the program and then lets the user choose one of the options
     
    while True:
        choice = input("\nWhat would you like to do?:\n1. track income & expense entries\n2. create a budget\n3. create savings goals\n4. convert currency\n5. use a calculator\n6. remove user\n7. log out\n\nYour choice here: ").strip()
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
            calc()
        elif choice == '6':
            confirm = input(f"\nAre you sure you want to remove your user?\n1. cancel\n2. confirm\n\nYour choice here: ").strip()
            if confirm == '2':
                remove_user()
                break
        elif choice == '7':
            print("You have logged out")
            break
        else:
            print("\nThat is not an option. Please try again...  (Please type the corresponding number)\n")

def sign_in(): # 
    user_profiles = read_file()
    for user in user_profiles:
        user["Active"] = False
    while True:
        sign_in_choice = input("\nWhat would you like to do?:\n1. log in\n2. sign up\n3. quit\n\nYour choice here: ").strip()
        if sign_in_choice == '1':
            found = False
            user_name = input('\nusername: ').strip()
            password = input('\npassword: ').strip()
            for ind, user in enumerate(user_profiles):
                if user_name == user['Name'] and password == user['Password']:
                    user_profiles[ind]["Active"] = True
                    write_file(user_profiles)
                    print('\nYou have logged in!')
                    found = True
                    menu()
                    user_profiles = read_file()
            if found == False:
                print('\nUsername or password couldn\'t be found')
                continue
        elif sign_in_choice == '2':
            sign_up_user_name = input('\nusername: ').strip()
            check = False
            for user in user_profiles:
                if sign_up_user_name == user['Name']:
                    print('\nThat username has already been taken.\n')
                    check = True
            if check == True:
                continue       
            sign_up_password = input('\npassword: ').strip()
            
            profile = {
                "Name": sign_up_user_name,
                "Password": sign_up_password,
                "Income": [],
                "Expense": [],


                "Goals": [],
                "Active": False,}
            user_profiles.append(profile)
            write_file(user_profiles)
            print("\nCreated new profile") #Now they go back and can go log in to that account

        elif sign_in_choice == '3':
            print('\n\nThank you for using this Personal Finance Program!\n\n\n')
            exit()
        else:
            print('\nThat is not an option. Try again...  (Please type the corresponding number)')
            
            
print("\n\n\nWelcome to this Personal Finance Program, where you can track entries, budget, and make savings goals.")
sign_in()


# README
# Check Everything