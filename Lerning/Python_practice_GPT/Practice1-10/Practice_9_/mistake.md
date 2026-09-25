# Python Practice #9 — Mistakes and What I Learned

## Practice Topic

Student Database — Read, Update, and Save

This exercise used:

* Classes
* Objects
* Lists
* Functions
* File handling
* Loops
* Object attributes
* References / modifying existing objects

---

# 1. Mistake: Looping Through `filename` Instead of the Open File

## Wrong

```python
def load_student(filename):
    students = []

    with open(filename, "r") as f:
        for student in filename:
            ...
```

## Why It Was Wrong

`filename` is only a string containing the path or filename.

For example:

```python
filename = "students.txt"
```

So this:

```python
for student in filename:
```

would loop through the characters:

```text
s
t
u
d
e
n
t
s
.
t
x
t
```

It does not read the file contents.

## Correct

```python
with open(filename, "r") as f:
    for line in f:
        ...
```

Here:

* `filename` = location/name of the file
* `f` = opened file object
* `line` = one line from the file

Example:

```text
First loop:
line = "001,Alice,80\n"

Second loop:
line = "002,Bob,75\n"

Third loop:
line = "003,Charlie,90\n"
```

## Rule to Remember

> `filename` tells Python where the file is.
> `f` is the actual opened file that I can read from.

---

# 2. Mistake: Using the Same Variable Name for Different Purposes

## Wrong Idea

```python
student = []

for student in ...:
```

I first used `student` as a list, and then reused `student` as the loop variable.

This makes the code confusing and can overwrite the meaning of the variable.

## Better

```python
students = []

for line in f:
    ...
```

Use plural names for collections:

```python
students
```

and singular names for one object:

```python
student
```

## Rule to Remember

> Use plural names for lists and singular names for one item.

Example:

```python
students = []

for student in students:
    ...
```

---

# 3. Mistake: Not Understanding How to Separate File Data

The file contained:

```text
001,Alice,80
002,Bob,75
003,Charlie,90
```

At first, each line is one string:

```python
"001,Alice,80"
```

I needed to separate it into three values.

## Solution

```python
line_id, line_name, line_score = line.split(",")
```

Result:

```python
line_id = "001"
line_name = "Alice"
line_score = "80"
```

Then convert the score into an integer:

```python
line_score = int(line_score)
```

Now:

```python
line_score = 80
```

instead of:

```python
line_score = "80"
```

## Rule to Remember

> `split(",")` separates a string wherever a comma appears.

---

# 4. Mistake: Misspelling `__init__`

## Wrong

```python
class student_info:
    def __inbit__(self, student_id, name, score):
        ...
```

I accidentally wrote:

```python
__inbit__
```

instead of:

```python
__init__
```

Python did not recognize it as the constructor.

## Correct

```python
class student_info:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
```

Then I can create an object:

```python
new_student = student_info("001", "Alice", 80)
```

## Rule to Remember

> Python special method names must be spelled exactly.

Especially:

```python
__init__
```

---

# 5. Mistake: Giving `append()` Three Arguments

## Wrong

```python
students.append(line_id, line_name, line_score)
```

`append()` accepts only one item.

I was giving it three:

```text
line_id
line_name
line_score
```

## Correct Idea

First create one object:

```python
new_student = student_info(line_id, line_name, line_score)
```

Then append that one object:

```python
students.append(new_student)
```

Now the list contains Student objects:

```text
students
[
    Student object,
    Student object,
    Student object
]
```

## Rule to Remember

> `append()` adds one item to a list.

If multiple pieces of data belong together, first put them into one object.

---

# 6. Confusion: Why `print(students)` Showed an Object Address

I tried:

```python
print(students)
```

and saw something like:

```text
[<__main__.student_info object at 0x00000244B5CE8C20>]
```

At first, I thought something was wrong.

But this actually means the list successfully contains a `student_info` object.

Python is showing:

```text
object type + memory location
```

The data is still inside the object.

I can access it using:

```python
for s in students:
    print(s.student_id, s.name, s.score)
```

Example output:

```text
001 Alice 80
002 Bob 75
003 Charlie 90
```

## Rule to Remember

> Seeing `<... object at 0x...>` does not mean the object is empty.

It means Python is showing its default object representation.

---

# 7. Mistake: Appending the New Score Instead of Updating the Object

My first attempt at `add_bonus()` was:

```python
def add_bonus(students, bonus):
    for s in students:
        new_score = s.score + bonus
        students.append(new_score)
```

## Why It Was Wrong

`students` is supposed to contain Student objects:

```text
[
    Student,
    Student,
    Student
]
```

But I was appending integers:

```text
[
    Student,
    Student,
    Student,
    85
]
```

That would mix Student objects and numbers in the same list.

Also, the requirement said:

> Modify the existing objects.

So I did not need to append anything.

## Correct

```python
def add_bonus(students, bonus):
    for s in students:
        new_score = s.score + bonus
        s.score = new_score
```

This can also be written as:

```python
def add_bonus(students, bonus):
    for s in students:
        s.score = s.score + bonus
```

or:

```python
def add_bonus(students, bonus):
    for s in students:
        s.score += bonus
```

## Important Concept

When:

```python
s
```

refers to a Student object, changing:

```python
s.score
```

changes the score inside that existing object.

Example:

```text
Before:

Alice object
score = 80

After:

Alice object
score = 85
```

It is still the same Alice object.

## Rule to Remember

> If I want to change an object, change its attribute directly.

Example:

```python
object.attribute = new_value
```

---

# 8. Mistake: Assigning the Result of `add_bonus()`

I almost called the function like this:

```python
students = add_bonus(students, 5)
```

But my function does not return anything:

```python
def add_bonus(students, bonus):
    for s in students:
        s.score += bonus
```

A function without `return` automatically returns:

```python
None
```

So this:

```python
students = add_bonus(students, 5)
```

would make:

```python
students = None
```

## Correct

```python
add_bonus(students, 5)
```

The function already modifies the objects.

## Rule to Remember

> Do not assign a function result unless the function actually returns something I need.

---

# 9. Mistake: Wrong Attribute Name in `save_students()`

I wrote:

```python
s.student.id
```

But my class had:

```python
self.student_id
```

So the correct attribute is:

```python
s.student_id
```

## Correct

```python
f.write(f"{s.student_id},{s.name},{s.score}")
```

## Rule to Remember

> Object attributes must match exactly what was created in `__init__`.

If I create:

```python
self.student_id
```

I access it with:

```python
object.student_id
```

---

# 10. Mistake: Forgetting `\n` When Writing the File

Without:

```python
\n
```

this:

```python
f.write(f"{s.student_id},{s.name},{s.score}")
```

would create:

```text
001,Alice,85002,Bob,80003,Charlie,95
```

Everything would be on one line.

## Correct

```python
f.write(f"{s.student_id},{s.name},{s.score}\n")
```

Result:

```text
001,Alice,85
002,Bob,80
003,Charlie,95
```

## Rule to Remember

> `\n` means "start a new line."

---

# 11. Mistake: Putting `return students` Inside the Loop

I wrote:

```python
def load_student(filename):
    students = []

    with open(filename, "r") as f:
        for line in f:
            ...
            students.append(new_student)

            return students
```

## Why It Was Wrong

`return` immediately stops the function.

So after reading Alice:

```text
Read Alice
↓
Create Alice object
↓
Append Alice
↓
return
↓
Function stops
```

Bob and Charlie would never be processed.

## Correct

```python
def load_student(filename):
    students = []

    with open(filename, "r") as f:
        for line in f:
            line_id, line_name, line_score = line.split(",")
            line_score = int(line_score)

            new_student = student_info(
                line_id,
                line_name,
                line_score
            )

            students.append(new_student)

    return students
```

Notice that `return` is outside the loop.

## Rule to Remember

> `return` ends the whole function immediately.

If I want a loop to finish first, put `return` after the loop.

---

# 12. Mistake: Using the Same File for Input and Output

Originally, I considered:

```python
students = load_student(filename)

add_bonus(students, 5)

save_students(filename, students)
```

This would overwrite the original `students.txt` because:

```python
open(filename, "w")
```

uses write mode.

Write mode clears the previous contents.

It is safer for this exercise to use:

```python
input_filename
```

and:

```python
output_filename
```

Example:

```python
students = load_student(input_filename)

add_bonus(students, 5)

save_students(output_filename, students)
```

## Rule to Remember

> `"r"` reads a file.
> `"w"` writes a file and replaces its existing contents.

---

# Final Correct Program

```python
class student_info:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score


def load_student(filename):
    students = []

    with open(filename, "r") as f:
        for line in f:
            line_id, line_name, line_score = line.split(",")
            line_score = int(line_score)

            new_student = student_info(
                line_id,
                line_name,
                line_score
            )

            students.append(new_student)

    return students


def add_bonus(students, bonus):
    for s in students:
        new_score = s.score + bonus
        s.score = new_score


def save_students(output_filename, students):
    with open(output_filename, "w") as f:
        for s in students:
            f.write(
                f"{s.student_id},{s.name},{s.score}\n"
            )


filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_9_\students.txt"

output_filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_9_\update_students.txt"


students = load_student(filename)

add_bonus(students, 5)

save_students(output_filename, students)
```

---

# Program Flow

```text
students.txt
      |
      v
load_student()
      |
      v
[
 Student("001", "Alice", 80),
 Student("002", "Bob", 75),
 Student("003", "Charlie", 90)
]
      |
      v
add_bonus(students, 5)
      |
      v
[
 Student("001", "Alice", 85),
 Student("002", "Bob", 80),
 Student("003", "Charlie", 95)
]
      |
      v
save_students()
      |
      v
update_students.txt
```

---

# Biggest Things I Learned

## 1. File Variable vs Filename

```python
filename
```

is only the file path.

```python
f
```

is the opened file.

---

## 2. A List Can Store Objects

```python
students.append(new_student)
```

The list does not have to contain only strings or integers.

It can contain objects.

---

## 3. Objects Store Related Information Together

Instead of keeping:

```python
"001"
"Alice"
80
```

separately, I can create:

```python
student_info("001", "Alice", 80)
```

which keeps all information about one student together.

---

## 4. Modify Object Attributes Directly

```python
s.score += bonus
```

changes the score inside the existing object.

I do not need to create another object or append another score.

---

## 5. `return` Stops a Function

```python
return
```

does not just return a value.

It also immediately ends the function.

So indentation matters a lot.

---

## 6. `append()` Adds One Item

```python
students.append(new_student)
```

is correct because `new_student` is one object.

This is wrong:

```python
students.append(id, name, score)
```

because that is three arguments.

---

# Debugging Lessons From This Practice

When Python gives an error:

1. Read the final line of the traceback.
2. Look at the exact line number Python points to.
3. Check what type of value each variable contains.
4. Check spelling carefully, especially special methods such as `__init__`.
5. Check indentation.
6. Ask whether the function should modify something or return something.
7. Follow the data step by step instead of trying to understand the entire program at once.

---

# Practical Rule to Remember

> Follow the data.

For this program:

```text
File line
→ split values
→ convert score
→ create object
→ append object
→ modify object
→ write object attributes back to file
```

If I know what form the data has at each step, the code becomes much easier to understand.
