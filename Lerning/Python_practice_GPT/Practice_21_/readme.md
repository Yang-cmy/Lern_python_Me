## Python Practice #21 — Two Stacks: Undo and Redo

Now let's move beyond a single stack. You'll build a simple **Undo/Redo system using two stacks**.

### Scenario

Imagine a text editor where the user performs actions:

```text
Type A
Type B
Delete B
```

You'll maintain:

```python
undo_stack = []
redo_stack = []
```

### Task

Create a class:

```python
class Editor:
```

It should contain:

```python
self.undo_stack = []
self.redo_stack = []
```

Implement these methods:

```python
do_action(action)
undo()
redo()
show_history()
```

### Rules

**`do_action(action)`**

Push the new action onto:

```python
self.undo_stack
```

Whenever a **new action** happens, clear the redo stack:

```python
self.redo_stack.clear()
```

**`undo()`**

Remove the most recent action from `undo_stack` and push it onto `redo_stack`.

For example:

```text
undo_stack = ["Type A", "Type B", "Delete B"]
redo_stack = []
```

After one `undo()`:

```text
undo_stack = ["Type A", "Type B"]

redo_stack = ["Delete B"]
```

**`redo()`**

Do the opposite: remove the top action from `redo_stack` and put it back onto `undo_stack`.

**`show_history()`**

Use a loop to print the actions currently in `undo_stack`.

### Test Your Program

```python
editor = Editor()

editor.do_action("Type A")
editor.do_action("Type B")
editor.do_action("Delete B")

editor.undo()
editor.undo()

editor.redo()

editor.show_history()
```

Expected history:

```text
Type A
Type B
```

At that point, your stacks should effectively contain:

```text
undo_stack
["Type A", "Type B"]
                 ↑ TOP

redo_stack
["Delete B"]
        ↑ TOP
```

### Requirements

Use **one class, two lists as stacks, `append()`, `pop()`, a loop, and empty-stack checks**. `undo()` and `redo()` must not crash when their corresponding stack is empty.

Don't create new lists inside `undo()` or `redo()` to replace the existing stacks.

### VS Code Debugging Challenge

Put breakpoints inside both `undo()` and `redo()`.

Watch:

```python
self.undo_stack
self.redo_stack
```

Then execute:

```text
do A
do B
do C

undo
undo
redo
```

Before running it, try to predict the contents of **both stacks after every operation**.

### Your Turn

Send me **only your Python code**. I'll review your attempt, explain any mistakes clearly, and finish with **one practical rule to remember**.
