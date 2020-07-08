
# Before type hinting, the usual way of writing functions is as follows:
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg((123,))


# Using Type Hinting it would be as follows:

from typing import List
def list_average(sequence: List) -> float:
    return sum(sequence) / len(sequence)

print(list_average([123]))


class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count

class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf contains {len(self.books)} books."
