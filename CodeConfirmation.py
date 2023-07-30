import os
import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email.mime.text import MIMEText
import pymysql
from ForgotPassword import ForgotPasswordPage

class CodeConfirmationPage(tk.Tk):
    def __init__(self, email):
        super().__init__()
        self.geometry('720x980')
        self.title('Reset Password')
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")
        self.email = email
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/another one.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        reset_password_title = tk.Label(self, text='Reset Password', font=self.custom_font, bg='#b3b5ba', fg='#000000')
        reset_password_title.place(y=140, x=70)

        enter_code_label = tk.Label(self, text='Enter Confirmation Code:', font=("typewriter", 15, "normal"), bg='#b3b5ba', fg='#000000')
        enter_code_label.place(y=305, x=150)

        self.enter_code_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#000000', width=30)
        self.enter_code_entry.place(y=335, x=150)

        password_reset_label = tk.Label(self, text='Enter Password:', font=("typewriter", 15, "normal"), bg='#b3b5ba', fg='#000000')
        password_reset_label.place(y=405, x=150)

        self.password_reset_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#000000', width=30)
        self.password_reset_entry.place(y=435, x=150)

        comfirm_password_reset_label = tk.Label(self, text='Comfirm Password:', font=("typewriter", 15, "normal"), bg='#b3b5ba', fg='#000000')
        comfirm_password_reset_label.place(y=505, x=150)

        self.comfirm_password_reset_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#000000', width=30)
        self.comfirm_password_reset_entry.place(y=535, x=150)


        self.reset_password_button = tk.Button(self,
                                               text="Reset Password",
                                               font=("typewriter", 20, "bold"),
                                               bd=0,
                                               bg='#000000',
                                               activebackground='#000000',
                                               cursor='hand2',
                                               fg="white",
                                               width=19,
                                               command=self.verify_code)
        self.reset_password_button.place(x=215, y=630)

        self.login_label = Label(self, text="Or...", font=('Open Sans', 9), fg='#b50d3d',
                                 bg='#b3b5ba')
        self.login_label.place(x=325, y=730)

        self.login_button = Button(self, text='Go back', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='#b3b5ba', activeforeground='blue', activebackground='#000000',
                                       cursor='hand2', bd=0,)
        self.login_button.place(x=360, y=730)
    
    def login_page(self):
        self.destroy()
        import Login
        Login.LoginPage().mainloop()
    
    def verify_code(self):
        entered_code = self.enter_code_entry.get().strip()
        print("Entered code:", entered_code)

        if entered_code == '' or self.password_reset_entry.get() == '' or self.comfirm_password_reset_entry.get() == '':
            messagebox.showerror("Error", "All fields must be filled.")
            return
        elif self.password_reset_entry.get() != self.comfirm_password_reset_entry.get():
            messagebox.showerror("Error", "Password must match.")
            return
        elif len(self.password_reset_entry.get()) < 5 or not any(char.isupper() for char in self.password_reset_entry.get()) or len(self.comfirm_password_reset_entry.get()) < 5 or not any(char.isupper() for char in self.comfirm_password_reset_entry.get()):
            messagebox.showerror("Error", "Password needs to be longer than 5 characters and include a capital letter.")
            return

        
        try:
            con = pymysql.connect(host='localhost', user='root', password=os.environ.get('MYSQL_PASSWORD'),
                                database='mydatabase')
            with con:
                my_cursor = con.cursor()

                query = "SELECT email FROM user_data WHERE email = %s AND one_time_codes = %s"
                my_cursor.execute(query, (self.email, entered_code))
                row = my_cursor.fetchone()

                if row:
                    query = "UPDATE user_data SET password = %s WHERE email = %s"
                    my_cursor.execute(query, (self.password_reset_entry.get(), self.email))
                    con.commit()  # Commit the changes to the database

                    messagebox.showinfo("Success", "Password reset successful.")
                    self.login_page()
                else:
                    messagebox.showerror('Error', 'Invalid code or email. Please try again.')

        except pymysql.Error as e:
            messagebox.showerror("Error", "Failed to connect to the database: " + str(e))
            print(f"Database error: {e}")

        except Exception as e:
            messagebox.showerror("Error", "An error occurred. Please try again.")
            print(f"Error: {e}")

        finally:
            try:
                if my_cursor:
                    my_cursor.close()
                if con:
                    con.close()
            except pymysql.Error:
                pass

if __name__ == "__main__":
    app = ForgotPasswordPage()
    app.mainloop()

    # After the ForgotPasswordPage is closed, the user enters the email.
    email = app.email  # Get the email entered by the user from the ForgotPasswordPage

    if email:
        code_confirmation_page = CodeConfirmationPage(email=email)
        code_confirmation_page.mainloop()