# wishlist.py
import tkinter as tk

def Wishlist():
    win = tk.Toplevel()
    win.title("Your Wishlist")
    win.geometry("300x200")
    tk.Label(win, text="Wishlist Items", font=("Helvetica", 14)).pack(pady=20)
