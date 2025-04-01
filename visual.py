# Alec George, Visuals

#file for displaying graphs and visualizing data

#for easier access to data, use pandas
import pandas as pd

#all about graphs, needs matplotlib
import matplotlib.pyplot as plt


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
        print(value)
        if value == True: #use the signed in profile
            print(data['Name'][index])
            account['name'] = data['Name'][index]

            #add income
            #variable to convert the list string into a list
            information = data['Income'][index]
            information = eval(information)
            for income in information:
                account['i_date'].append(income[0])
                account['i_amt'].append(income[1])
                account['i_name'].append(income[2])


            #add expense
            #variable to convert the list string into a list
            information = data['Expense'][index]
            information = eval(information)
            for income in information:
                print(income)
                account['e_date'].append(income[0])
                account['e_amt'].append(income[1])
                account['e_name'].append(income[2])


            

    
    return account



#main function to choose what to do
def graph_menu():
    #variable to save money data
    df = pd.read_csv('users.csv').to_dict()
    account_data = dict_to_list(df)
    print(account_data)

    plt.pie([1,2,3,4,5])
    plt.show()

graph_menu()