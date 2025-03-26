# Alishya Xavier, Income and Expenses File
import datetime as dt
from visual import graph_menu
from file_handler import read_file, find_active, write_file
'''
            If they want to view total income and expenses
                Input is they want to see data visualization or time period
                If data visualization
                    Call displaying graph function
                If time period
                    INPUT specified time period
                    DISPLAY total income and expenses for time period
            If they want to exit
                exit to main menu(break out of loop)
'''

def entry_tracking():
    users = read_file()
    user_ind = find_active(users)
    while True:
        options = input('\nWhat would you like to do?\n1. Add income entry\n2. Add expense entry\n3. View total income and expenses\n4. Exit\n\nChoice: ')
        if options == '1':
            income = input('How much income are you adding: ')
            source = input('What is the source of your income: ')
            entry = [dt.datetime.now(), income, source]
            users[user_ind]['Income'].append(entry)
            write_file(users)
        elif options == '2':
            expense = input('How much expense are you adding: ')
            category = input('What is the category of your expense: ')
            entry = [dt.datetime.now(), expense, category]
            users[user_ind]['Expense'].append(entry)
            write_file(users)
        elif options == '3':
            choice = input('\nWhat do you want to see?\n1. Data visualization\n2. Time period\n\nChoice: ')
            if choice == '1':
                graph_menu()
            elif choice == '2':
                #Working on it
            else:
                print('That is not an option. Try again...')

        elif options == '4':
            break
        else:
            print('That is not an option. Try again...')
