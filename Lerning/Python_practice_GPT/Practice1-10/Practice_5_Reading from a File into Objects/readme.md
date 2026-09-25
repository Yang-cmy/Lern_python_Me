Python Practice #5 — Reading from a File into Objects

Today's exercise combines file handling, classes, lists, loops, and functions.

Task

Suppose a file named students.txt contains:

Alice,85
Bob,92
Charlie,78

Write a Python program that:

Creates a class named Student with:
name
score
Writes a function named load_students(filename) that:
Opens the file.
Reads each line.
Splits the line using ,.
Creates a Student object.
Stores each object in a list.
Returns the list.
Write another function named print_students(students) that prints:
Alice - 85
Bob - 92
Charlie - 78
Constraints
✅ Use a class.
✅ Use a list to store the objects.
✅ Use a for loop.
✅ Use with open(...).
✅ Convert the score to an integer.
❌ Do not hardcode the student names or scores.
❌ Do not use external libraries.
VS Code Debugging Tip

If your program crashes while reading the file:

Set a breakpoint on the line that reads each file line.
Press F5 to start debugging.
Watch these variables:
line
parts (after using split(","))
name
score
students
Step through one line at a time with F10 and verify that each Student object is created correctly before it's added to the list.