## Python Practice #7 — Updating Objects from a File

Today's exercise combines classes, file handling, lists, loops, and references. It also mirrors a task you'll often see in real programs: loading data and updating existing objects.

## Task

## Suppose you already have these Student objects:
```python
students = [
    Student("Alice", 80),
    Student("Bob", 75),
    Student("Charlie", 90)
]
```
## A file named updates.txt contains:
```python
Alice,85
Charlie,95
```
## Write a function:

`update_scores(students, filename)`

## The function should:

- Open updates.txt.
- Read one line at a time.
- Split each line using ,.
- find the matching Student object by name.
- Update the existing object's score (do not create a new Student object).
- Leave students not listed in the file unchanged.
- Expected Result

## Before updating:
```python
Alice - 80
Bob - 75
Charlie - 90
```
## After calling:

`update_scores(students, "updates.txt")`

## The list should contain:

```python
Alice - 85
Bob - 75
Charlie - 95
```
## Constraints
- ✅ Use a Student class.
- ✅ Store students in a list.
- ✅ Use nested for loops (one to read the file, one to search the list).
- ✅ Use with open(...).
- ❌ Do not create a new list.
- ❌ Do not create new Student objects.
- ❌ Do not use dictionaries for this exercise.