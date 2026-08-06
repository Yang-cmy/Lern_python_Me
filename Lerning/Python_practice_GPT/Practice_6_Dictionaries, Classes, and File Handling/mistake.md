# Mistakes made in this project

Here are the mistakes that were made in the code and why they were wrong.

## 1. The function was not called correctly

Wrong code:
`python
save_inventory = (inventory, filename)
`

Why it was wrong:
- This creates a tuple, not a function call.
- The save_inventory() function never actually ran.
- Because of that, the file was not created or written properly.

Correct version:
`python
save_inventory(inventory, filename)
`

## 2. The whole dictionary was written to the file

Wrong code:
`python
file.write(inventory)
`

Why it was wrong:
- inventory is a dictionary object, not a string.
- Python cannot write the whole dictionary directly as text in the way you wanted.
- The file needed to contain each product as a line like 
ame,price.

Correct version:
`python
for key, product in inventory.items():
    file.write(f"{product.name},{product.price}\n")
`

## 3. The file was read incorrectly

Wrong code:
`python
with open(filename) as file:
    for line in file:
        print(file.readline())
`

Why it was wrong:
- The loop already reads each line from the file.
- Calling eadline() again inside the loop reads the next line again.
- That causes lines to be skipped or printed incorrectly.

Correct version:
`python
with open(filename) as file:
    for line in file:
        print(line, end="")
`

## 4. The code did not fully match the practice goal

Why it was wrong:
- The goal of the exercise was to save product data from objects in a dictionary into a file.
- The earlier version did not properly write the object values in the expected format.
- The corrected version now saves the data clearly and in the intended structure.
