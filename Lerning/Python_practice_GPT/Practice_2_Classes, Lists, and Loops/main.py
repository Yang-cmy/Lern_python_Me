# Classes, Lists, and Loops
class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

Student1 = student("Alice", [80, 90, 82])

def average_score():
    sum = 0
    average = 0
    for i in range(len(Student1.score)):
        sum += Student1.score[i]
        average = sum / len(Student1.score)
        print(Student1.score[i])

    print(Student1.name)
    print("Average :",average)
    print(len(Student1.score))
    print(sum)

average_score()


