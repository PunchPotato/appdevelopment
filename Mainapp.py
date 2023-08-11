import tkinter as tk
from tkinter import Button, Label, font
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import os
import json

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")
        
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.bg_image_top = ImageTk.PhotoImage(Image.open("Login page/top background.png"))
        self.bg_label_top = tk.Label(self, image=self.bg_image_top, bd=0, highlightthickness=0)
        self.bg_label_top.image = self.bg_image_top
        self.bg_label_top.place(y=0, x=195)

        self.bg_image_bottom = ImageTk.PhotoImage(Image.open("Login page/bottom background.png"))
        self.bg_label_bottom = tk.Label(self, image=self.bg_image_bottom, bd=0, highlightthickness=0)
        self.bg_label_bottom.image = self.bg_image_bottom
        self.bg_label_bottom.place(y=835, x=0)
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        frame.bind("<Configure>", configure_canvas)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        
        self.title_image = ImageTk.PhotoImage(Image.open('Login page/potential logo.png'))
        main_title = tk.Label(self, image=self.title_image, bg='#b3b5ba', fg='#000000')
        main_title.place(y=20, x=240)
        
        self.box_image = ImageTk.PhotoImage(Image.open("Login page/box.png"))
        self.box = tk.Label(frame, image=self.box_image, fg='#000000')
        self.box.pack(pady=200, padx=60)

        self.addfood_button = tk.Button(frame, text='Add Food', font=font.Font(family="typewriter", size=20, weight="normal"),
                                         command=lambda: self.controller.show_frame(Page1AddFood))
        self.addfood_button.place(y=300, x=100)

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

        self.selected_food_label = tk.Label(frame, text="", font=("typewriter", 20, "normal"), bg='#b3b5ba')
        self.selected_food_label.place(y=220, x=150)

    def update_food(self, name, calories):
        self.selected_food_label.config(text=f"{name}, {calories}cals".title())
        label += 1
    

class Page1AddFood(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.bg_image_top = ImageTk.PhotoImage(Image.open("Login page/top background.png"))
        self.bg_label_top = tk.Label(self, image=self.bg_image_top, bd=0, highlightthickness=0)
        self.bg_label_top.image = self.bg_image_top
        self.bg_label_top.place(y=0, x=195)

        self.bg_image_bottom = ImageTk.PhotoImage(Image.open("Login page/bottom background.png"))
        self.bg_label_bottom = tk.Label(self, image=self.bg_image_bottom, bd=0, highlightthickness=0)
        self.bg_label_bottom.image = self.bg_image_bottom
        self.bg_label_bottom.place(y=835, x=0)
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        frame.bind("<Configure>", configure_canvas)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)


        self.title_image = ImageTk.PhotoImage(Image.open('Login page/potential logo.png'))
        main_title = tk.Label(self, image=self.title_image, font=self.custom_font, bg='#b3b5ba', fg='#000000')
        main_title.place(y=20, x=240)

        self.food_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="#000000", bd=0, bg='#b3b5ba')
        self.food_entry.insert(0, "Search Food Here!")
        self.food_entry.place(y=250, x=220)
        self.food_entry.bind("<FocusIn>", self.temp_food_entry_text)

        self.search_icon = ImageTk.PhotoImage(Image.open('Login page/search icon.png'))
        self.searchiconbutton = Button(self, image = self.search_icon, bg='#b3b5ba',activebackground='#b3b5ba',
                                       cursor='hand2', bd=0, command=self.API_connection)
        self.searchiconbutton.place(x=500, y=255)

        self.add_food_button = ImageTk.PhotoImage(Image.open('Login page/add food button.png'))

        add_food_button = tk.Button(self, image=self.add_food_button, bd=5, bg='#b3b5ba', activebackground='#b3b5ba',
                            cursor='hand2', command=self.add_food)
        add_food_button.place(y=750, x=290)
        
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

    def add_food(self):
        page1_instance = self.controller.frames[Page1]
        page1_instance.update_food(self.name, self.calories)

    def temp_food_entry_text(self, event):
        if  self.food_entry.get() == 'Search Food Here!':
            self.food_entry.delete(0, "end")
    
    def API_connection(self,):    
        self.query = self.food_entry.get().strip()
        self.api_key = self.api_key = os.environ.get('MY_API_KEY')
        self.api_url = f'https://api.api-ninjas.com/v1/nutrition?query={self.query}'
        self.headers = {'X-Api-Key': self.api_key}

        self.response = requests.get(self.api_url, headers=self.headers)

        self.json_data = self.response.text
        self.data = json.loads(self.json_data)
        self.name = self.data[0]["name"]
        self.calories = self.data[0]["calories"]
        self.serving_size_g = self.data[0]["serving_size_g"]
        self.fat_total_g = self.data[0]["fat_total_g"]
        self.fat_saturated_g = self.data[0]["fat_saturated_g"]
        self.protein_g = self.data[0]["protein_g"]
        self.sodium_mg = self.data[0]["sodium_mg"]
        self.potassium_mg = self.data[0]["potassium_mg"]
        self.cholesterol_mg = self.data[0]["cholesterol_mg"]
        self.carbohydrates_total_g = self.data[0]["carbohydrates_total_g"]
        self.fiber_g = self.data[0]["fiber_g"]
        self.sugar_g = self.data[0]["sugar_g"]
        
        if self.response.status_code == requests.codes.ok:
            self.label = Label(
            self.master,
            bg='#b3b5ba',
            font=("typewriter", 20, "normal"),
            text=f"Name: {self.name}\n"
                 f"Calories: {self.calories}\n"
                 f"Serving Size (g): {self.serving_size_g}\n"
                 f"Total Fat (g): {self.fat_total_g}\n"
                 f"Saturated Fat (g): {self.fat_saturated_g}\n"
                 f"Protein (g): {self.protein_g}\n"
                 f"Sodium (mg): {self.sodium_mg}\n"
                 f"Potassium (mg): {self.potassium_mg}\n"
                 f"Cholesterol (mg): {self.cholesterol_mg}\n"
                 f"Total Carbohydrates (g): {self.carbohydrates_total_g}\n"
                 f"Fiber (g): {self.fiber_g}\n"
                 f"Sugar (g): {self.sugar_g}"
        )
            self.label.place(y=350, x=200)
        else:
            print("Error:", self.response.status_code, self.response.text)
            self.label = Label(self, text=str("Error:", self.response.status_code, self.response.text))
            self.label.place(y=600, x= 200)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.bg_image_top = ImageTk.PhotoImage(Image.open("Login page/top background.png"))
        self.bg_label_top = tk.Label(self, image=self.bg_image_top, bd=0, highlightthickness=0)
        self.bg_label_top.image = self.bg_image_top
        self.bg_label_top.place(y=0, x=195)

        self.bg_image_bottom = ImageTk.PhotoImage(Image.open("Login page/bottom background.png"))
        self.bg_label_bottom = tk.Label(self, image=self.bg_image_bottom, bd=0, highlightthickness=0)
        self.bg_label_bottom.image = self.bg_image_bottom
        self.bg_label_bottom.place(y=835, x=0)
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        frame.bind("<Configure>", configure_canvas)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)


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

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.bg_image_top = ImageTk.PhotoImage(Image.open("Login page/top background.png"))
        self.bg_label_top = tk.Label(self, image=self.bg_image_top, bd=0, highlightthickness=0)
        self.bg_label_top.image = self.bg_image_top
        self.bg_label_top.place(y=0, x=195)

        self.bg_image_bottom = ImageTk.PhotoImage(Image.open("Login page/bottom background.png"))
        self.bg_label_bottom = tk.Label(self, image=self.bg_image_bottom, bd=0, highlightthickness=0)
        self.bg_label_bottom.image = self.bg_image_bottom
        self.bg_label_bottom.place(y=835, x=0)
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        frame.bind("<Configure>", configure_canvas)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)


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
        for F in (Page1,Page1AddFood, Page2, Page3):
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
