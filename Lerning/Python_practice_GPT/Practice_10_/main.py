class Products():
    def __init__(self,id,name,quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

def load_inventory(filename):
    products = []
    with open(filename, "r") as f:
        for line in f:
            id, name, quantity = line.split(",")
            quantity = int(quantity)

            new_product = Products(id, name, quantity)
            products.append(new_product)

        return products



def sell_product(products, product_id, amount):
    for p in products:
        if p.id == product_id and p.quantity >= amount:
            p.quantity -= amount
        if p.id == product_id and p.quantity < amount:
            print("Not enough stock")


"""
# or you can do it like this it run the same as above
def sell_product(products, product_id, amount):
    for p in products:
        if p.id == product_id:
            if p.quantity >= amount:
                p.quantity -= amount
            else:
                print("Not enough stock")
"""

def save_inventory(update_filename, products):
    with open(update_filename, "w") as f:
        for p in products:
            f.write(f"{p.id},{p.name},{p.quantity}\n")


filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_10_\inventory.txt"

update_filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_10_\update_inventory.txt"

products = load_inventory(filename)

sell_product(products, "P001", 11)

save_inventory(update_filename, products)
            
