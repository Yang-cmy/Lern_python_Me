class UndoStack():
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def undo(self):
        if self.is_empty():
            return None
        return self.actions.pop()

    def show_actions(self):
        if self.is_empty():
            return None
        for i in range(len(self.actions)):
            print(self.actions[i])


    def is_empty(self):
        return len(self.actions) == 0

history = UndoStack()

history.add_action("Type Hello")
history.add_action("Type World")
history.add_action("Delete World")

history.show_actions()

print("Undo:", history.undo())
print("Undo:", history.undo())

history.show_actions()