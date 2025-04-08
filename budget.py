# Alishya Xavier, Budgeting

#This imports functions from the file_handler file
from file_handler import read_file, find_active

#The budget function that manages and displays details about their spending
def budget(): 

    #Variables that stores their spent amounts for each catagory
    spent_housing = 0
    spent_food = 0
    spent_utilities = 0
    spent_transportation = 0
    spent_insurance = 0
    spent_other = 0

    print("\nCreating a budget compares how much you spent on an expense category to a limit that you set for each category.")

    try:
        #Gathers the users input for spending limits in the categories
        housing = float(input('\nHow much do you want your limit to be on housing:\n').strip())
        food = float(input('\nHow much do you want your limit to be on food:\n').strip())
        utilities = float(input('\nHow much do you want your limit to be on utilities:\n').strip())
        transportation = float(input('\nHow much do you want your limit to be on transportation:\n').strip())
        insurance = float(input('\nHow much do you want your limit to be on insurance:\n').strip())
        other = float(input('\nHow much do you want your limit to be on other expenses:\n').strip())

    #Error Handling
    except:
        print("\nInvalid Input Type (Input in an Integer)")
        return

    #Reads the users data and finds who is the active user    
    users = read_file()
    user_ind = find_active(users)

    #Iterates over the active user's expenses to calculate the total spending in each category
    for expense in users[user_ind]['Expense']:
        if expense[2] == 'housing':
            spent_housing += float(expense[1]) 
        elif expense[2] == 'food':
            spent_food += float(expense[1])
        elif expense[2] == 'utilities':
            spent_utilities += float(expense[1])
        elif expense[2] == 'transportation':
            spent_transportation += float(expense[1])
        elif expense[2] == 'insurance':
            spent_insurance += float(expense[1])
        elif expense[2] == 'other':
            spent_other += float(expense[1])

    categories = [[spent_housing, housing, "housing"], [spent_food, food, "food"], [spent_utilities, utilities, "utilities",], [spent_transportation, transportation, "transportation",], [spent_insurance, insurance, "insurance",], [spent_other, other, "other expenses"]]

    #This is a helper function that displays the details of each category
    def display(spent, limit, name):
        dif = spent - limit
        if limit == 0:
            if spent > 0:
                percent = ">100"
            elif spent == 0:
                percent = "100"
            elif spent < 0:
                percent = "<100"
        else:
            percent = round(spent/limit * 100, 2)
        print(f'\n{name.title()}: Spent- ${spent}   Limit- ${limit}   How much over Limit- ${dif}   Percentage of Limit Met- {percent}%')
        if dif > 0:
            print(f"You went over your {name} limit.")
        else:
            print(f'You stayed within your {name} limit')

    #Iterates over categories to display spending details
    for each in categories:
        display(each[0],each[1],each[2])

