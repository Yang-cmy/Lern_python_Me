
# Finding the Average: Error Explanation and Correction

Your idea is good: use a function, loop five times, store the data, and calculate the average.

However, there is an important problem with the `try-except` block.

## What Happens When the First Input Is Invalid?

Suppose the first input is invalid:

```python
i = 0
Data = []
```

Because the input is invalid, nothing is appended to `Data`.

During the next loop, `i` becomes `1`. If the user then enters a valid number, the following code runs:

```python
Data.append(User_Choice)   # The number is stored at Data[0]
average += Data[i]         # Tries to access Data[1]
```

The new number is stored at `Data[0]`, but the program tries to access `Data[1]`.

This causes an `IndexError`.

Also, dividing by `number` is incorrect if some inputs are invalid because fewer than `number` values may have been accepted.

---

## Corrected Version

```python
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

## Why `while True` Is Useful

Suppose the user enters something invalid:

```text
Enter data 1: hello
Please enter a valid number!
Enter data 1:
```

The program asks for data 1 again. It does not continue to data 2 until the user enters a valid number.

You also do not need to write:

```python
average += Data[i]
```

You can directly write:

```python
total += user_choice
```

This is simpler and avoids indexing errors.

---

## Variable Naming

Python normally uses lowercase variable names:

1. `data`
2. `user_choice`
3. `total`

Names beginning with uppercase letters, such as `Data`, are normally used for classes.

---

**Practical rule:** When invalid input should not count, keep asking inside a `while` loop until the user provides valid input.

