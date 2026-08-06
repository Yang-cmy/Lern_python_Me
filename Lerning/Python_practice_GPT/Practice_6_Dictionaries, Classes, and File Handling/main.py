class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

def create_inventory():
    inventory = { #yeah this is how you create Dicionary with Class
        "Pen" : Product("Pen", 10.0),
        "Notebook" : Product("Notebook", 30.0),
        "Pencil" : Product("Pencil", 5.0)
    }
    return inventory #teturn the dictionary

def save_inventory(inventory, filename):
    with open(filename, "w") as file:
        for key, product in inventory.items():
            file.write(f"{product.name},{product.price}\n")

    with open(filename) as file:
        for line in file:
            print(line, end="")

filename = (r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_6_Dictionaries, Classes, and File Handling\product.txt")

inventory = create_inventory()
save_inventory(inventory, filename)