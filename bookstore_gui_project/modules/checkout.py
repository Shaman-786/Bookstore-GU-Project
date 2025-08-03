from tkinter import *
from tkinter import messagebox

def open_checkout_window():
    check = Toplevel()
    check.title("💳 Checkout")
    check.geometry("400x400")
    check.configure(bg="#d8f3dc")

    Label(check, text="Shipping Details", font=("Arial", 16, "bold"), bg="#d8f3dc").pack(pady=10)

    Entry(check, width=30).pack(pady=5)
    Entry(check, width=30).pack(pady=5)

    Button(check, text="Confirm Order", bg="#40916c", fg="white",
           command=lambda: messagebox.showinfo("Order", "Your order has been placed!")).pack(pady=20)
