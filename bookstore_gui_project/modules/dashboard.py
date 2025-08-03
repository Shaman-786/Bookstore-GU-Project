from tkinter import *
from modules.crud import open_crud_window
from modules.cart import open_cart_window
from modules.wishlist import open_wishlist_window
from modules.checkout import open_checkout_window

def open_dashboard(root):
    root.destroy()
    dash = Tk()
    dash.title("📚 Bookstore Dashboard")
    dash.geometry("900x600")
    dash.configure(bg="#edf6f9")

    Label(dash, text="📘 Bookstore Dashboard", font=("Arial", 24, "bold"), bg="#edf6f9", fg="#1d3557").pack(pady=30)

    Button(dash, text="📚 Manage Books", command=open_crud_window, font=("Arial", 14), bg="#457b9d", fg="white",
           width=20, pady=10).pack(pady=10)

    Button(dash, text="🛒 View Cart", command=open_cart_window, font=("Arial", 14), bg="#1d3557", fg="white",
           width=20, pady=10).pack(pady=10)

    Button(dash, text="💖 Wishlist", command=open_wishlist_window, font=("Arial", 14), bg="#e63946", fg="white",
           width=20, pady=10).pack(pady=10)

    Button(dash, text="💳 Checkout", command=open_checkout_window, font=("Arial", 14), bg="#2a9d8f", fg="white",
           width=20, pady=10).pack(pady=10)

    dash.mainloop()
