# Alec George, Visuals

#file for displaying graphs and visualizing data

#for easier access to data, use pandas
import pandas as pd

#all about graphs, needs matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

#function to find the largest value in a list
def largest_value(lst):
    value = 0
    for i in lst:
        if i >= value:
            value = i

    return value


#function to find the smallest value in a list
def smallest_value(lst):
    value = largest_value(lst)
    for i in lst:
        if i <= value:
            value = i

    return value


#function to test if something is an integer
def is_int(value):
    try:
        int(value)
    except:
        value = is_int('\nthat is not an option. Try again.\nYour answer here:\n')
    return int(value)


#function to add all y values with the same x value
def add_values(x, y):
    #variables
    new_x = []
    new_y = []
    next_x = 100
    next_y = 0

    #loop through all numbers and make a list
    while next_x <= largest_value(x):
        if next_x in x:
            new_x.append(next_x)
            next_y = 0
            for index, value in enumerate(x):
                if value == next_x:
                    next_y += y[index]

            new_y.append(next_y)
            

        next_x += 1

    return new_x, new_y





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
                account['i_amt'].append(int(income[1]))
                account['i_name'].append(income[2])
            
            #change dates to more readable things for computer, make dates a single number
            for i in range(len(account['i_date'])):
                #subtract 2025 from year to make it simpler
                account['i_date'][i] = (int(account['i_date'][i][0])-2025)*365 + int(account['i_date'][i][1])*30 + int(account['i_date'][i][2])


            #add expense
            #variable to convert the list string into a list
            information = data['Expense'][index]
            information = eval(information)
            for expense in information:
                account['e_date'].append(expense[0].split('-'))
                account['e_amt'].append(int(expense[1]))
                account['e_name'].append(expense[2])

            #change dates to more readable things for computer, make dates a single number
            for i in range(len(account['e_date'])):
                #subtract 2025 from year to make it simpler
                account['e_date'][i] = (int(account['e_date'][i][0])-2025)*365 + int(account['e_date'][i][1])*30 + int(account['e_date'][i][2])

    return account



#main function to choose what to do
def graph_menu():
    #variable to save money data
    df = pd.read_csv('users.csv').to_dict()
    account_data = dict_to_list(df)


    #loop continuously
    while True:
        #ask user if they want to see a pie chart or a line graph
        user_input = input('''\nWhat would you like to see? Type:
1 to see a pie chart of your income
2 to see a pie chart of your expenses
3 to see a line graph of both over time
4 to exit
Your answer here:
''').strip()
        user_input = is_int(user_input)
        
        if user_input == 1:
            #make sure there is data in it
            if len(account_data['i_amt']) > 0:
                plt.pie(account_data['i_amt'],labels=account_data['i_name'])
            else:
                print('\nnot enough data\n')
                continue

        
        elif user_input == 2:
            #make sure there is data in it
            if len(account_data['e_amt']) > 0:
                plt.pie(account_data['e_amt'],labels=account_data['e_name'])
            else:
                print('\nnot enough data\n')
                continue

        elif user_input == 3:
            #variables for income points
            i_x_points, i_y_points = add_values(account_data['i_date'], account_data['i_amt'])
            
            #variables for expense points
            e_x_points, e_y_points = add_values(account_data['e_date'], account_data['e_amt'])

            #make sure there is data in it
            if len(account_data['e_amt']) > 1 or len(account_data['i_amt']) > 1:
                

                #assign graph bounds and margins (bit of space between the graph and edges)
                bounds = [smallest_value([smallest_value(i_x_points),smallest_value(e_x_points)]), largest_value([largest_value(i_x_points),largest_value(e_x_points)]), smallest_value([smallest_value(i_y_points),smallest_value(e_y_points)]), largest_value([largest_value(i_y_points),largest_value(e_y_points)])]
                margins = [(bounds[1]-bounds[0])//20,(bounds[3]-bounds[2])//20]

                

                fig, ax = plt.subplots()
                #plot lines
                ax.plot(i_x_points, i_y_points)
                ax.plot(e_x_points, e_y_points)

                #give axes names
                plt.xlabel('Time')
                plt.ylabel('Income')

                #set graph size
                ax.set(xlim=(bounds[0], bounds[1]+margins[0]), ylim=(bounds[2]-margins[1], bounds[3]+margins[1]), xticks=np.arange(bounds[0], bounds[1]), yticks=np.arange(bounds[2], bounds[3]))

                #give information
                print("\nBlue is income\nOrange is expense\nThis graph plots the lines over a period of multiple days (If you only have entries from one day then it can't make lines over time)")
            else:
                print('\nnot enough data\n')
                continue
                
        elif user_input == 4:
            break

        #show graph
        print("\nto continue, exit the graph\n")
        plt.show()