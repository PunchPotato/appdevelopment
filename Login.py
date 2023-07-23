import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import os


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Login Page')
        self.custom_font = font.Font(family="typewriter", size=70, weight="normal")
        self.open_eye = None
        self.close_eye = None
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/another one.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        login_title = tk.Label(self, text='USER LOGIN', font=self.custom_font, bg='white', fg='#0d2158')
        login_title.place(y=100, x=70)

        self.name_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="grey", bd=0)
        self.name_entry.insert(0, "Username")
        self.name_entry.place(y=350, x=220)
        self.name_entry.bind("<FocusIn>", self.temp_name_entry_text)

        self.password_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="grey", bd=0)
        self.password_entry.insert(0, "Password")
        self.password_entry.place(y=450, x=220)
        self.password_entry.bind("<FocusIn>", self.temp_password_entry_text)

        self.open_eye = ImageTk.PhotoImage(Image.open('Login page/openeye.png'))
        self.close_eye = ImageTk.PhotoImage(Image.open('Login page/closeeye.png'))
        self.eye_button = Button(self, image=self.open_eye, bd=0, bg='white', activebackground='white', cursor='hand2',
                                 command=self.hide)
        self.eye_button.place(y=450, x=500)

        self.forget_button = Button(self, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                                    cursor='hand2', font=("typewriter", 9, "bold"), fg='firebrick1',
                                    activeforeground='firebrick1', command=self.forgot_password)
        self.forget_button.place(x=410, y=495)

        tk.Frame(self, width=300, height=2, bg="#0d2158").place(y=390, x=220)
        tk.Frame(self, width=300, height=2, bg="#0d2158").place(y=490, x=220)

        login_button = tk.Button(self, text="Log in", font=("typewriter", 20, "bold"), bd=0, bg='#0d2158',
                                 activebackground='#0d2158', cursor='hand2', fg="white", width=19,
                                 command=self.connect_database)
        login_button.place(y=550, x=210)

        or_label = Label(self, text='----------------------------OR----------------------------',
                         font=("typewriter", 20), fg='#0d2158', bg='white')
        or_label.place(x=100, y=620)

        self.facebook_logo = PhotoImage(file='Login page/facebook.png')
        self.fbLabel = Label(self, image=self.facebook_logo, bg='white')
        self.fbLabel.place(x=360, y=670)

        self.google_logo = PhotoImage(file='Login page/google.png')
        self.googleLabel = Label(self, image=self.google_logo, bg='white')
        self.googleLabel.place(x=440, y=670)

        self.twitter_logo = PhotoImage(file='Login page/twitter.png')
        self.twitterLabel = Label(self, image=self.twitter_logo, bg='white')
        self.twitterLabel.place(x=280, y=670)

        self.signupLabel = Label(self, text="Don't have an account?", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.signupLabel.place(x=250, y=750)

        self.newaccountButton = Button(self, text='Create New One', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0, command=self.signup_page)
        self.newaccountButton.place(x=380, y=750)

    def temp_name_entry_text(self, event):
        if self.name_entry.get() == 'Username':
            self.name_entry.delete(0, "end")

    def temp_password_entry_text(self, event):
        if self.password_entry.get() == 'Password':
            self.password_entry.delete(0, "end")

    def hide(self):
        self.password_entry.config(show='*')
        self.eye_button.config(image=self.close_eye, command=self.show)

    def show(self):
        self.password_entry.config(show='')
        self.eye_button.config(image=self.open_eye, command=self.hide)

    def signup_page(self):
        self.destroy()
        import Signup
        Signup.SignupPage().mainloop()

    def forgot_password(self):
        self.destroy()
        import ForgotPassword
        ForgotPassword.ForgotPasswordPage().mainloop()

    def connect_database(self):
        if self.name_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror("Error", "All fields must be filled.")
        elif self.name_entry.get() == 'Username' or self.password_entry.get() == 'Password':
            messagebox.showerror("Error", "All fields must be filled.")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password=os.environ.get('MYSQL_PASSWORD'))
                my_curser = con.cursor()
            except:
                messagebox.showerror("Error", "Failed to connect to database")
                return
            query = 'use mydatabase'
            my_curser.execute(query)
            query = 'select * from user_data where username =%s and password =%s'
            my_curser.execute(query, (self.name_entry.get(), self.password_entry.get()))
            row = my_curser.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username or password.")
            else:
                messagebox.showinfo("Success", "Login is successful.")


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
