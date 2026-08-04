# Fix for Simple_Calculator `main.py`

## Original mistakes

1. `if Calculation_Choice in Calculation == "+":`
   - This condition is invalid.
   - You wanted to compare `Calculation_Choice` with `+`, but `in` and `==` together do not work that way.

2. `print(Results , Results = number1+number2)`
   - Assigning inside a `print()` call is not valid Python.
   - You also never converted the user input from `input()` into a number.

3. `number1 = input("number1: ")` and `number2 = input("number2: ")`
   - `input()` returns a string.
   - You need `int()` or `float()` before doing arithmetic.

4. `while user_choice == "Yes":` with `user_choice` defined outside the function
   - The loop used a global variable but the variable was never updated inside the loop.
   - This can cause logic problems and make the function harder to reuse.

5. Division by zero handling was after the calculation
   - If `number2` was zero, the code would still try to divide before printing the error.

## Fixed code

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

        user_choice = input("Would you like to calculate again? (yes/exit): ")
        if user_choice.lower() != "yes":
            break


if __name__ == "__main__":
    Main()
```

## Summary

- Use `float(input(...))` to read numbers.
- Compare the operator with `==`, not `in ... ==`.
- Do assignments separately from `print()`.
- Handle invalid operations and division by zero before calculating.
- Put the function call inside `if __name__ == "__main__":`.



#i actually forgot about Local variable and Global Variable