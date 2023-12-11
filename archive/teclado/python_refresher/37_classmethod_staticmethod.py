class ClassTest:

    def instance_method(self):
        print(f"Called instance_method of {self}")

    def __str__(self):
        return "ClassTest object STR"

    def __repr__(self):
        return "ClassTest object REPR"

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(var):
        print(f"Called static method {var}")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method("hey")
print("---------------------")


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    # "Book" shows that you are returning same type we are currently in
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

    @staticmethod
    def small_book(name: str, weight: int) -> "Book":
        return Book(name, Book.TYPES[1], weight)


print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)
book_hardcover = Book.hardcover("Harry Potter", 1500)
print(book_hardcover)
book_paperback = Book.paperback("Python 101", 600)
print(book_paperback)
small_book = Book.small_book("Math", 50)
print(small_book)
