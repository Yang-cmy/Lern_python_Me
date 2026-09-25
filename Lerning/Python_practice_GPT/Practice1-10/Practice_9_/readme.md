# python Practice #9 — Student Database (Read, Update, Save)

This exercise combines lists, loops, functions, classes, file handling, references, and debugging. It's similar to a small real-world program.

You are building a simple student database.

## Step 1: Create a Student class

The class should have:

`student_id (string)`
`name (string)`
`score (integer)`

## Step 2: Write a function

`load_students(filename)`

**This function should:**

- Open a file.
- Read each line.
- Each line is formatted like:
- 001,Alice,80
- 002,Bob,75
- 003,Charlie,90
- Create a Student object for each line.
- Store the objects in a list.
- Return the list.

## Step 3: Write another function

`add_bonus(students, bonus)`

**It should:**

- Receive the list of Student objects.
- Use a for loop.
- Add bonus points to every student's score.
- Modify the existing objects (do not create new objects).

## Step 4: Write another function

`save_students(filename, students)`

**It should save the updated data back to a file in exactly this format:**

>- 001,Alice,85
>- 002,Bob,80
>- 003,Charlie,95

**Example**

`Input file (students.txt):`

>- 001,Alice,80
>- 002,Bob,75
>- 003,Charlie,90

**Program:**
```python
students = load_students("students.txt")

add_bonus(students, 5)

save_students("students_updated.txt", students)
```
**Expected output file (students_updated.txt):**

>- 001,Alice,85
>- 002,Bob,80
>- 003,Charlie,95

## Requirements

- ✅ Use a class.
- ✅ Use a list of Student objects.
- ✅ Use three functions:
    - load_students()
    - add_bonus()
    - save_students()
- ✅ Use with open(...).
- ✅ Use for loops.
- ✅ Modify the original objects.
- ❌ Do not use global variables.
- ❌ Do not use external libraries.
- ❌ Do not hardcode the student data.