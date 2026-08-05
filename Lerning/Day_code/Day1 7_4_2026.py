import tkinter as tk
from tkinter import font
from datetime import datetime

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("400x150")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a1a')
        
        # Create time label
        self.time_label = tk.Label(
            root, 
            font=("Arial", 80, "bold"),
            background='#1a1a1a',
            foreground='#00ff00'
        )
        self.time_label.pack(expand=True)
        
        # Create date label
        self.date_label = tk.Label(
            root,
            font=("Arial", 14),
            background='#1a1a1a',
            foreground='#00aa00'
        )
        self.date_label.pack()
        
        # Start updating time
        self.update_time()
    
    def update_time(self):
        # Get current time and date
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%A, %B %d, %Y")
        
        # Update labels
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        
        # Schedule next update after 1000ms (1 second)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()
