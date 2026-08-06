class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Alice", 85)
student2 = Student("Bob", 92)
student3 = Student("Charlie", 78)

def load_students(filename):
    students =[]

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            name, score = line.split(",")
            score = int(score)

            new_student = Student(name, score)
            students.append(new_student)

        return students

def print_students(students):
    for student in students:
        print(f"{student.name} - {student.score}")

filename = (r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_5_Reading from a File into Objects\students.txt")

students = load_students(filename)
print_students(students)