# Python Practice #12 — Browser Back Button with a Stack

Build a tiny browser history program. This continues your Stack coursework while practicing lists, loops, functions, classes, and references.

Create a class called BrowserHistory containing:

`self.history = []`

Implement these three methods:

```python
visit(page)
back()
current_page()
```
The behavior should be:

- `visit(page)` pushes a page onto the history stack.
- `back()` removes the current page and returns to the previous page.
- `current_page()` returns the page at the top of the stack.
- If there is only one page left, `back()` should do nothing.

Test it with:

```python
browser = BrowserHistory()

browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")

print(browser.current_page())

browser.back()

print(browser.current_page())
```

Expected output:

```python
github.com
youtube.com
```
Then add one extra challenge: write a separate function

`show_history(browser)`

that uses a loop to print every page currently stored in `browser.history`.

For this exercise, don't use another list and don't create a new `BrowserHistory` object inside your functions. I specifically want you to modify the same object so you get more practice with object references.

VS Code debugging challenge: Put a breakpoint inside `back()`. Run with F5, then use F10 and watch `self.history` before and after `pop()`.

Write it yourself first and send me your code. I’ll wait for your attempt before explaining anything or showing a solution.