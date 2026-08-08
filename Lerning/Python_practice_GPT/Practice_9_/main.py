class student_info():
    def __init__(self,student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

def load_student(filename): # this whole function make me confuse at first
    students = []
    with open(filename, "r") as f: # f is the open file hun and filename is th diirection
        for line in f: #line read the information in f huh?
            line_id, line_name, line_score =  line.split(",")
            line_score = int(line_score)

            new_student = student_info(line_id, line_name, line_score) # create a object format function and then append to list error what?
            students.append(new_student)

        return students

def add_bonus(students, bonus):
    for s in students:
        new_score = s.score + bonus
        s.score = new_score #just the simpiest way but it take me so long to relize it or s.score += bonus

def save_students(output_filename, students):
    with open(output_filename, "w") as f:
        for s in students:
            f.write(f"{s.student_id},{s.name},{s.score}\n")
        
        


filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_9_\students.txt"
output_filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_9_\update_students.txt"

students = load_student(filename)
add_bonus(students, 5)
save_students(output_filename, students)

