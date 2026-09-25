class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return None

        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

    def save_stack(self, filename):
        with open(filename, "w") as f:
            for l in self.items:
                f.write(f"{l}\n")

    def load_stack(self, filename, max_size):
        with open(filename, "r") as f:
            for l in f:
                cleaned = l.rstrip("\n")
                self.items.append(cleaned)

        return self.items


filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_22_\stack.txt"
stack = Stack(5)
stack.load_stack(filename, 5)

print(stack.items)
print("Top:", stack.peek())