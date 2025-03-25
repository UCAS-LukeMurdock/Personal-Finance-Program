# Personal Finance Project - Luke Murdock, Alishya Xavier, Alec George
# Alec George, Main
from entry_tracking import entry_tracking
from budget import budget_func
from goals import goal_menu

def menu(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this Personal Finance Program, where you can  it.")
    while True:
        choice = input("\n(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n")
        if choice == 1:
            entry_tracking()
        elif choice == 2:
            budget_func()
        elif choice == 3:
            goal_menu()
        elif choice == 4:
            print("Come Back Soon!")
            exit()     
        else:
            print("Something Broke")
            continue
menu()
#