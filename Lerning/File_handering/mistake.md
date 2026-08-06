# Mistakes and Fixes — File_handering

This file documents mistakes made while opening/reading files and how to fix them, plus suggestions to improve future code.

- **Mistake:** Opening a filename without the correct path (FileNotFoundError).
  - **Fix:** Use a path relative to the script's directory:

```python
import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "demofile.txt")
with open(file_path) as f:
    print(f.read())
```

- **Mistake:** Using Windows backslashes in normal strings (e.g. "C:\Users\...") which create escape sequences.
  - **Fix:** Use a raw string `r"C:\..."`, escape backslashes `"C:\\Users\\..."`, or use forward slashes `"C:/Users/..."`.

- **Mistake:** Not using `with` to open files (may leave files unclosed).
  - **Fix:** Use `with open(...) as f:` so files are closed automatically.

- **Mistake:** Hardcoding absolute paths reduces portability and breaks when running from different CWDs.
  - **Fix:** Build paths from `__file__` (script location) or use `pathlib.Path(__file__).resolve().parent / 'demofile.txt'`.

- **Additional improvements:**
  - Use `pathlib` (object-oriented, clearer API).
  - Check existence before opening: `os.path.exists(file_path)` or `Path.exists()`.
  - Wrap file operations in `try/except` to surface useful error messages.
  - Add small helper functions to centralize file path logic.
  - Add unit tests for code that reads files and include fixtures for test files.
  - Add logging for debug information when file operations fail.

- **Where to learn:** Read the official docs (`os`, `os.path`, `pathlib`, and file I/O) and tutorials: "Python file I/O", "Python pathlib".


---

If you want, I can convert the examples to `pathlib` style or add a tiny test demonstrating the behavior.

here to learn it
Search for:
“Python os.path”
“Python file handling”
“Python pathlib”
Good sources:
Python docs: https://docs.python.org/3/library/os.html
Python docs: https://docs.python.org/3/library/pathlib.html
Tutorials: “Python file I/O” and “Python working with paths”