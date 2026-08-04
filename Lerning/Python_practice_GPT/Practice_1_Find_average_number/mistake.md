# Your idea is good: use a function, loop five times, store the data, and calculate the average. However, there is an important problem with the try-except.

## Suppose the first input is invalid:

i = 0
Data = []

Nothing is appended. On the next loop, i becomes 1. If the user enters a valid number:

Data.append(User_Choice)   # The number is stored at Data[0]
average += Data[i]         # Tries to access Data[1]

This causes an IndexError.

Also, dividing by number is incorrect if some inputs are invalid because fewer than number values may have been accepted.

---

## Simple corrected version

``` python
def find_average(number):
    data = []
    total = 0

    for i in range(number):
        while True:
            try:
                user_choice = int(input(f"Enter data {i + 1}: "))
                data.append(user_choice)
                total += user_choice
                break

            except ValueError:
                print("Please enter a valid number!")

    average = total / number
    print("Data:", data)
    print("Average:", average)


find_average(5)
```
---

## Why while True is useful

If the user enters something invalid, such as:

Enter data 1: hello
Please enter a valid number!
enter data 1:

The program asks for data 1 again. It does not continue to data 2 until a valid number is entered.

You also do not need this:

average += Data[i]

---

## You can directly use:

total += user_choice

That is simpler and avoids indexing errors.

One naming improvement: Python normally uses lowercase variable names:

1.data
2.user_choice
3.total

Uppercase names such as Data are usually reserved for class names.

Practical rule: When invalid input should not count, keep asking inside a while loop until the user provides valid input.

````markdown
# Hello
````