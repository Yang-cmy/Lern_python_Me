# Practice 12 — BrowserHistory Stack Mistakes

## My original idea

I used a Python list to store browser history.

The idea was:

* `visit()` → add a new page
* `back()` → remove the latest page
* `current_page()` → show the current page
* `is_empty()` → check whether the history is empty

This is a good situation for a **Stack** because browser history follows:

**LIFO — Last In, First Out**

The most recently visited page should be the first page removed when going back.

---

## Mistake 1: I did not call the `is_empty()` method

I wrote:

```python
if self.is_empty == 0:
```

This does not run the method.

`self.is_empty` refers to the method itself.

To actually run the method, I need parentheses:

```python
if self.is_empty():
```

Because `is_empty()` already returns either `True` or `False`, I do not need to compare it with `0`.

### Remember

```python
self.is_empty
```

means:

> Refer to the method.

While:

```python
self.is_empty()
```

means:

> Run the method and get its result.

---

## Mistake 2: `visit()` should not check whether the stack is empty

I originally wrote:

```python
def visit(self, page):
    if self.is_empty == 0:
        return None
    return self.history.append(page)
```

There is no reason to stop `visit()` when the history is empty.

If the history is empty, visiting a page should simply add the first page.

Correct version:

```python
def visit(self, page):
    self.history.append(page)
```

For example:

```text
[]

visit("google.com")

["google.com"]

visit("youtube.com")

["google.com", "youtube.com"]

visit("github.com")

["google.com", "youtube.com", "github.com"]
```

---

## Mistake 3: I used index `[0]` for the current page

I wrote:

```python
return self.history[0]
```

But `[0]` gives the **first/oldest** page.

Example:

```python
["google.com", "youtube.com", "github.com"]
```

Indexes:

```text
     0              1              2
     ↓              ↓              ↓
["google.com", "youtube.com", "github.com"]
```

So:

```python
self.history[0]
```

returns:

```text
google.com
```

But the current page should be:

```text
github.com
```

Because the newest item is at the end of the list, I should use:

```python
self.history[-1]
```

---

## Stack operations in this program

Because I use the **end of the list as the top of the stack**, the operations are:

```python
self.history.append(page)
```

= **PUSH** — add something to the top.

```python
self.history.pop()
```

= **POP** — remove something from the top.

```python
self.history[-1]
```

= **PEEK** — look at the top without removing it.

Example:

```text
Bottom                              Top
  ↓                                  ↓

["google.com", "youtube.com", "github.com"]
```

If I call:

```python
self.history.pop()
```

`github.com` is removed.

The stack becomes:

```text
["google.com", "youtube.com"]
                         ↑
                        Top
```

Now:

```python
self.history[-1]
```

returns:

```text
youtube.com
```

---

## Correct version

```python
class BrowserHistory():
    def __init__(self):
        self.history = []

    def visit(self, page):
        self.history.append(page)

    def back(self):
        if self.is_empty():
            return None
        return self.history.pop()

    def current_page(self):
        if self.is_empty():
            return None
        return self.history[-1]

    def is_empty(self):
        return len(self.history) == 0


browser = BrowserHistory()

browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")

print(browser.current_page())

browser.back()

print(browser.current_page())
```

Output:

```text
github.com
youtube.com
```

---

# What I should remember

When using a Python list as a Stack:

```python
stack.append(value)   # PUSH
stack.pop()           # POP
stack[-1]             # PEEK
```

And when calling a method:

```python
method()
```

not:

```python
method
```

## Practical Rule

**If I use `append()` and `pop()` for a Stack, the end of the list (`[-1]`) is the top of the Stack.**
