# Python Practice #10 — Inventory Management System Review

## What I did correctly

The overall structure of my program was correct.

I successfully used:

* A class to represent each product.
* A list to store multiple product objects.
* `load_inventory()` to read product data from a file.
* `sell_product()` to modify the quantity of a product.
* `save_inventory()` to write the updated data back to a file.
* `with open(...)` for file handling.
* `for` loops.
* No global variables inside the functions.
* No external libraries.
* No hardcoded product data inside the inventory system.

I also correctly modified the original `Product` object stored inside the list.

For example:

```python
for p in products:
    if p.id == product_id:
        p.quantity -= amount
```

`p` refers to the existing object inside `products`.

This means:

```python
p.quantity -= amount
```

changes the original object rather than creating a new replacement object.

---

# Main Mistake

My original condition was:

```python
if p.id == product_id and p.quantity > amount:
    p.quantity -= amount
```

The problem is the use of:

```python
>
```

instead of:

```python
>=
```

For example, suppose:

```python
p.quantity = 10
amount = 10
```

Then:

```python
10 > 10
```

is:

```python
False
```

So the program would not allow the customer to buy all 10 products, even though there is exactly enough stock.

The correct condition is:

```python
p.quantity >= amount
```

This allows both situations:

```python
quantity > amount
```

and:

```python
quantity == amount
```

---

# Better Logic for sell_product()

My original code used two separate `if` statements:

```python
if p.id == product_id and p.quantity > amount:
    p.quantity -= amount

if p.id == product_id and p.quantity < amount:
    print("Not enough stock")
```

A clearer solution is to first find the correct product:

```python
if p.id == product_id:
```

Then check the stock:

```python
if p.quantity >= amount:
    p.quantity -= amount
else:
    print("Not enough stock")
```

Full version:

```python
def sell_product(products, product_id, amount):
    for p in products:
        if p.id == product_id:
            if p.quantity >= amount:
                p.quantity -= amount
            else:
                print("Not enough stock")
```

This is easier to understand because once the correct product is found, only two possibilities exist:

```text
Enough stock
    ↓
Sell the product

Not enough stock
    ↓
Print an error
```

---

# Small Improvement: Class Name

I originally wrote:

```python
class Products:
```

A better name is:

```python
class Product:
```

Each object represents one product, so a singular class name is clearer.

Example:

```python
keyboard = Product("P001", "Keyboard", 10)
mouse = Product("P002", "Mouse", 25)
```

The list can still be plural:

```python
products = []
```

So:

```text
Product  = one object
products = list of Product objects
```

---

# Small Improvement: strip()

When reading the file, it is useful to write:

```python
id, name, quantity = line.strip().split(",")
```

instead of only:

```python
id, name, quantity = line.split(",")
```

`strip()` removes the newline character at the end of each line and any unnecessary surrounding whitespace.

---

# Corrected Version

```python
class Product:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity


def load_inventory(filename):
    products = []

    with open(filename, "r") as f:
        for line in f:
            id, name, quantity = line.strip().split(",")
            quantity = int(quantity)

            new_product = Product(id, name, quantity)
            products.append(new_product)

    return products


def sell_product(products, product_id, amount):
    for p in products:
        if p.id == product_id:
            if p.quantity >= amount:
                p.quantity -= amount
            else:
                print("Not enough stock")


def save_inventory(update_filename, products):
    with open(update_filename, "w") as f:
        for p in products:
            f.write(f"{p.id},{p.name},{p.quantity}\n")


products = load_inventory("inventory.txt")

sell_product(products, "P001", 2)

save_inventory("inventory_updated.txt", products)
```

---

# Important Concept: Object References

This exercise demonstrates an important Python concept.

Suppose the list contains:

```python
products = [
    Product("P001", "Keyboard", 10),
    Product("P002", "Mouse", 25)
]
```

When I write:

```python
for p in products:
```

`p` does not contain a completely separate copy of the product.

It refers to the same object stored in the list.

Therefore:

```python
p.quantity -= 2
```

changes the object inside `products`.

Example:

```text
Before:

products
   ↓
Product P001
quantity = 10


p
↓
same Product P001
```

After:

```python
p.quantity -= 2
```

the object becomes:

```text
Product P001
quantity = 8
```

So later:

```python
save_inventory(filename, products)
```

will save the updated quantity.

---

# And  i entirely forgot about Logical opreation

like using and or etc.

---

# Rule to Remember

When checking whether a value is "enough", always think about the equality case.

Ask:

```text
What happens when both values are equal?
```

For stock checking:

```python
quantity >= amount
```

is correct because having exactly the requested amount still means there is enough stock.

Boundary cases such as:

```python
<
>
<=
>=
==
```

are common sources of logic bugs.
