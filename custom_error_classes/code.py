class Book:
    def __init__(self, name: str, page_count:int) -> None:
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return (
            f"<Book {self.name}, read {self.pages_read} out of {self.page_count} pages.>"
        )

    def read(self, pages: int) -> None:
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"You tried to read {self.pages_read + pages} " +
            f"pages while the book contains only {self.page_count}")
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

class TooManyPagesReadError(ValueError):
    pass


python101 = Book("Python 101", 500)
try:
    python101.read(40)
    python101.read(35)
    python101.read(475)
except  TooManyPagesReadError as many_page_error:
    print(f"ERROR: {many_page_error}")
