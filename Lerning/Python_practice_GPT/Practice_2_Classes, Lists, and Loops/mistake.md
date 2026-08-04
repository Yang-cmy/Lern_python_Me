# Mistake of this code 

This is invalid because :

class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

Student1 = student("Alice", [80, 90, 82])

```python
class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

Student1 = student("Alice", [80, 90, 82])

def average_score():
    for i in range(len(Student1.score)):
        sum = 0 # Create the variable inside loop making it resetting to 0 in every loop pass
        average = 0 # Create the variable inside loop making it resetting to 0 in every loop pass
        sum += Student1.score[i]
        average = sum / len(Student1.score)
        print(Student1.score[i])

    print(Student1.name)
    print("Average :",average)
    print(len(Student1.score))
    print(sum)

average_score()
```

# This is the fixed version

Create variable outside loop instant so it will not reseting as loop pass

```python
class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

Student1 = student("Alice", [80, 90, 82])

def average_score():
    sum = 0 #
    average = 0 # outside the loop
    for i in range(len(Student1.score)):
        sum += Student1.score[i]
        average = sum / len(Student1.score)
        print(Student1.score[i])

    print(Student1.name)
    print("Average :",average)
    print(len(Student1.score))
    print(sum)

average_score()
```
---

# Other solution is using sum function

instand of calculating each score inside object using Sum is easier

```python
total = sum(Student1.score) # Using sum function
    average = total / len(Student1.score)

    for score in Student1.score:
        print(score)
```