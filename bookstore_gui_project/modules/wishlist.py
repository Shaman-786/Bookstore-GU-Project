from tkinter import *

wishlist_items = []

def open_wishlist_window():
    wish = Toplevel()
    wish.title("💖 Wishlist")
    wish.geometry("400x400")
    wish.configure(bg="#fff0f3")

    Label(wish, text="Your Wishlist", font=("Arial", 16, "bold"), bg="#fff0f3").pack(pady=10)

    for item in wishlist_items:
        Label(wish, text=item, bg="#fff0f3").pack()
