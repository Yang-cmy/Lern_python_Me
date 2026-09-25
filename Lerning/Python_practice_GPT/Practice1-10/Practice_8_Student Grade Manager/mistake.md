# Mistakes found in the previous `main.py` (original code submitted)

1. Wrong empty-check for scores
	- What was wrong: `if self.score == 0:` compares a list to an int.
	- Why: `self.score` is a list; comparing it to `0` always fails and is semantically incorrect.
	- Fix: check length: `if len(self.score) == 0:` (or `if not self.score:`).

2. Loop variable name mismatch
	- What was wrong: `for scores in self.score: total += score` — loop uses `scores` but adds `score` (undefined).
	- Why: referencing the wrong variable raises `NameError` at runtime.
	- Fix: use a single name consistently, e.g. `for s in self.score: total += s`.

3. Iterating students incorrectly
	- What was wrong: `for key, name in students.item():` — lists have no `.item()` and the unpacking is wrong.
	- Why: `.item()` doesn't exist on Python lists; this raises `AttributeError`.
	- Fix: iterate directly: `for s in students:` and use the instance `s`.

4. Using the class name instead of the instance and not calling methods
	- What was wrong: `f"{student.name} - Average: {student.average}"` uses the class name `student` and the method object.
	- Why: `student` is the class, not the instance from the loop; `student.average` is a function object, not its return value.
	- Fix: use the loop variable and call the method: `f"{s.name} - Average: {s.average()}\n"`.

5. Report never produced / not calling `save_report`
	- What was wrong: the code defined `save_report()` but never called it.
	- Why: no file is created unless you call the function.
	- Fix: call `save_report(students, filename)` after building `students`.

6. Naming and style issues (PEP8 / clarity)
	- What: class named `student` (lowercase) — PEP8 recommends `Student`.
	- Why: `Student` is clearer and follows conventions, improving readability.
	- Fix: rename class to `Student` and instantiate with `Student(...)`.

7. File I/O robustness and formatting
	- What: `f.write` used without a newline and without error handling.
	- Why: lines may concatenate; file errors not caught.
	- Fix: write `f.write(f"{s.name} - Average: {s.average()}\n")` and wrap file operations in try/except if needed.

8. Path portability
	- What: hard-coded absolute Windows path (raw string) reduces portability.
	- Fix: consider a relative path or `os.path.join()` for cross-platform code.

Suggested minimal corrected `save_report()` example:

```
def save_report(students, filename):
	 with open(filename, 'w', encoding='utf-8') as f:
		  for s in students:
				f.write(f"{s.name} - Average: {s.average()}\n")

# call it
save_report(students, filename)
```

Summary: the runtime exceptions came from wrong type comparisons, a mismatched loop variable name, iterating the students list incorrectly, referencing the class instead of instance, and forgetting to call the report function. Fixing those makes the program run and write the expected report.
