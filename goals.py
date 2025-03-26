# Luke Murdock, Savings Goals
from file_handler import read_file, write_file, find_active, intput
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

def create(): # 
    profiles = read_file()
    user_ind = find_active(profiles)
    goal = input("What is your Savings Goal?: \n")
    profiles[user_ind]["Goals"].append((goal,0))
    write_file(profiles)

def add(): # 
    profiles = read_file()
    user_ind = find_active(profiles)
    while True:
        choice_goal = input("Which Goal amount did you want to add to? [Exit(0)]:\n")
        if choice_goal == "0":
        for ind, goal in enumerate(profiles[user_ind]["Goals"]):
            if choice_goal == goal[0]:
                goal_ind = ind
            else:
                print("That Goal couldn't be found")
                break
        amount = input("How much money do you want to add to it?:\n")
        if 
    # checking allowed and stuff

def view(): # 
    choice = input("Type Desired Goal [All(0)]: ")
    if choice == "0":
        pass
    elif choice != "0":
        pass
    # Finish

def goal_menu(): # 
    while True:
        choice = input("\nSavings Goals\nCreate Goal(1) Add to Goal Progress(2) View Goals(3) Exit(4)\n")
        if choice == 1:
            create()
        elif choice == 2:
            add()
        elif choice == 3:
            view()
        elif choice == 4:
            break
        else:
            print('That is not an option. Try again...')

# Remeber to make sure file things are int() or str()