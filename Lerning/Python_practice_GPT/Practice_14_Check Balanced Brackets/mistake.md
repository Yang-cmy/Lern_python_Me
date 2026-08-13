# Practice 13 — Check Brackets with a Stack

## My goal

I wanted to check whether parentheses in a string are balanced.

Examples:

```text
()      -> True
(())    -> True
(()     -> False
())     -> False
```

A Stack works well for this because every opening bracket `(` should be matched with a closing bracket `)`.

---

## My first mistake: returning `True` too early

My first version did this:

```python
if l == target2:
    if len(stack) != 0:
        stack.pop()
        return True
```

The problem is:

```python
return True
```

was inside the loop.

That means the function stopped as soon as it found one valid pair.

For example:

```text
())
```

The program could see:

```text
(  -> push
)  -> pop
```

and immediately return:

```text
True
```

But there is still another:

```text
)
```

left to check.

So the result would be wrong.

---

## Correct idea

I should only return `False` early when I find an impossible closing bracket.

For example:

```text
)
```

There is no `(` before it.

So if the stack is empty when I see `)`:

```python
if len(stack) == 0:
    return False
```

That means the string is already invalid.

But when I successfully match a pair:

```python
stack.pop()
```

I should continue checking the rest of the text.

I should NOT return `True` yet.

---

## My corrected code

```python
def check_brackets(text):
    stack = []
    target1 = "("
    target2 = ")"

    for l in text:
        if l == target1:
            stack.append(l)

        if l == target2:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False
```

---

## How the Stack works

When I find:

```text
(
```

I push it into the stack:

```python
stack.append(l)
```

Example:

```text
Text: ((
Stack:

["(", "("]
```

When I find:

```text
)
```

I remove one `(`:

```python
stack.pop()
```

Example:

```text
Before:

["(", "("]

Read: )

After:

["("]
```

The `)` matched one previous `(`.

---

## Example 1: `(())`

Start:

```text
stack = []
```

Read first `(`:

```text
["("]
```

Read second `(`:

```text
["(", "("]
```

Read `)`:

```text
["("]
```

Read last `)`:

```text
[]
```

After the loop:

```python
len(stack) == 0
```

So:

```text
True
```

The brackets are balanced.

---

## Example 2: `(()`

Read:

```text
(  -> ["("]

(  -> ["(", "("]

)  -> ["("]
```

After checking everything:

```text
["("]
```

The stack is not empty.

That means there is an opening bracket that was never closed.

Result:

```text
False
```

---

## Example 3: `())`

Read:

```text
(  -> ["("]

)  -> []

)  -> stack is already empty
```

The last `)` has no matching `(`.

So this condition becomes true:

```python
if len(stack) == 0:
    return False
```

Result:

```text
False
```

---

# What I learned

There are two different times when I should return a result.

### Return `False` immediately

If I find a closing bracket but there is nothing in the stack:

```python
if len(stack) == 0:
    return False
```

This means the string can never become valid anymore.

### Return `True` only after the loop

I need to finish checking all characters first.

Then:

```python
if len(stack) == 0:
    return True
```

If the stack is empty, every `(` had a matching `)`.

---

# Stack idea

For this problem:

```python
stack.append("(")
```

means:

**PUSH an opening bracket**

and:

```python
stack.pop()
```

means:

**Match and remove the latest opening bracket**

This follows LIFO:

**Last In, First Out**

---

# Practical Rule

**Do not return `True` until all input has been checked.**

For bracket checking:

```text
See "("
    -> PUSH

See ")"
    -> If stack empty: False
    -> Otherwise POP

After the loop
    -> Stack empty: True
    -> Stack not empty: False
```
