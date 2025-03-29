# Alec George, Visuals

#file for displaying graphs and visualizing data

#for easier access to data, use pandas
import pandas as pd

#all about graphs, needs matplotlib
import matplotlib.pyplot as plt


#function to take the user info (dictionaries of dictionaries), and make it into dictionaries of lists
def dict_to_list(data):

    #dictionary for account data
    accounts = {
        'name': [],
        'income': [],
        'expense': [],
        'goals': []
    }


    #add name
    for data_index in data['Name'].values():
        accounts['name'].append(data_index)

    #add income
    for index, data_index in enumerate(data['Income'].values()):
        accounts['income'].append(eval(data_index))
            
        for sub_index in eval(data_index):
            accounts['income'][index].append(sub_index)

    #add expense
    for data_index in data['Expense'].values():
        accounts['expense']

    
    #add goals
    for data_index in data['Goals'].values():
        accounts['goals'].append(eval(data_index))

    return accounts



#main function to choose what to do
def main():
    #variable to save money data
    df = pd.read_csv('users.csv').to_dict()
    account_data = dict_to_list(df)
    for i in range(len(account_data['name'])):
        print(account_data['name'][i])
        print(account_data['income'][i])
        print(account_data['expense'][i])
        print(account_data['goals'][i])
        print('\n\n')


    plt.pie([1,2,3,4,5], labels=account_data['name'])
    plt.show()
main()