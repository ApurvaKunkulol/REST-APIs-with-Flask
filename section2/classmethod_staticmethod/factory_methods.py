class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, booktype, weight):
        self.name = name
        self.booktype = booktype
        self.weight = weight

    def __repr__(self):
        return f"<Title {self.name} of type {self.booktype} weighing {self.weight} grams.>"

    @classmethod
    def hardcover(cls, name, paperweight):
        return Book(name, Book.TYPES[0], paperweight + 100)

    @classmethod
    def paperback(cls, name, paperweight):
        return Book(name, Book.TYPES[1], paperweight)


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("SITA - The Princess of Mithila", 600)
print(book)
print("\n\n")
print(book2)
