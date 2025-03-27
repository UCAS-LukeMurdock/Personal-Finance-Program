# Alishya Xavier, Income and Expenses File
import datetime as dt
from visual import graph_menu
from file_handler import read_file, find_active, write_file
'''
                If time period
                    INPUT specified time period
                    DISPLAY total income and expenses for time period
'''

def entry_tracking():
    users = read_file()
    user_ind = find_active(users)
    while True:
        options = input('\nWhat would you like to do?\n1. Add income entry\n2. Add expense entry\n3. View total income and expenses\n4. Exit\n\nChoice: ')
        if options == '1':
            income = input('How much income are you adding: ')
            source = input('What is the source of your income: ')
            entry = [str(dt.datetime.now()), income, source]
            users[user_ind]['Income'].append(entry)
            write_file(users)
        elif options == '2':
            expense = input('How much expense are you adding: ')
            category = input('What is the category of your expense(housing, food, utilities, transportation, insurance, or other): ')
            if category == 'housing' or category == 'food' or category == 'utilities' or category == 'transportation' or category == 'insurance' or category == 'other':
                entry = [str(dt.datetime.now()), expense, category]
                users[user_ind]['Expense'].append(entry)
                write_file(users)
            else:
                print('That is not an option')
                continue

        elif options == '3':
            choice = input('\nWhat do you want to see?\n1. Data visualization\n2. Time period\n\nChoice: ')
            if choice == '1':
                graph_menu()
            elif choice == '2':
                time_period = input('')
                #Working
            else:
                print('That is not an option. Try again...')

        elif options == '4':
            break
        else:
            print('That is not an option. Try again...')
