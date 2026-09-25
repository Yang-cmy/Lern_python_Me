# Python Practice #13 — Undo System with a Stack

Let's continue practicing Stack, but make it slightly more challenging.

Imagine you're building a simple text editor. Every time the user types something, the program stores it in a stack so the most recent action can be undone first.

## Your task

Create a class:

`class UndoStack:`

It should contain:

`self.actions = []`

Create three methods:

```python
add_action(action)
undo()
show_actions()
```

The behavior should be:

- `add_action(action)` → push the action onto the stack.
- `undo()` → remove and return the most recent action.
- If the stack is empty, `undo()` should return `None`.
- `show_actions()` → use a loop to print all actions currently stored.

Test your program with:

```python
history = UndoStack()

history.add_action("Type Hello")
history.add_action("Type World")
history.add_action("Delete World")

history.show_actions()

print("Undo:", history.undo())
print("Undo:", history.undo())

history.show_actions()
```

The important part is the LIFO behavior:

```text
Type Hello
Type World
Delete World
        ↑
       TOP
```

So the first `undo()` should return:

`Delete World`

and the second should return:

`Type World`

## Extra challenge

Don't use:

`self.actions[-1]`

inside undo().

Try to solve the removal and return using only Python's `pop()`.

## VS Code debugging

Put a breakpoint on the line containing `pop()`. Press F5, then use F10 and watch `self.actions`.

Pay attention to what happens to the same list object after each `pop()`.

Send me your code when you're done. Don't worry if it doesn't work perfectly—I want to see your attempt first, then I'll explain the mistakes and finish with one practical rule to remember.