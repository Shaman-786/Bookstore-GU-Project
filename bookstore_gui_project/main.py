# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from book_db import BookDB
from cart import Cart
from wishlist import Wishlist
from checkout import Checkout

db = BookDB()


class DuaaBookStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Duaa Book Store")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f3f3f3")

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="📚 Duaa Book Store", font=("Helvetica", 24, "bold"), bg="#4a7abc", fg="white",
                          pady=10)
        header.pack(fill=tk.X)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f3f3f3")
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="➕ Add Book", command=self.add_book_ui).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="👁️ View Books", command=self.view_books_ui).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="🛒 Cart", command=Cart).grid(row=0, column=2, padx=10)
        ttk.Button(btn_frame, text="❤️ Wishlist", command=Wishlist).grid(row=0, column=3, padx=10)
        ttk.Button(btn_frame, text="💳 Checkout", command=Checkout).grid(row=0, column=4, padx=10)

        self.status = tk.Label(self.root, text="", fg="green", bg="#f3f3f3")
        self.status.pack(pady=5)

    def add_book_ui(self):
        win = tk.Toplevel(self.root)
        win.title("Add New Book")
        win.geometry("400x300")

        tk.Label(win, text="Title").pack()
        title = tk.Entry(win)
        title.pack()

        tk.Label(win, text="Author").pack()
        author = tk.Entry(win)
        author.pack()

        tk.Label(win, text="Price").pack()
        price = tk.Entry(win)
        price.pack()

        def save():
            db.add_book(title.get(), author.get(), price.get())
            messagebox.showinfo("Success", "Book Added!")
            win.destroy()

        tk.Button(win, text="Save Book", command=save).pack(pady=10)

    def view_books_ui(self):
        win = tk.Toplevel(self.root)
        win.title("All Books")
        win.geometry("600x400")

        books = db.get_books()

        tree = ttk.Treeview(win, columns=("Title", "Author", "Price"), show="headings")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.heading("Price", text="Price")
        tree.pack(fill=tk.BOTH, expand=True)

        for book in books:
            tree.insert("", tk.END, values=(book['title'], book['author'], book['price']))


if __name__ == "__main__":
    root = tk.Tk()
    app = DuaaBookStoreApp(root)
    root.mainloop()
