# Python Practice #15 — Reverse a Word Using a Stack

We're continuing with your Stack coursework, but this time the exercise is shorter and focuses on understanding LIFO clearly.

## Task

Write a function:

`reverse_word(word)`

The function should use a Python list as a stack to reverse a word.

For example:

`print(reverse_word("Python"))`

Expected output:

`nohtyP`

## How your program should work

For `"CAT"`, first use a loop to push every character onto the stack:
```text
[]
[C]
[C, A]
[C, A, T]
        ↑
       TOP
```
Then use another loop to repeatedly pop from the stack:
```Text
pop → T
pop → A
pop → C
```
Therefore:

`TAC`

## Requirements

Your function must:

- Create an empty list called stack.
- Use append() to push characters.
- Use pop() to remove characters.
- Use one loop to fill the stack.
- Use another loop to empty the stack.
- Return the reversed string.

Don't use:

```python
word[::-1]
reversed(word)
```
The purpose is to practice Stack operations, not Python's shortcut for reversing strings.

## Test your function

Try at least these:

```python
print(reverse_word("Python"))
print(reverse_word("Stack"))
print(reverse_word("ABC"))
```
Expected:
```text
nohtyP
kcatS
CBA
```
## VS Code Debugging Challenge

Set a breakpoint inside your second loop and run:

`reverse_word("ABC")`

Use F10 and watch `stack`.

You should see it shrink:

```python
["A", "B", "C"]
["A", "B"]
["A"]
[]
```

Pay attention to which element disappears first. That's the key idea behind LIFO