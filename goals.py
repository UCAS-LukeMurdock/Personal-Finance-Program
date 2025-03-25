# Luke Murdock, Savings Goals
from file_handler import read_file, write_file, intput
"""
Procedure for goal menu
    Find if the user wants to create a goal, add to a goal's progress, view a goal, or exit to main menu
    Goes to the desired procedure below

Procedure for creating new goal
    Find what goal they want to reach
    Create the goal as a list and write to the file

Procedure for adding to goal
    Find out which goal they want to add to
    Find how much money they want to add to their progress
    Add the money to their goal and write to file

Procedure for viewing goals and Progress
    Find out which goal they want to view or if they want to view all of them
    Display their desired goal's information and progress percentage
"""

def goal_menu():
    choice = intput("Create Goal(1) Add to Goal Progress(2) View Goals(3) Exit(4)", 1,4)
