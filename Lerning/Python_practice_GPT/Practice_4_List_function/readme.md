Python Practice #4 — References, Lists, and Functions

Today's exercise focuses on one of the most important Python concepts: references (how variables point to the same object), along with lists, loops, and functions.

Task

Write a function called:

add_bonus(scores, bonus)

The function should:

Accept:
scores: a list of integers.
bonus: an integer.
Use a for loop to add bonus to every score in the original list.
Modify the original list (do not create a new list).
Return the modified list.
Example
grades = [70, 85, 90]

add_bonus(grades, 5)

print(grades)

Expected output:

[75, 90, 95]
Constraints
✅ Use a for loop.
✅ Modify the existing list.
❌ Do not use list comprehensions.
❌ Do not create another list like new_scores = [].
VS Code Debugging Tip

If your list doesn't change:

Set a breakpoint inside the loop.
Press F5 to start debugging.
Watch:
scores
the loop variable
the current index (if you're using one)
Step through each iteration with F10 and check whether the values inside scores are actually being updated.

Hint: Think carefully about the difference between changing a loop variable and changing an element inside a list.