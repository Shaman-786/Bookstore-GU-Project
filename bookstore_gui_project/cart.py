# cart.py
import tkinter as tk

def Cart():
    win = tk.Toplevel()
    win.title("Your Cart")
    win.geometry("300x200")
    tk.Label(win, text="Cart Items", font=("Helvetica", 14)).pack(pady=20)
