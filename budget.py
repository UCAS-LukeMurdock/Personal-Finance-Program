# Alishya Xavier, Budgeting
from file_handler import read_file, find_active
'''
        Compares the expenses to the limit inside the file
        DISPLAY comparision
'''

def budget():
    spent_housing = 0
    spent_food = 0
    spent_utilities = 0
    spent_transportation = 0
    spent_insurance = 0
    spent_other = 0

    housing = input('\nHow much do you want to spend on housing: \n')
    food = input('\nHow much do you want to spend on food: \n')
    utilities = input('\nHow much do you want to spend on utilities: \n')
    transportation = input('\nHow much do you want to spend on transportation: \n')
    insurance = input('\nHow much do you want to spend on insurance: \n')
    other = input('\nHow much do you want to spend on other things: \n')


    users = read_file
    user_ind = find_active(users)
    for expense in users[user_ind]['Expense']:
        if expense[2] == 'housing':
            spent_housing += expense[1]
        elif expense[2] == 'food':
            spent_food += expense[1]
        elif expense[2] == 'utilities':
            spent_utilities += expense[1]
        elif expense[2] == 'transportation':
            spent_transportation += expense[1]
        elif expense[2] == 'insurance':
            spent_insurance += expense[1]
        elif expense[2] == 'other':
            spent_other += expense[1]
    
    def display(spent, limit, name):
        round(spent/limit * 100, 2)
        print(f'This is how much you spent in {name}: ${spent}. You should have spent: ${limit}\n')

categories = [spent_housing, housing, spent_food, food, spent_utilities, utilities, spent_transportation, transportation, spent_insurance, insurance, spent_other, other]
       #Working on it

for each in categories:
    display()
    