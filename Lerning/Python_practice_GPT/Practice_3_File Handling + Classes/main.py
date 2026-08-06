
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author


def save_book(books):
    with open(r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_3_File Handling + Classes\books.txt", "w") as file:
        for book in books:
            file.write(f"{book.title},{book.author}\n")

book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
with open(r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_3_File Handling + Classes\books.txt") as file:
    print(file.read())

books = [book1, book2]

save_book(books)
            