# Python Practice #6 — Dictionaries, Classes, and File Handling

This exercise builds on your previous work and introduces a common real-world pattern: saving object data to a file.

## Task

Create a class called `Product`.

The class should have:

- `name` (string)
- `price` (float)

Then write two functions:

1. `create_inventory()`
- Create an empty dictionary called `inventory`.
- Add at least 3 `Product` objects to it.
- Use the product name as the dictionary key.

Example:
```python
inventory = {
    "Pen": Product("Pen", 15.0),
    "Notebook": Product("Notebook", 45.5)
}
```
Return the dictionary.

---

2. `save_inventory(inventory, filename)`
- Open the file using:
```python
with open(filename, "w") as file:
```
- Use a for loop to write each product in this format:
```python
Pen,15.0
Notebook,45.5
Eraser,8.5
```
Each product should be on its own line.

***

## Expected Output File (inventory.txt)
```python
Pen,15.0
Notebook,45.5
Eraser,8.5
```
## Constraints
- ✅ Use a class.
- ✅ Use a dictionary that stores Product objects.
- ✅ Use a for loop.
- ✅ Use with open(...).
- ❌ Do not hardcode each file.write() separately.
- ❌ Do not use external libraries.