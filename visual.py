# Alec George, Visuals

#file for displaying graphs and visualizing data

#for easier access to data, use pandas
import pandas as pd

#all about graphs, needs matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np


#function to test if something is an integer
def is_int(value):
    try:
        int(value)
    except:
        value = is_int('\nthat is not an option. Try again.\nYour answer here:\n')
    return int(value)


#function to add all y values with the same x value
def add_values(x, y):
    x = x.sort()
    #variables
    new_x = []
    new_y = []
    next_x = 0
    next_y = 0




#function to take the user info (dictionaries of dictionaries), and make it into dictionaries of lists
def dict_to_list(data):

    #dictionary for account data
    account = {
        'name': '',
        'i_date': [],
        'i_amt': [],
        'i_name': [],
        'e_date': [],
        'e_amt': [],
        'e_name': [],
    }

    for index, value in enumerate(data['Active'].values()):
        if value == True: #use the signed in profile
            account['name'] = data['Name'][index]

            #add income
            #variable to convert the list string into a list
            information = data['Income'][index]
            information = eval(information)
            for income in information:
                account['i_date'].append(income[0].split('-'))
                account['i_amt'].append(income[1])
                account['i_name'].append(income[2])
            
            #change dates to more readable things for computer, make dates a single number
            for i in range(len(account['i_date'])):
                #subtract 2025 from year to make it simpler
                account['i_date'][i] = (int(account['i_date'][i][0])-2025)*365 + int(account['i_date'][i][1])*30 + int(account['i_date'][i][2])


            #add expense
            #variable to convert the list string into a list
            information = data['Expense'][index]
            information = eval(information)
            for income in information:
                account['e_date'].append(income[0])
                account['e_amt'].append(income[1])
                account['e_name'].append(income[2])

            #change dates to more readable things for computer, make dates a single number
            for i in range(len(account['e_date'])):
                #subtract 2025 from year to make it simpler
                account['e_date'][i] = (int(account['e_date'][i][0])-2025)*365 + int(account['e_date'][i][1])*30 + int(account['e_date'][i][2])

    return account



#main function to choose what to do
def graph_menu():
    print([1,2,3,52,3,4])
    #variable to save money data
    df = pd.read_csv('users.csv').to_dict()
    account_data = dict_to_list(df)

    #ask user if they want to see a pie chart or a line graph
    user_input = input('''\nWhat would you like to see? Type:
1 to see a pie chart of your income
2 to see a pie chart of your expenses
3 to see a line graph of both over time
Your answer here:
''')
    user_input = is_int(user_input)
    
    if user_input == 1:
        #make sure there is data in it
        if len(account_data['i_amt']) > 0:
            plt.pie(account_data['i_amt'],labels=account_data['i_name'])
        else:
            print('\nnot enough data\n')

    
    elif user_input == 2:
        #make sure there is data in it
        if len(account_data['e_amt']) > 0:
            plt.pie(account_data['e_amt'],labels=account_data['e_name'])
        else:
            print('\nnot enough data\n')

    elif user_input == 3:
            #make sure there is data in it
            if len(account_data['e_amt']) > 0 or len(account_data['i_amt']) > 0:
                #variables for points
                x_points = []
                y_points = []

                fig, ax = plt.subplots()
                ax.plot(account_data['i_date'], account_data['i_amt'])
                ax.plot(account_data['e_amt'])
                ax.set(xticks=[1,2,3,4,5,6], yticks=np.arange(0,30))
            else:
                print('\nnot enough data\n')


    #show graph
    plt.show()

