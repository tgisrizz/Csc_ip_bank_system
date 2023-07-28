import tkinter as tk

ch = 0
root = tk.Tk()

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="sign in", variable=choice, value=1)
radio2 = tk.Radiobutton(root, text="sign up ", variable=choice, value=2)

radio1.pack()
radio2.pack()

def process_choice():

  ch = choice.get()
  if ch == 1:
        import existing_user
        root.destroy()
       
  elif ch == 2:
        import new_user
        root.destroy()
       
button = tk.Button(root, text="Enter", command=lambda: process_choice())
button.pack()

root.mainloop()
