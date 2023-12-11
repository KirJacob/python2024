class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."


shelf = BookShelf(300)

print(shelf)


class Book(BookShelf):
    def __init__(self, name: str, quantity: int):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book <{self.name}>"


book = Book("Harry Potter", 120)
print(book)
