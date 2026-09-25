# Practice 18 — Task Stack + Save to File

## Score: 9/10

My final code works correctly.

I used a Stack to store tasks, removed the most recent task with `pop()`, displayed the remaining tasks, and saved them into a text file.

## Mistakes I Made

### 1. I forgot to call `is_empty()`

Wrong:

```python
if self.is_empty:
```

Correct:

```python
if self.is_empty():
```

A method needs `()` when I want to run it.

---

### 2. My `is_empty()` logic was backwards

Wrong:

```python
return len(self.tasks) != 0
```

That means:

> return `True` when there ARE tasks

But `is_empty()` should mean:

> return `True` when there are NO tasks

Correct:

```python
return len(self.tasks) == 0
```

---

### 3. I used the wrong attribute name

Wrong:

```python
len(self.task)
```

But my list is:

```python
self.tasks
```

Correct:

```python
len(self.tasks)
```

Small typo, but it would cause an error.

---

### 4. I used `return` inside the loop

Wrong:

```python
for t in range(len(self.tasks)):
    return self.tasks[t]
```

`return` immediately ends the entire function, so only the first task would be returned.

Correct:

```python
for t in range(len(self.tasks)):
    print(self.tasks[t])
```

Now every task is shown.

---

### 5. I confused the object with the list inside the object

I originally tried:

```python
save_tasks(tasks, filename)
```

But:

```python
tasks
```

is a `TaskStack` object.

The actual list is:

```python
tasks.tasks
```

So I used:

```python
save_tasks(tasks.tasks, filename)
```

This is an important OOP idea:

```python
tasks          # TaskStack object
tasks.tasks    # list stored inside the object
```

---

## Final Code

```python
class TaskStack:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def finish_task(self):
        if self.is_empty():
            return None
        return self.tasks.pop()

    def show_tasks(self):
        if self.is_empty():
            return None

        for t in range(len(self.tasks)):
            print(self.tasks[t])

    def is_empty(self):
        return len(self.tasks) == 0


def save_tasks(task, filename):
    with open(filename, "w") as f:
        for i in task:
            f.write(f"{i}\n")


filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_18_\task.txt"

tasks = TaskStack()

tasks.add_task("Study Python")
tasks.add_task("Finish homework")
tasks.add_task("Read book")

print("Finished:", tasks.finish_task())

tasks.show_tasks()

save_tasks(tasks.tasks, filename)
```

## What Can Be Improved

This works:

```python
save_tasks(tasks.tasks, filename)
```

But it directly accesses the internal list of the object.

Later, a cleaner OOP design could let the class handle saving itself.

For example:

```python
def save_tasks(self, filename):
    with open(filename, "w") as f:
        for task in self.tasks:
            f.write(f"{task}\n")
```

Then I could call:

```python
tasks.save_tasks(filename)
```

That is cleaner because the object manages its own data.

For now, my current version is still correct and easier to understand.

## Practical Rule

**Always know whether I am working with the object itself or with data stored inside the object.**

```python
object.attribute
```

means:

> access data that belongs to that object.
