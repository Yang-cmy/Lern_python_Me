class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")

        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")

        return self.items.pop()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) > self.max_size


stack = Stack(3)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Top:", stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())