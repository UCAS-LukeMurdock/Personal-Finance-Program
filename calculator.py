#Luke Murdock, Calculator

def calc(): # Calculates and Displays two inputted numbers using an inputted operation
    operation = ""
    error = False
    print("\nThis is a Calculator that lets you choose two numbers and the operation that is used on them.")
    while True:
        num1 = input('First number? (Type "Exit" to Exit):').lower()
        if num1 == "exit":
            break
        try:
            num1 = float(num1)
        except:
            print("Not a Number")
            continue

        operation = input("What operation? (+, -, *, /, ** [exponents], // [divison without remainder], % [division's remainder]):")

        try:
            num2 = float(input("Second number?:"))
        except:
            print("Not a Number")
            continue
            
        if (operation == "+") :
            answer = num1 + num2
        elif (operation == "-") :
            answer = num1 - num2
        elif (operation == "*") :
            answer = num1 * num2
        
        elif (operation == "/") :
            if num2 == 0:
                print("Divide by 0 Error")
                continue
            else:
                answer = num1 / num2

        elif (operation == "**") :
            answer = num1 ** num2
        elif (operation == "//") :
            answer = num1 // num2
        elif (operation == "%") :
            answer = num1 % num2
        else:
            answer = "error"

        print(num1, operation, num2, "=", answer)