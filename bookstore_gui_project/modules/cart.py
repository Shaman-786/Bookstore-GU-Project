from tkinter import *
from tkinter import messagebox

cart_items = []

def open_cart_window():
    cart = Toplevel()
    cart.title("🛒 Your Cart")
    cart.geometry("400x400")
    cart.configure(bg="#e9ecef")

    Label(cart, text="Items in Cart", font=("Arial", 16, "bold"), bg="#e9ecef").pack(pady=10)

    for item in cart_items:
        Label(cart, text=item, bg="#e9ecef").pack()
