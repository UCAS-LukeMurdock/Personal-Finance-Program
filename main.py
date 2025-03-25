# Personal Finance Project - Luke Murdock, Alishya Xavier, Alec George
# Alec George, Main
from file_handler import read_file, write_file
from entry_tracking import entry_tracking
from budget import budget
from goals import goal_menu
from currency import convert



def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this Personal Finance Program, where you can track entries, budget, and make savings goals.")
    while True:
        choice = input("What would you like to do:\n1. Entry track\n2. Budget\n3. Savings goal\n4. Currency Converter\n5. Log out\nChoice: ")
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
            exit()     
        else:
            print("That is not an option. Please try again...")
            

def sign_in():
    user_profiles = read_file()
    while True:
        sign_in_choice = input("What would you like to do:\n1. Log in\n2. Sign up\n3. Exit\nChoice: ")
        if sign_in_choice == '1':
            user_name = input('Username: ')
            password = input('Password: ')
            for user in user_profiles:
                if user_name == user['Name'] and password == user['Password']:
                    print('You have logged in!')
                    menu() #Could break
                else:
                    print('Either the username or password is incorrect.')
                    continue
        elif sign_in_choice == '2':
            sign_up_user_name = input('Username: ')
            sign_up_password = input('Password: ')
            #Save what they wrote into the file for their account
            write_file(user_profiles)
            # Luke will work on it
            continue #Now they go back and can go log in to that account

        elif sign_in_choice == '3':
            print('Thankyou for using your Personal Finance Program!')
            exit()
        else:
            print('That is not an option. Try again...')
            
            
                

#We should figure out user index so that we can know which user is signed in etc.
sign_in()
