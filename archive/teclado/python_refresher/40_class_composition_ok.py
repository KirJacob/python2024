from typing import List


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


shelf = BookShelf(Book("Harry Potter"), Book("Robinzon Cruzoe"), Book("Red Hat"))
print(shelf)


class BookShelfV2:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
