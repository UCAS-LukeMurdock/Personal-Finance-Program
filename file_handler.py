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
                    # detail = detail[1:-1]
                    # outer = detail.split("],")
                    # for ind, inner in enumerate(outer):
                    #     inner = f"{inner}]"
                    #     outer[ind] = (eval(inner))
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

def find_active(users): # 
    for ind, user in enumerate(users):
        if user["Active"] == True:
            return ind

# DELETE????
def intput(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response

print(read_file())
