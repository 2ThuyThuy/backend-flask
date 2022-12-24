class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f'Bookshelf with {self.books} book.'

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'

book = Book("Harry Potter", 120)

print(book)
    
  
     
    