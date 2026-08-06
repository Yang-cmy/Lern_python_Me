class Student():
    def __init__(self, name, score): #i finally know how useful class is to modify a data using __init__ function
        self.name = name
        self.score = score

student1 = Student("Alice", 85) #No shit how could i know that it had to create seperate object first in order to Modify it
student2 = Student("Bob", 92) #And this is object by the way
student3 = Student("Charlie", 78)

def load_students(filename): #create a function this function do all shit contain everything i dont even know about
    students =[]

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            name, score = line.split(",")
            score = int(score)

            new_student = Student(name, score)
            students.append(new_student)

        return students

def print_students(students): #wtf how is this work?
    for student in students:
        print(f"{student.name} - {student.score}")

filename = (r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_5_Reading from a File into Objects\students.txt")

students = load_students(filename)
print_students(students)