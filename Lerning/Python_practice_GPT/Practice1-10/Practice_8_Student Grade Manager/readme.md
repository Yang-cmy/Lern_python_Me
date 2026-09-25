# Python Practice #8 — Student Grade Manager

Today's exercise combines classes, lists, functions, file handling, and debugging. It also introduces a little more program organization.

Task

Create a program that manages student grades.

## Step 1: Create a Student class

### The class should have:

```python
name (string)
scores (list of integers)
```
### Add a method:

```python
average()
```
### that:

Uses a for loop to calculate the average.
Returns 0 if the student has no scores.

## Step 2: Write a function

`save_report(students, filename)`

### This function should:

Open the file using:
with open(filename, "w") as file:
Use a for loop to write one line for each student.

### Format:

```python
Alice - Average: 85.0
Bob - Average: 91.5
Charlie - Average: 78.0
```
## Step 3: Create data

Create at least 3 Student objects.

### Example:
```python
students = [
    Student("Alice", [80, 90, 85]),
    Student("Bob", [95, 90, 89]),
    Student("Charlie", [70, 80, 84])
]
```
### Call:

- save_report(students, "report.txt")
- Expected report.txt
- Alice - Average: 85.0
- Bob - Average: 91.3
- Charlie - Average: 78.0

(The averages should match your calculations.)

## Constraints
- ✅ Use a class.
- ✅ Store students in a list.
- ✅ Use at least one function besides the class method.
- ✅ Use a for loop.
- ✅ Use with open(...).
- ❌ Do not use sum() or statistics.mean().
- ❌ Do not hardcode the output lines.