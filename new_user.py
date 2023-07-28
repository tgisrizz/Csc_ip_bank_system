import tkinter as tk 
import random as r

bank_id = 0
k = True

def new_login():
    id_value = id_entry.get()
    pwd_value = pwd_entry.get()
    pwd1_value = pwd1_entry.get()
    mail_value = mail_entry.get()
    bank_id = r.randint(10000,99999)
    if pwd_value == pwd1_value:
        flag = True
        pass
    else:
        flag = False
        pass

    dic = {"login_id" : bank_id, 'password' : pwd_value, 'mail' : mail_value,'Acc holder name' : id_value}

    if flag:
        with open ('bank login credentials file.txt',"ab+") as f:
            while k:
                for i in f:
                    if i[0] == bank_id:
                        bank_id = r.randint(10000,99999)
                        break
                    else:
                        f.write("\n".endcode())
                        f.write(str(dic).encode())

root2 = tk.Tk()
root2.title("Login Form")

id = tk.Label(root2, text="bank_id:")
id_entry = tk.Entry(root2)

pwd = tk.Label(root2, text="Password:")
pwd_entry = tk.Entry(root2, show="*")

pwd1 = tk.Label(root2, text="Password:")
pwd1_entry = tk.Entry(root2, show="*")

mail = tk.Label(root2, text="Recovery mail id:")
mail_entry = tk.Entry(root2)

login_button = tk.Button(root2, text="confirm", command=new_login)

id.grid(row=0, column=0)
id_entry.grid(row=0, column=1)

pwd.grid(row=1, column=0)
pwd_entry.grid(row=1, column=1)

pwd1.grid(row=2, column=0)
pwd1_entry.grid(row=2, column=1)

mail.grid(row=3, column=0)
mail_entry.grid(row=3, column=1)

login_button.grid(row=4, column=0, columnspan=5)

root2.mainloop()