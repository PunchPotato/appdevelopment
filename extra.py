
import tkinter as tk
  
root = tk.Tk()
root.geometry('250x150')
root.title("Button Border")
  
# Label
l = tk.Label(root, text = "Enter your Roll No. :",
             font = (("Times New Roman"), 15))
l.pack()
  
# Entry Widget
tk.Entry(root).pack()
  
# for space between widgets
tk.Label(root, text=" ").pack()
  
# Frame for button border with black border color
button_border = tk.Frame(root, highlightbackground = "black", 
                         highlightthickness = 2, bd=0)
bttn = tk.Button(button_border, text = 'Submit', fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
bttn.pack()
button_border.pack()
  
root.mainloop()