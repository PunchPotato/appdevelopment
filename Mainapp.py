import tkinter as tk
from tkinter import Button, font
from PIL import ImageTk, Image
import requests
import os

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/Main app.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        self.title_image = ImageTk.PhotoImage(Image.open('Login page/potential logo.png'))
        main_title = tk.Label(self, image=self.title_image, font=self.custom_font, bg='#b3b5ba', fg='#000000')
        main_title.place(y=20, x=240)

        self.name_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="#000000", bd=0, bg='#b3b5ba')
        self.name_entry.insert(0, "Username")
        self.name_entry.place(y=350, x=220)

        self.newaccountButton = Button(self, text='Create New One', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='#b3b5ba', activeforeground='blue', activebackground='#b3b5ba',
                                       cursor='hand2', bd=0, command=self.API_connection)
        self.newaccountButton.place(x=380, y=750)
        
        self.calorie_button = ImageTk.PhotoImage(Image.open('Login page/cals button.png'))
        self.weight_button = ImageTk.PhotoImage(Image.open('Login page/weight button.png'))
        self.profile_button = ImageTk.PhotoImage(Image.open('Login page/profile button.png'))

        button = tk.Button(self, image=self.calorie_button, bd=5, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page1))
        button.place(y=860, x=20)

        button = tk.Button(self, image=self.weight_button,bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            command=lambda: self.controller.show_frame(Page2))
        button.place(y= 855, x = 290)

        button = tk.Button(self, image=self.profile_button, bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page3))
        button.place(y=855, x=580)

    def API_connection(self):
        self.query = self.name_entry.get().strip()
        self.api_key = os.environ.get('MY_API_KEY')
        print(self.api_key)
        self.api_url = f'https://api.api-ninjas.com/v1/nutrition?query={self.query}'
        self.headers = {'X-Api-Key': self.api_key}

        self.response = requests.get(self.api_url, headers=self.headers)

        if self.response.status_code == requests.codes.ok:
            print(self.response.text)
        else:
            print("Error:", self.response.status_code, self.response.text)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/Main app.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        self.title_image = ImageTk.PhotoImage(Image.open('Login page/potential logo.png'))
        main_title = tk.Label(self, image=self.title_image, font=self.custom_font, bg='#b3b5ba', fg='#000000')
        main_title.place(y=20, x=240)

        self.calorie_button = ImageTk.PhotoImage(Image.open('Login page/cals button.png'))
        self.weight_button = ImageTk.PhotoImage(Image.open('Login page/weight button.png'))
        self.profile_button = ImageTk.PhotoImage(Image.open('Login page/profile button.png'))

        button = tk.Button(self, image=self.calorie_button, bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page1))
        button.place(y=855, x=20)

        button = tk.Button(self, image=self.weight_button,bd=5, bg='#b3b5ba', activebackground='#b3b5ba',
                            command=lambda: self.controller.show_frame(Page2))
        button.place(y= 860, x = 290)

        button = tk.Button(self, image=self.profile_button, bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page3))
        button.place(y=855, x=580)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/Main app.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        self.title_image = ImageTk.PhotoImage(Image.open('Login page/potential logo.png'))
        main_title = tk.Label(self, image=self.title_image, font=self.custom_font, bg='#b3b5ba', fg='#000000')
        main_title.place(y=20, x=240)

        self.calorie_button = ImageTk.PhotoImage(Image.open('Login page/cals button.png'))
        self.weight_button = ImageTk.PhotoImage(Image.open('Login page/weight button.png'))
        self.profile_button = ImageTk.PhotoImage(Image.open('Login page/profile button.png'))

        button = tk.Button(self, image=self.calorie_button, bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page1))
        button.place(y=855, x=20)

        button = tk.Button(self, image=self.weight_button,bd=10, bg='#b3b5ba', activebackground='#b3b5ba',
                            command=lambda: self.controller.show_frame(Page2))
        button.place(y= 855, x = 290)

        button = tk.Button(self, image=self.profile_button, bd=5, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=lambda: self.controller.show_frame(Page3))
        button.place(y=860, x=580)



class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry('720x980')
        
        self.frames = {}
        for F in (Page1, Page2, Page3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Page1)
    
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()