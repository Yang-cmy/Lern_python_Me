# Python Practice #10 — Inventory Management System

```text
This exercise combines everything you've practiced so far: lists, loops, functions, classes, file handling, references, and debugging.

Scenario

You are creating a small inventory system for a shop.
```

## Step 1: Create a Product class

The class should have:

```python
id (string)
name (string)
quantity (integer)
```
## Step 2: Write a function

`load_inventory(filename)`

This function should:

- Open the file.
- Read each line.
- Each line is formatted like:
- P001,Keyboard,10
- P002,Mouse,25
- P003,Monitor,8
- Create a Product object for each line.
- Store the objects in a list.
- Return the list.

## Step 3: Write a function

`sell_product(products, product_id, amount)`

The function should:

- Search for the product with the matching product_id.
- If there is enough stock:
- Reduce the quantity.
- Otherwise:
- Print "Not enough stock"
- Modify the existing object (do not create a new one).

## Step 4: Write a function

`save_inventory(filename, products)`

Save the updated inventory back to a file in the same format:

```python
P001,Keyboard,8
P002,Mouse,25
P003,Monitor,8
```
Example

Input file (inventory.txt):

```python
P001,Keyboard,10
P002,Mouse,25
P003,Monitor,8
```

Program:

```python
products = load_inventory("inventory.txt")

sell_product(products, "P001", 2)

save_inventory("inventory_updated.txt", products)
```

Expected output file (inventory_updated.txt):

```python
P001,Keyboard,8
P002,Mouse,25
P003,Monitor,8
```

## Requirements
- ✅ Use a class.
- ✅ Store objects in a list.
- ✅ Use three functions:
    - load_inventory()
    - sell_product()
    - save_inventory()
- ✅ Use with open(...).
- ✅ Use for loops.
- ✅ Modify the original object (reference), not create a replacement.
- ❌ Do not use global variables.
- ❌ Do not use external libraries.
- ❌ Do not hardcode product data.
- VS Code Debugging Tip

## If the quantity doesn't change:

- Set a breakpoint inside sell_product().
- Press F5 to start debugging.
- Watch these variables:
- products
- product
- product.id
- product.quantity
- amount
- Step through the loop with F10 and verify:
- The correct product is found.
- The condition for enough stock is True.
- product.quantity decreases before the function exits.