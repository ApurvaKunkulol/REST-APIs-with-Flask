class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"A bookshelf with {len(self.books)} books."


class Book:
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."

book1 = Book("Harry Potter")
book2 = Book("Unfinished Innings")
book3 = Book("VP Menon, the unsung Architect of Modern India")

bookshelf = BookShelf(book1, book2, book3)
print(bookshelf)
