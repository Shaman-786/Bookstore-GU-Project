# checkout.py
import tkinter as tk

def Checkout():
    win = tk.Toplevel()
    win.title("Checkout")
    win.geometry("300x200")
    tk.Label(win, text="Checkout Page", font=("Helvetica", 14)).pack(pady=20)
