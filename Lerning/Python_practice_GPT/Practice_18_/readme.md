# Python Practice #18 — Stack-Based Task Manager

You’ve practiced reversing data and LIFO behavior. Now use a class to make the stack feel more like a real program.

## Task

Create a class called:

`class TaskStack:`

It should contain:

`self.tasks = []`

Create these three methods:
```python
add_task(task)
finish_task()
show_tasks()
```
The behavior should be:
```text
add_task(task) → push a task onto the stack.
finish_task() → remove and return the most recently added task.
If there are no tasks, finish_task() should return None.
show_tasks() → use a loop to print every unfinished task.
```
Then write a separate function:

`save_tasks(task_stack, filename)`

This function should save the unfinished tasks into a text file using:
```python
with open(filename, "w") as file:
Test your program
```
Use:
```python
tasks = TaskStack()

tasks.add_task("Study Python")
tasks.add_task("Finish homework")
tasks.add_task("Read book")

print("Finished:", tasks.finish_task())

tasks.show_tasks()

save_tasks(tasks, "tasks.txt")
```
Your tasks.txt should contain:
```text
Study Python
Finish homework
Important reference challenge
```
Your function receives:

`task_stack`

which refers to the same TaskStack object created here:

`tasks = TaskStack()`

**Do not create another TaskStack() inside save_tasks().**

## Requirements

Use a class, list, loop, function, append(), pop(), and file handling. Make finish_task() safe when the list is empty, and don't use global variables.

## VS Code Debugging Challenge

Put a breakpoint inside:

`finish_task()`

Watch:

- self
- self.tasks

Then step over pop() with F10.

Pay attention to something important: tasks, self, and the task_stack parameter can all refer to the same object at different points in your program.