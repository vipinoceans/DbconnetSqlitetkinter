import sqlite3
from tkinter import *
from tkinter import messagebox as ms

with sqlite3.connect("quit.db") as db:
    cursur = db.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
cursur.execute("SELECT * from user")
db.commit()

db.close()

class main:
    def __init__(self,master):
    	# Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()
        
    def login(self):
        with sqlite3.connect("quit.db") as db:
            cursur = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursur.execute(find_user,[(self.username.get(),(self.password.get()))])
        results = cursur.fetchall()
        if results:
            self.log.pack_forget()
            self.head["text"] = self.username.get()
            self.head['pady']=150
        else:
            ms.showerror("Oops!username not matching")
    def new_user(self):
        with sqlite3.connect("quit.db") as db:
            cursur = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursur.execute(find_user,[(self.username.get()),(self.password.get())])
        if cursur.fetchall():
            ms.showerror("oops! User name taken")
        else:
            ms.showinfo("`success, account created")

            self.log()
            # Create New Account
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            cursur.execute(insert, [(self.n_username.get()), (self.n_password.get())])
            db.commit()
        
    def log(self):
        self.username.set("")
        self .password.set("")
        self.logf.pack_forget()
        self.head['text'] = "create Account"
        self.crf.pack()
        
    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.cr.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)
        
root = Tk()
main(root)
root.geometry("400x350+350+150")
root.mainloop()
