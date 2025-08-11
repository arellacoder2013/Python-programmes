import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    length = len(password)

    if length < 5:
        result = "Weak"
    elif 5 <= length <= 8:
        result = "Medium"
    elif 9 <= length <= 12:
        result = "Strong"
    else:
        result = "Very Strong"

    result_label.config(text=f"Password Strength: {result}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")



label = tk.Label(root, text="Enter your password:",bg="lightblue")
label.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength,bg="lightpink")
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()