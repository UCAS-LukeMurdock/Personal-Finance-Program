#Luke Murdock, Calculator

def calc():
    operation = ""
    error = False
    while True:
        try:
            num1 = float(input("First number?:"))
        except:
            error = True
            print("Not an Integer")
            break

        operation = input("What operation? (+, -, *, /, ** [exponents], // [divison without remainder], % [division's remainder]):")

        try:
            num2 = float(input("Second number?:"))
        except:
            error = True
            print("Not an Integer")
            break
            
        if (operation == "+") :
            answer = num1 + num2
        elif (operation == "-") :
            answer = num1 - num2
        elif (operation == "*") :
            answer = num1 * num2
        
        elif (operation == "/") :
            if num2 == 0:
                error = True
                print("Divide by 0 Error")
                break
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
        break

    if error == False:
        print(num1, operation, num2, "=", answer)