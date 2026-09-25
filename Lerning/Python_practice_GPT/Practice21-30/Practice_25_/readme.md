## Python Practice #25 — Build a Simple Linked List

We’re moving on from Stack. According to your Python roadmap, **Arrays and Linked Lists** are part of the Data Structures & Algorithms section, so this is our next major topic. 

### Task

Create a simple **singly linked list** using two classes:

```python
class Node:
```

and:

```python
class LinkedList:
```

A `Node` should store:

```python
data
next
```

For example:

```text
10 → 20 → 30 → None
```

Each node points to the next node.

### Part 1 — `Node`

Your `Node` constructor should receive a value:

```python
Node(10)
```

and initially:

```python
next = None
```

### Part 2 — `LinkedList`

Your linked list should start with:

```python
self.head = None
```

Create a method:

```python
append(value)
```

It should add a new node to the **end** of the linked list.

Then create:

```python
display()
```

which uses a `while` loop to print every value.

### Example

```python
numbers = LinkedList()

numbers.append(10)
numbers.append(20)
numbers.append(30)

numbers.display()
```

Expected output:

```text
10
20
30
```

Internally, it should look like:

```text
head
 ↓
[10 | •] → [20 | •] → [30 | None]
```

### Requirements

Use:

* Two classes
* `Node` objects
* References through `.next`
* A `while` loop
* `self.head`

Don't use a Python list like this:

```python
self.items = []
```

The whole point is to learn how objects can be connected through **references**.

### VS Code Debugging Challenge

Set a breakpoint inside `append()`.

After:

```python
numbers.append(10)
numbers.append(20)
numbers.append(30)
```

inspect:

```python
self.head
self.head.next
self.head.next.next
```

Try to understand why these are **three different `Node` objects** connected together.

### Your Turn

Send me **only your Python code**.

I'll review your attempt first, explain any mistakes clearly, and end with **one practical rule to remember**.
