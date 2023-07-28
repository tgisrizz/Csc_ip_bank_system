import tkinter as tk
from tkinter import messagebox

flag = None

def login():
    bank_id = bank_id_entry.get()
    password = password_entry.get()

    if bank_id == "123456789" and password == "password":
        messagebox.showinfo(title="Login Successful", message="You have successfully logged in.")
        flag = True
       
    else:
        messagebox.showerror(title="Login Failed", message="Invalid id or password.")

root1 = tk.Tk()
root1.title("Login Form")

bank_id_label = tk.Label(root1, text="bank_id:")
bank_id_entry = tk.Entry(root1)

password_label = tk.Label(root1, text="Password:")
password_entry = tk.Entry(root1, show="*")

login_button = tk.Button(root1, text="Login", command=login)

bank_id_label.grid(row=0, column=0)
bank_id_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2)

root1.mainloop()