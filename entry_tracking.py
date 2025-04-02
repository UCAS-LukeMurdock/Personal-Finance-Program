# Alishya Xavier, Income and Expenses Entry File
import datetime as dt
from visual import graph_menu
from file_handler import read_file, find_active, write_file

def entry_tracking():
    users = read_file()
    user_ind = find_active(users)
    while True:
        options = input('\nWhat would you like to do?\n1. Add income entry\n2. Add expense entry\n3. View total income and expenses\n4. Exit\n\nChoice: ')
        
        if options == '1':
            income = input('How much income are you adding: ')
            source = input('What is the source of your income: ')
            date = dt.datetime.now().strftime("%Y-%m-%d")
            entry = [date, income, source]
            users[user_ind]['Income'].append(entry)
            write_file(users)
            print('Income entry added successfully!')
        
        elif options == '2':
            expense = input('How much expense are you adding: ')
            category = input('What is the category of your expense(housing, food, utilities, transportation, insurance, or other): ')
            if category in ['housing','food','utilities','transportation','insurance','other']:
                date = dt.datetime.now().strftime("%Y-%m-%d")
                entry = [date, expense, category]
                users[user_ind]['Expense'].append(entry)
                write_file(users)
                print('Expense entry added successfully!')
            else:
                print('That is not an option. Please try again.')
                continue

        elif options == '3':
            choice = input('\nWhat do you want to see?\n1. Data visualization\n2. Time period\n\nChoice: ')
            
            if choice == '1':
                graph_menu()

            elif choice == '2':
                start_time_period = input('What is your start day(YYYY-MM-DD): ')
                end_time_period = input('What is your end day(YYYY-MM-DD): ')
                try:
                    start_date = dt.datetime.strptime(start_time_period, "%Y-%m-%d")
                    end_date = dt.datetime.strptime(end_time_period, "%Y-%m-%d")
                    total_income, total_expenses = calculate_totals(users[user_ind], start_date, end_date)
                    print(f"Total Income: ${total_income:.2f}")
                    print(f"Total Expenses: ${total_expenses:.2f}")
                    change = total_income - total_expenses
                    print(f'Net total: {change}')
                except ValueError:
                    print("Invalid date format! Please use YYYY-MM-DD.")
                    
            else:
                print('That is not an option. Try again...')

        elif options == '4':
            print('Exiting the tracker!')
            break
        else:
            print('That is not an option. Try again...')



def calculate_totals(user_data, start_date, end_date):
    total_income = 0
    total_expense = 0

    #Calculates income
    for entry in user_data['Income']:
        entry_date = dt.datetime.strptime(entry[0], "%Y-%m-%d")
        if start_date <= entry_date <= end_date:
            total_income += float(entry[1])
    
    # Calculates expenses
    for entry in user_data['Expense']:
        entry_date = dt.datetime.strptime(entry[0], "%Y-%m-%d")
        if start_date <= entry_date <= end_date:
            total_expenses += float(entry[1])

    return total_income, total_expenses

entry_tracking()