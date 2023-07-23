import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import re
import os


class SignupPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Sign Up')
        self.custom_font = font.Font(family="typewriter", size=45, weight="normal")
        self.open_eye = None
        self.close_eye = None
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/another one.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        create_account_title = tk.Label(self, text='CREATE AN ACCOUNT', font=self.custom_font, bg='white', fg='#0d2158')
        create_account_title.place(y=100, x=30)

        email_title = tk.Label(self, text='Email:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        email_title.place(y=255, x=150)

        self.email_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.email_entry.place(y=285, x=150)

        username_title = tk.Label(self, text='Username:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        username_title.place(y=370, x=150)

        self.username_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.username_entry.place(y=400, x=150)

        password_title = tk.Label(self, text='Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        password_title.place(y=495, x=150)

        self.password_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.password_entry.place(y=525, x=150)

        confirm_password_title = tk.Label(self, text='Comfirm Password:', font=("typewriter", 15, "normal"), bg='white',
                                          fg='#0d2158')
        confirm_password_title.place(y=610, x=150)

        self.password_comfirm_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158',
                                               width=30)
        self.password_comfirm_entry.place(y=640, x=150)

        create_account_button = tk.Button(self, text="Create Account", font=("typewriter", 20, "bold"), bd=0,
                                          bg='#0d2158', activebackground='#0d2158', cursor='hand2', fg="white",
                                          width=19, command=self.connect_database)
        create_account_button.place(y=720, x=210)

        self.terms_and_conditions_label= Label(self, text="I agree to Terms & Conditions", font=('Open Sans', 12),
                                               fg='firebrick1', bg='white')
        self.terms_and_conditions_label.place(x=270, y=685)

        self.check = IntVar()
        terms_and_conditions_box = tk.Checkbutton(self, bd=0, bg='white', variable=self.check)
        terms_and_conditions_box.place(x=245, y=685)

        self.signupLabel = Label(self, text="Or...", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.signupLabel.place(x=335, y=780)

        self.newaccountButton = Button(self, text='Log In', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0, command=self.login_page)
        self.newaccountButton.place(x=360, y=780)

    def clear(self):
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.password_comfirm_entry.delete(0, END)
        self.check.set(0)

    def login_page(self):
        self.destroy()
        import Login
        Login.LoginPage().mainloop()

    def create_account(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password=os.environ.get('MYSQL_PASSWORD'))
            my_cursor = con.cursor()
            query = 'create database if not exists mydatabase'
            my_cursor.execute(query)
            query = 'use mydatabase'
            my_cursor.execute(query)
            query = 'create table if not exists user_data(id int auto_increment primary key not null, ' \
                    'email varchar(50), username varchar(100), password varchar(20))'
            my_cursor.execute(query)
            con.commit()

            query = 'SELECT * FROM user_data WHERE username = %s OR email = %s'
            my_cursor.execute(query, (self.username_entry.get(), self.email_entry.get()))

            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Username or email already exists.")
            else:
                query = 'insert into user_data (email, username, password) values(%s, %s, %s)'
                my_cursor.execute(query, (self.email_entry.get(), self.username_entry.get(), self.password_entry.get()))

                con.commit()
                con.close()

                messagebox.showinfo("Success", "Account created successfully!")
                self.clear()
                self.destroy()
                import Login
                Login.LoginPage().mainloop()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to connect to the database. Error: {str(e)}")
            return

    def connect_database(self):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if self.email_entry.get() == '' or self.username_entry.get() == '' or self.password_entry.get() == '' or\
                self.password_comfirm_entry.get() == '':
            messagebox.showerror("Error", "All fields must be filled.")
        elif re.match(email_pattern, self.email_entry.get()):
            pass
        else:
            messagebox.showerror("Error", "Email not valid.")
        if self.password_comfirm_entry.get() != self.password_entry.get():
            messagebox.showerror("Error", "Passwords do not match.")
        elif self.check.get() == 0:
            messagebox.showerror("Error", "Accept Terms & Conditions.")
        elif len(self.password_entry.get()) > 5 and any(char.isupper() for char in self.password_entry.get()):
            self.create_account()
        else:
            messagebox.showerror("Error", "Password needs to be longer than 5 characters and include a capital letter.")


if __name__ == "__main__":
    Sign_up_page = SignupPage()
    Sign_up_page.mainloop()
