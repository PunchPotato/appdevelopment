import tkinter as tk

class FoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food App")
        self.buttons = []  # List to store the created buttons
        self.current_y = 240
        
        self.frame = tk.Frame(root, bg='#b3b5ba')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.add_food_button = tk.Button(self.frame, text="Add Food", command=self.add_food)
        self.add_food_button.place(y=300, x=200)
    
    def add_food(self):
        name = "Food Name"  # Replace with the actual name of the food
        calories = 100  # Replace with the actual calorie content
        
        new_button = tk.Button(self.frame, text="", font=("typewriter", 20, "normal"), bg='#b3b5ba', bd=0,
                               command=lambda: self.controller.show_frame(FoodInfoPage))
        
        if self.buttons:
            self.current_y += 100
        new_button.place(y=self.current_y, x=200)
        new_button.config(text=f"{name}, {calories} cals".title())
        self.buttons.append(new_button)

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodApp(root)
    root.mainloop()