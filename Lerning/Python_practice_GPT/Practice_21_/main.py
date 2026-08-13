class Editor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do_action(self,item):
        self.undo_stack.append(item)
        self.redo_stack.clear()

    def undo(self):
        if self.is_undoempty():
            return None
        recent_action = self.undo_stack.pop()
        self.redo_stack.append(recent_action)

    def redo(self):
        if self.is_redoempty():
            return None
        recent_action = self.redo_stack.pop()
        self.undo_stack.append(recent_action)

    def show_history(self):
        for i in self.undo_stack:
            print(i)

    def is_undoempty(self):
        return len(self.undo_stack) == 0

    def is_redoempty(self):
        return len(self.redo_stack) == 0



editor = Editor()

editor.do_action("Type A")
editor.do_action("Type B")
editor.do_action("Delete B")

editor.undo()
editor.undo()

editor.redo()

editor.show_history()
