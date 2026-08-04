# Compare Before and After

## Before (broken code)

```python
#This is calculator program

user_choice = "Yes"
number1 = 0
number2 = 0
Calculation = ("+", "-", "*", "/")
Calculation_Choice = None
Results = 0

def Main(number1,number2,Calcuration_Choice):
    while user_choice == "Yes":
        try:
            number1 = int(input("number1: "))
            Calculation_Choice = input("Calculation: ")
            number2 = int(input("number2: "))

            if Calculation_Choice in Calculation == "+":
                  Results = number1+number2
            elif Calculation_Choice in Calculation == "-":
                  Results , Results = number1-number2
            elif Calculation_Choice in Calculation == "*":
                  Results , Results = number1*number2
            elif Calculation_Choice in Calculation == "/":
                  print(Results , Results = number1/number2)
                  if number2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = number1 / number2

            user_choice = input("Would you like to calculate again? (yes/exit) :")

Results = Main(number1,number2,Calculation_Choice)
```

### What is wrong

- `if Calculation_Choice in Calculation == "+":` is not a valid comparison.
- `Results , Results = number1-number2` is invalid syntax and wrong assignment.
- `print(Results , Results = number1/number2)` is invalid; you cannot assign inside `print()`.
- The division by zero check runs after the calculation instead of before.
- The function uses global `user_choice` but never updates it reliably inside the loop.
- The function is called with parameters but the loop ignores them, making the call unnecessary.

## After (corrected code)

```python
# This is calculator program

Calculation = ("+", "-", "*", "/")


def Main():
    while True:
        try:
            number1 = float(input("number1: "))
            Calculation_Choice = input("Calculation (+, -, *, /): ")
            number2 = float(input("number2: "))

            if Calculation_Choice == "+":
                result = number1 + number2
            elif Calculation_Choice == "-":
                result = number1 - number2
            elif Calculation_Choice == "*":
                result = number1 * number2
            elif Calculation_Choice == "/":
                if number2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = number1 / number2
            else:
                print("Please enter a valid operation: +, -, *, or /.")
                continue

            print("Result:", result)
        except ValueError:
            print("Please enter a valid number!")
            continue

        user_choice = input("Would you like to calculate again? (yes/exit)")
        if user_choice.lower() != "yes":
            break


if __name__ == "__main__":
    Main()
```

### Main improvements

- Strong, explicit operator comparison using `==`.
- Separate variable assignment from printing.
- Use `float(input(...))` so numeric operations work correctly.
- Check division by zero before performing `/`.
- Use `if __name__ == "__main__":` to run the calculator only when the file is executed directly.
- Keep the loop and the user prompt inside the function so the behavior is predictable.
