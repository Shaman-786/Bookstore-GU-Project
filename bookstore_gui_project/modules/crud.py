from tkinter import *
from tkinter import messagebox

books = []

def open_crud_window():
    crud = Toplevel()
    crud.title("📘 Manage Books")
    crud.geometry("600x500")
    crud.configure(bg="#f8edeb")

    Label(crud, text="Add a New Book", font=("Arial", 16, "bold"), bg="#f8edeb").pack(pady=10)

    title_var = StringVar()
    author_var = StringVar()

    Entry(crud, textvariable=title_var, font=("Arial", 12)).pack(pady=5)
    Entry(crud, textvariable=author_var, font=("Arial", 12)).pack(pady=5)

    def add_book():
        title = title_var.get()
        author = author_var.get()
        if title and author:
            books.append(f"{title} by {author}")
            messagebox.showinfo("Success", "Book Added!")
        else:
            messagebox.showwarning("Error", "Fields cannot be empty")

    Button(crud, text="Add Book", command=add_book, bg="#6a994e", fg="white", font=("Arial", 12)).pack(pady=10)
