# Alec George, Visuals

#file for displaying graphs and visualizing data

#for easier access to data, use pandas
import pandas as pd

#all about graphs, needs matplotlib
import matplotlib as mpl


#main function to choose what to do
def main():
    #variable to save money data
    df = pd.read_csv('users.csv').to_dict()


    mpl.pie([1,2,3,4])
    mpl.show()
main()