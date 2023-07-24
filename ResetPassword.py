import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import smtplib
from email.mime.text import MIMEText
import os


class ResetPasswordPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Reset Password')
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/another one.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        reset_password_title = tk.Label(self, text='Reset Password', font=self.custom_font, bg='white', fg='#0d2158')
        reset_password_title.place(y=140, x=70)

        password_reset_label = tk.Label(self, text='Enter Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        password_reset_label.place(y=355, x=150)

        self.password_reset_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.password_reset_entry.place(y=385, x=150)

        comfirm_password_reset_label = tk.Label(self, text='Comfirm Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        comfirm_password_reset_label.place(y=455, x=150)

        self.comfirm_password_reset_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.comfirm_password_reset_entry.place(y=485, x=150)

        self.reset_password_button = tk.Button(self,
                                               text="Reset Password",
                                               font=("typewriter", 20, "bold"),
                                               bd=0,
                                               bg='#0d2158',
                                               activebackground='#0d2158',
                                               cursor='hand2',
                                               fg="white",
                                               width=19,)
        self.reset_password_button.place(x=215, y=580)

        self.login_lable = Label(self, text="Now...", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.login_lable.place(x=325, y=680)

        self.login_button = Button(self, text='Log In', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0,)
        self.login_button.place(x=360, y=680)

if __name__ == "__main__":
    reset_password_page = ResetPasswordPage()
    reset_password_page.mainloop()
