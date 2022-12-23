class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name} ,{self.book_type}, weigning {self.weight}g>"

    # @classmethod
    # def hardcover(cls, name, page_weight):
    #     return Book(name, Book.TYPE[0], page_weight + 100)
    @classmethod
    def hardcover(cls, name, page_weight): # cls same class
        return cls(name, cls.TYPE[0], page_weight + 100)

# book = Book("Harry Porter", "hardcover", 1500)
# print(book.name)
# print(book)

book2 = Book.hardcover("Harry Potter", 1500)
print(book2)