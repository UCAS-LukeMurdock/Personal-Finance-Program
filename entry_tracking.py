# Alishya Xavier, Income and Expenses Entry File

#This imports the necessary libraries and gets the functions from different files
import datetime as dt
from visual import graph_menu
from file_handler import read_file, find_active, write_file

#Function that handles income and expense entries tracking
def entry_tracking():
    #Reads the user's data from the file
    users = read_file()
    #Finds the active user
    user_ind = find_active(users)
    while True:
        options = input('\nWhat would you like to do?\n1. add an income entry\n2. add an expense entry\n3. view income and expenses\n4. Exit\n\nyour choice here: ')
        
        if options == '1':
            #Adding an income entry
            try:
                income = round(float(input('\nhow much income do you want your entry to have (Type "0" to Exit):\n')), 2)
            except:
                print("\nThat is not an option. Try again... (Type a Number)")
                continue
            if income == 0:
                continue
            elif income < 0:
                print("\nThat is not an option. Try again... (Type a Number greater than 0)")
                continue
            source = input('\nWhat is the source of your income: ')
            date = dt.datetime.now().strftime("%Y-%m-%d") #Gets current date
            entry = [date, income, source]#Makes an income entry list
            users[user_ind]['Income'].append(entry)#Adds entry to the users data
            write_file(users)#Updates data to file
            print('\nIncome entry added successfully!')
        
        elif options == '2':
            #Adding an expense entry
            try:
                expense = round(float(input('\nWhat is your entry\'s expense (Type "0" to Exit):\n')), 2)
            except:
                print("\nThat is not an option. Try again... (Type a Number)")
                continue
            if expense == 0:
                continue
            elif expense < 0:
                print("\nThat is not an option. Try again... (Type a Number greater than 0)")
                continue
            category = input('What is the category of your expense (housing, food, utilities, transportation, insurance, or other):\n')
            if category in ['housing','food','utilities','transportation','insurance','other']:
                date = dt.datetime.now().strftime("%Y-%m-%d")
                entry = [date, expense, category]
                users[user_ind]['Expense'].append(entry)
                write_file(users)
                print('\nExpense entry added successfully!')
            else:
                print('\nThat is not an option. Please try again. (Type one of the allowed categories)')
                continue

        elif options == '3':
            #Viewing the total income and expenses
            choice = input('\nWhat do you want to see?\n1. Graphs/charts of income or expense\n2. income/expense in a time period\n3. display all entries\n\nyour choice here: ')
            
            if choice == '1':
                #Calling the data visualization function
                graph_menu()

            elif choice == '2':
                #Views income and expenses for specific time period
                start_time_period = input('\nWhat is your start day(YYYY-MM-DD): ')
                end_time_period = input('\nWhat is your end day(YYYY-MM-DD): ')
                try:
                    #Shows total income and expenses if date format is properly inputted
                    start_date = dt.datetime.strptime(start_time_period, "%Y-%m-%d")
                    end_date = dt.datetime.strptime(end_time_period, "%Y-%m-%d")
                    total_income, total_expenses = calculate_totals(users[user_ind], start_date, end_date)
                    print(f"\nTotal Income: ${total_income:,.2f}")
                    print(f"Total Expenses: ${total_expenses:,.2f}")
                    change = total_income - total_expenses
                    print(f'\nNet total: ${change:,.2f}')
                except ValueError:
                    print("\nInvalid date format! Please use YYYY-MM-DD.")

            elif choice == '3':
                def display_all(entry_type): # Displays all entries for either type of entry
                    nonlocal users, user_ind
                    print(f"\n{entry_type}{'' if entry_type == 'Income' else 's'}:")
                    for entry in users[user_ind][entry_type]:
                        print(f"\nDate- {entry[0]}\n{'Source' if entry_type == 'Income' else 'Category'}- {entry[2]}\nAmount- ${entry[1]}")
                    input("\nPress Enter to continue\n")
                
                display_all("Income")
                display_all("Expense")
                
            else:
                print('\nThat is not an option. Try again...')

        elif options == '4':
            print('\nExiting the tracker!')
            break
        else:
            print('\nThat is not an option. Try again...')


# Function to calculate total income and expenses with time period
def calculate_totals(user_data, start_date, end_date):
    total_income = 0
    total_expense = 0

    #Calculates total income
    for entry in user_data['Income']:
        entry_date = dt.datetime.strptime(entry[0], "%Y-%m-%d")
        if start_date <= entry_date <= end_date:
            total_income += float(entry[1])
    
    # Calculates total expenses
    for entry in user_data['Expense']:
        entry_date = dt.datetime.strptime(entry[0], "%Y-%m-%d")
        if start_date <= entry_date <= end_date:
            total_expense += float(entry[1])

    return total_income, total_expense

