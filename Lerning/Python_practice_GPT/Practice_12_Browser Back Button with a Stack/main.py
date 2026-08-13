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