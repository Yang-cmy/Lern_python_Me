class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def average(self):
        if len(self.score) == 0: # when compare integer, use == not =
            return 0

        total = 0
        for s in self.score:
            total += s
        return total/len(self.score) # If the lower line goes invisible that mean your indentation is wrong


def save_report(students, filename):
    with open(filename, "w") as f:
        for s in students:
            f.write(f"{s.name} - Average: {s.average()}\n")
            print(f"{s.name} - Average: {s.average()}")


filename = (r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_8_\report.txt")

students = [
    student("Alice", [80, 90, 85]),
    student("Bob", [95, 90, 89]),
    student("Charlie", [70, 80, 84])
]

save_report(students, filename)
