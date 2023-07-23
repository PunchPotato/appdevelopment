import tkinter as tk

def button_clicked(event):
    print("Button clicked!")

# Create the main window
window = tk.Tk()

# Create a button
button = tk.Button(window, text="Click Me")
button.pack()

# Bind the button to a function
button.bind("<Button-1>", button_clicked)

# Run the main window's event loop
window.mainloop()