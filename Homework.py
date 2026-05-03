import tkinter as tk
from tkinter import messagebox
from datetime import datetime
def calculate_age():
    try:
        name = name_entry.get().strip()
        birth_date_str = birth_entry.get().strip()

        if not name:
            messagebox.showerror("Input Error", "Please enter your name.")
            return

        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()

        if birth_date > today:
            messagebox.showerror("Input Error", "Birth date cannot be in the future.")
            return

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            prev_month = (today.month - 1) if today.month > 1 else 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days += (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days

        if months < 0:
            years -= 1
            months += 12

        result_label.config(
            text=f"Hello {name}, you are {years} years, {months} months, and {days} days old."
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter date in YYYY-MM-DD format.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Enter your birth date (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)
birth_entry = tk.Entry(root, font=("Arial", 12))
birth_entry.pack(pady=5)

tk.Button(root, text="Calculate Age", font=("Arial", 12), command=calculate_age).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=350)
result_label.pack(pady=10)

root.mainloop()
