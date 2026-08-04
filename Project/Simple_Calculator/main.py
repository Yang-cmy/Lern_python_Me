#i will try again
#in the end 
#Not finish 100percent have error where it store results when we calculate again
Calculation = ("+", "-", "*", "/")

def Main():
    while True:
        try:
            number1 = int(input("Enter first number: "))
            Calculation = input("Enter your opreation: ")
            number2 = int(input("Enter secound number: "))

            if Calculation == "+":
                results = number1+number2
            elif Calculation == "-":
                results = number1-number2
            elif Calculation == "*":
                results = number1*number2
            elif Calculation == "/":
                if number2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = number1 / number2
            else:
                print("Please enter a valid opreation +, -, * or /")
                continue

            print("Results: ",results)
        except ValueError:
            print("Please enter a valid number!")
            continue

        user_choice = input("Would you like to calculate again? (yes/exit):")
        if user_choice.lower() != "yes":
            break 

if __name__ == "__main__":
    Main()