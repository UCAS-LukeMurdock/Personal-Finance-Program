#Luke Murdock, Calculator

def calc(): # Calculates and Displays two inputted numbers using an inputted operation
    operation = ""
    print("\nThis is a Calculator that lets you choose two numbers and the operation that is used on them.")
    while True:
        num1 = input('\nWhat is the first number? (Type "Exit" to Exit): ').lower()
        if num1 == "exit":
            break
        try:
            num1 = float(num1)
        except:
            print("\nNot a Number")
            continue

        operation = input("\nWhat operation are you doing? (+, -, *, /, ** [exponents], // [divison without remainder], % [division's remainder]): ")

        try:
            num2 = float(input("\nWhat is the second number?: "))
        except:
            print("\nNot a Number")
            continue
        
        # Calculates
        if (operation == "+") :
            answer = num1 + num2
        elif (operation == "-") :
            answer = num1 - num2
        elif (operation == "*") :
            answer = num1 * num2
        
        elif (operation == "/") :
            if num2 == 0:
                print("\nDivide by 0 Error")
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