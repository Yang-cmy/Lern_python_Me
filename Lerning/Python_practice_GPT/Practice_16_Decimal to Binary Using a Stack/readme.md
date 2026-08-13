# Python Practice #16 — Decimal to Binary Using a Stack

Let's continue with Stack, but now use it to solve a small algorithm problem.

## Task

Write a function:

`decimal_to_binary(number)`

that converts a positive decimal integer into binary using a list as a stack.

For example:

`print(decimal_to_binary(13))`

Expected output:

`1101`

How it works

To convert 13 to binary, repeatedly divide by 2 and store the remainder:

```python
13 % 2 = 1
 6 % 2 = 0
 3 % 2 = 1
 1 % 2 = 1
```

If you push those remainders onto a stack, you'll get:

```text
[1, 0, 1, 1]
          ↑
         TOP
```

But reading them in the order they were added gives the wrong direction.

Use the LIFO behavior of a stack:

```text
pop → 1
pop → 1
pop → 0
pop → 1
```
Result:

`1101`

## Requirements

Your function must:

- Create an empty list called `stack`.
- Use a `while` loop.
- Calculate the remainder using `% 2`.
- Push remainders using `append()`.
- Remove them using `pop()`.
- Return the binary result as a **string**.

For this exercise, assume `number > 0`.

Do not use Python's shortcuts:

```python
bin(number)
format(number, "b")
```

```python
Test Cases
print(decimal_to_binary(13))
print(decimal_to_binary(10))
print(decimal_to_binary(8))
```

Expected:

```text
1101
1010
1000
```

## VS Code Debugging Challenge

Set a breakpoint inside your first `while` loop and test:

`decimal_to_binary(10)`

Watch:

```text
number
remainder
stack
```
You should eventually see something like:

```text
number = 10   remainder = 0   stack = [0]
number = 5    remainder = 1   stack = [0, 1]
number = 2    remainder = 0   stack = [0, 1, 0]
number = 1    remainder = 1   stack = [0, 1, 0, 1]
```
Then watch what happens when you start pop()-ing the values.