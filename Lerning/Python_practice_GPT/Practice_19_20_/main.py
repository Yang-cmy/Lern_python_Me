class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return None
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size


stack = Stack(5)

stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.peek())
print("Size:", stack.size())

print("Removed:", stack.pop())

print("Top:", stack.peek())
print("Size:", stack.size())
        
