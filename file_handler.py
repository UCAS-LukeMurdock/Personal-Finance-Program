# Luke Murdock, File Handler- Read & Write to Files, Integer Input Handler, and other Handlers
import csv

def read_file(): # Turns a file into a list of dictionaries
    dicts = []
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            dict = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 2 or detail_index == 3 or detail_index == 4 or detail_index == 5:
                    detail = eval(detail)
                dict.update({detail_types[detail_index]:detail})
            dicts.append(dict)
    return dicts

def write_file(dicts): # Writes the list of dictonary onto the file
    with open ("users.csv", "w", newline="") as file:
        fieldnames = ["Name","Password","Income","Expense","Goals","Active"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dicts)

def find_active(users): # Finds active user index
    for ind, user in enumerate(users):
        if user["Active"] == True:
            return ind
