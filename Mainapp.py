import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/Main app.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        main_title = tk.Label(self, text='Everything Fitness', font=self.custom_font, bg='#b3b5ba', fg='#000000')
        main_title.place(y=10, x=30)


        label = tk.Label(self, text="This is Page 1")
        label.pack(pady=200, padx=10)
        
        button = tk.Button(self, text="Go to Page 2", command=lambda: self.controller.show_frame(Page2))
        button.pack()

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/Main app.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        label = tk.Label(self, text="This is Page 2")
        label.pack(pady=200, padx=10)
        
        button = tk.Button(self, text="Go to Page 1", command=lambda: self.controller.show_frame(Page1))
        button.pack()

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry('720x980')
        
        self.frames = {}
        for F in (Page1, Page2):
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