import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollable Page")
root.geometry("400x300")

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", configure_canvas)

for i in range(30):
    tk.Label(frame, text=f"Element {i}").pack(pady=5)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()