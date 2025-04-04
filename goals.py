# Luke Murdock, Savings Goals
from file_handler import read_file, write_file, find_active

def create(): # Lets the user create a new goal with a name and a goal amount
    profiles = read_file()
    user_ind = find_active(profiles)
    name = input("What thing are you saving for?:\n").strip()
    try:
        goal = round(float(input("How much money do you need to save for your Savings Goal? (Type a Number):\n").strip()),2)
    except:
        print("Invalid Input Type (Input a Number)\nGoal was not Created")
        return
    if goal <= 0:
        print("Your Goal is too Low\nGoal was not Created")
        return
    
    print(f"Created Goal!\n{name}: $0/${goal}  0% Completion\nComplete this Goal to Remove it")
    profiles[user_ind]["Goals"].append([name,goal,0])
    write_file(profiles)

def add(): # Lets the user add or withdraw money from one of their goals that they choose
    profiles = read_file()
    user_ind = find_active(profiles)
    goal_ind = -1
    while True:
        choice = input("Which Goal did you want to change its progress for? [Type '0' to Exit]:\n").strip()
        if choice == "0":
            break
        for ind, goal in enumerate(profiles[user_ind]["Goals"]):
            if choice.upper() == goal[0].upper():
                goal_ind = ind
        if goal_ind == -1:
            print("That Goal couldn't be found")
            continue

        try:
            amount = float(input("How much Money do you want to Add to it? [Use '-' for Withdrawing from the Goal]:\n").strip())
        except:
            print("Invalid Input Type (Input a Number)")
            continue
        amount = round(amount,2)
        profiles[user_ind]["Goals"][goal_ind][2] = float(profiles[user_ind]["Goals"][goal_ind][2]) + amount

        # If the user reached their goal then it tells them and then deletes it
        if profiles[user_ind]["Goals"][goal_ind][2] >= profiles[user_ind]["Goals"][goal_ind][1]:
            print(f"\nYou Accomplished this Goal!\n{profiles[user_ind]["Goals"][goal_ind][0]}: ${profiles[user_ind]["Goals"][goal_ind][2]}/${profiles[user_ind]["Goals"][goal_ind][1]}  {round(float(profiles[user_ind]["Goals"][goal_ind][2])/float(profiles[user_ind]["Goals"][goal_ind][1])*100,2)}% Completion")
            profiles[user_ind]["Goals"].pop(goal_ind)
            print("This Goal was Removed")
        write_file(profiles)
        break

def view(): # Lets the user see either a specific goal or all of their goals
    profiles = read_file()
    user_ind = find_active(profiles)
    found = False

    choice = input("Type Desired Goal or type 'All' to view all goals:\n").strip()
    for goal_ind, goal in enumerate(profiles[user_ind]["Goals"]):
        if choice.upper() == goal[0].upper() and choice != '0':
            print(f"\n{profiles[user_ind]["Goals"][goal_ind][0]}: ${profiles[user_ind]["Goals"][goal_ind][2]}/${profiles[user_ind]["Goals"][goal_ind][1]}  {round(float(profiles[user_ind]["Goals"][goal_ind][2])/float(profiles[user_ind]["Goals"][goal_ind][1])*100,2)}% Completion")
            found = True
            break
        elif choice.lower() == "all":
            found = True
            print(f"\n{profiles[user_ind]["Goals"][goal_ind][0]}: ${profiles[user_ind]["Goals"][goal_ind][2]}/${profiles[user_ind]["Goals"][goal_ind][1]}  {round(float(profiles[user_ind]["Goals"][goal_ind][2])/float(profiles[user_ind]["Goals"][goal_ind][1])*100,2)}% Completion")
    if found == False or profiles[user_ind]["Goals"] == []:
        print("No Goals Found")

def goal_menu(): # Lets the user choose what to do with their goals
    while True:
        choice = input("\nSavings Goals\nCreate Goal(1) Change Goal Progress(2) View Goals(3) Exit(4)\n\nChoice: ").strip()
        if choice == "1":
            create()
        elif choice == "2":
            add()
        elif choice == "3":
            view()
        elif choice == "4":
            break
        else:
            print('That is not an option. Try again... (Please type the corresponding number)')