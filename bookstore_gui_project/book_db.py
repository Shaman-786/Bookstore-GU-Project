# book_db.py
import json
import os

class BookDB:
    def __init__(self):
        self.file = "books.json"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def add_book(self, title, author, price):
        books = self.get_books()
        books.append({"title": title, "author": author, "price": price})
        with open(self.file, "w") as f:
            json.dump(books, f)

    def get_books(self):
        with open(self.file, "r") as f:
            return json.load(f)
