import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Packing labels vertically, expanding to fill both directions
label1.pack(fill="both", expand=True, padx=10, pady=5)
label2.pack(fill="both", expand=True, padx=10, pady=5)
label3.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()