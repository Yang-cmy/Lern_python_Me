# Practice 16 — Decimal to Binary Using a Stack

## Score

**7/10**

## What I did well

I correctly understood most of the algorithm:

* I created a list as a Stack.
* I used a `while` loop.
* I used `% 2` to calculate the remainder.
* I used `// 2` for integer division.
* I used `append()` to push values into the Stack.
* I used `pop()` to remove values in reverse order.
* I understood that the Stack is needed because binary digits are generated backwards.

The main mistake was in how I built the final string.

---

# My first attempt

```python
def decimal_to_binary(number):
    stack = []

    while number > 0:
        remain = number % 2
        number = number // 2

        stack.append(remain)

    results = ""

    while len(stack) > 0:
        results = stack.pop()
        results += str(results)

    return results
```

---

# Mistake 1 — Replacing `results`

I wrote:

```python
results = stack.pop()
```

But `results` was originally:

```python
results = ""
```

which is a string.

When I do:

```python
results = stack.pop()
```

I replace the string with an integer.

For example:

```python
stack = [0, 1, 0, 1]
```

Then:

```python
results = stack.pop()
```

makes:

```python
results = 1
```

Now `results` is an integer instead of a string.

What I actually wanted was to keep the existing string and add the popped digit to it.

Correct idea:

```python
last_binary = stack.pop()
results += str(last_binary)
```

---

# Mistake 2 — Adding `results` to itself

I wrote:

```python
results += str(results)
```

Suppose:

```python
results = 1
```

Then:

```python
str(results)
```

becomes:

```python
"1"
```

So conceptually I am trying to combine:

```text
1 + "1"
```

That is not what I want.

I don't want to convert `results`.

I want to convert the value I just popped from the Stack.

Correct:

```python
last_binary = stack.pop()
results += str(last_binary)
```

---

# Why `str()` is needed

The Stack contains integers:

```python
[0, 1, 0, 1]
```

But my result is a string:

```python
results = ""
```

Python cannot directly do:

```python
results += 1
```

because one value is a string and the other is an integer.

So I need:

```python
str(1)
```

which becomes:

```python
"1"
```

Then this works:

```python
results += "1"
```

---

# Correct Code

```python
def decimal_to_binary(number):
    stack = []

    while number > 0:
        remain = number % 2
        number = number // 2

        stack.append(remain)

    results = ""

    while len(stack) > 0:
        last_binary = stack.pop()
        results += str(last_binary)

    return results
```

---

# How the Algorithm Works

For:

```python
decimal_to_binary(10)
```

## Step 1 — Find the remainders

Start:

```text
number = 10
stack = []
```

First loop:

```text
10 % 2 = 0
10 // 2 = 5

stack = [0]
```

Next:

```text
5 % 2 = 1
5 // 2 = 2

stack = [0, 1]
```

Next:

```text
2 % 2 = 0
2 // 2 = 1

stack = [0, 1, 0]
```

Next:

```text
1 % 2 = 1
1 // 2 = 0

stack = [0, 1, 0, 1]
```

Now:

```text
number = 0
```

so the first `while` loop stops.

---

# Step 2 — Pop the Stack

The Stack is:

```text
[0, 1, 0, 1]
          ↑
         TOP
```

Start:

```python
results = ""
```

First pop:

```text
pop() → 1

results = "1"
```

Second pop:

```text
pop() → 0

results = "10"
```

Third pop:

```text
pop() → 1

results = "101"
```

Fourth pop:

```text
pop() → 0

results = "1010"
```

Final answer:

```text
1010
```

---

# Why Stack Is Useful Here

The decimal conversion generates the binary digits backwards.

For `10`:

```text
10 % 2 = 0
5 % 2  = 1
2 % 2  = 0
1 % 2  = 1
```

Generated order:

```text
0 1 0 1
```

But the correct binary is:

```text
1 0 1 0
```

The Stack reverses the order because it uses:

**LIFO — Last In, First Out**

```text
PUSH:

0
1
0
1

Stack:
[0, 1, 0, 1]
          ↑
         TOP
```

Then:

```text
POP → 1
POP → 0
POP → 1
POP → 0
```

Result:

```text
1010
```

---

# One More Mistake From My Earlier Attempt

Earlier I used:

```python
number = number / 2
```

This uses normal division and produces floating-point numbers.

Example:

```text
10 / 2 = 5.0
5.0 / 2 = 2.5
```

For this algorithm, I need integer division:

```python
number = number // 2
```

Example:

```text
10 // 2 = 5
5 // 2 = 2
2 // 2 = 1
1 // 2 = 0
```

---

# What I Learned

This problem has two separate phases:

```text
PHASE 1

Decimal
   ↓
calculate remainder
   ↓
PUSH into Stack
```

Then:

```text
PHASE 2

Stack
  ↓
POP
  ↓
convert integer to string
  ↓
add to result
```

I should not mix these two jobs together.

---

# Practical Rule

**When building a string inside a loop, initialize it once and add new values to it instead of replacing it.**

Correct pattern:

```python
result = ""

while something:
    value = ...
    result += str(value)
```

For this Stack problem:

```text
remainder → PUSH → POP → str() → add to result
```
