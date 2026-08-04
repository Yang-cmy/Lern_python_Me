"""
def find_average():
    number = []
    average = 0
    Total_Data = int(input("Total Data Enter"))

    for i in range(Total_Data):
        try:
            User_Choice = int(input("Enter Data:"))
            number.append(User_Choice)
            average += number[i]
        except ValueError:
            print("Please enter a valid number!")

    print("",average/Total_Data)
        

find_average()
"""

def find_average(number):
    Data = []
    total = 0

    for i in range(number):
        try:
            User_Choice = int(input(f"Enter Data{i + 1}:"))
            Data.append(User_Choice)
            total += Data[i]
        except ValueError:
            print("Please enter a valid Data!")

    average = total/number
    print("Data:", Data)
    print("Average:", average)
        

find_average(5)