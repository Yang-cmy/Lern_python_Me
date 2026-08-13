class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
print(stack.pop())
print(stack.peek())

The output will be:

30
30
20
Let's understand it piece by piece

The first part creates our own Stack class:

class Stack:

You can think of a class as a blueprint. Later:

stack = Stack()

creates an actual stack from that blueprint.

Then:

def __init__(self):
    self.items = []

__init__() runs automatically when you write:

stack = Stack()

So initially:

stack.items
↓
[]

The stack is empty.

Your Week 4 notes describe the important position in a stack as the top. Since we're using a Python list, we're going to treat the rightmost item as the top.

For example:

[10, 20, 30]
         ↑
        TOP
push()
def push(self, item):
    self.items.append(item)

Your notes specifically say that Python's:

append()

works like the Stack push() operation.

So:

stack.push(10)

means internally:

self.items.append(10)

Stack:

[10]
 ↑
TOP

Then:

stack.push(20)

becomes:

[10, 20]
     ↑
    TOP

Then:

stack.push(30)

becomes:

[10, 20, 30]
         ↑
        TOP

Notice that 30 was the last value pushed in.

peek()
def peek(self):
    if self.is_empty():
        return None
    return self.items[-1]

Your notes say:

s[-1]

accesses the top element.

For our stack:

index:      0   1   2
           ↓   ↓   ↓
items =   [10, 20, 30]
                    ↑
                   -1

Therefore:

self.items[-1]

returns:

30

But importantly, it doesn't remove 30.

So:

print(stack.peek())

prints:

30

while the stack is still:

[10, 20, 30]
pop()
def pop(self):
    if self.is_empty():
        return None
    return self.items.pop()

Python's list:

pop()

removes the last/rightmost element.

Before:

[10, 20, 30]
         ↑
        TOP

After:

stack.pop()

it returns:

30

and the stack becomes:

[10, 20]
     ↑
    TOP

That's LIFO:

Push order:
10 → 20 → 30

Pop order:
30 → 20 → 10

The Last In was 30, so 30 is the First Out.

Why do we check is_empty()?

This is the safety requirement from your exercise.

Normally:

items = []
items.pop()

would cause an error because there is nothing to remove.

Your Week 4 notes call this situation Stack Underflow: trying to pop() an empty stack.

So we protect ourselves:

if self.is_empty():
    return None

The same protection is used for peek() because:

[][ -1 ]

would also crash.

is_empty()
def is_empty(self):
    return len(self.items) == 0

Suppose:

self.items = []

Then:

len(self.items)

is:

0

Therefore:

len(self.items) == 0

becomes:

0 == 0

which is:

True

But if:

self.items = [10, 20]

then:

2 == 0

is:

False

So:

[]            → True
[10]          → False
[10, 20, 30]  → False
Now do the debugging challenge

Add:

print(stack.items)

after operations:

stack = Stack()

print(stack.items)

stack.push(10)
print(stack.items)

stack.push(20)
print(stack.items)

stack.push(30)
print(stack.items)

print(stack.peek())
print(stack.items)

print(stack.pop())
print(stack.items)

print(stack.peek())
print(stack.items)

You'll see something similar to:

[]
[10]
[10, 20]
[10, 20, 30]
30
[10, 20, 30]
30
[10, 20]
20
[10, 20]

That also shows an important difference:

peek()
[10, 20, 30] → [10, 20, 30]

pop()
[10, 20, 30] → [10, 20]

peek() looks at the top.

pop() takes the top.

One rule worth remembering

Stack = LIFO. With a Python list, think of the right side as TOP: append() pushes, pop() removes, and [-1] peeks.

Also, your Week 4 notes mention a size() method, but your Practice #11 only requires push, pop, peek, and is_empty, so you don't need to add size() unless your teacher asks for it.