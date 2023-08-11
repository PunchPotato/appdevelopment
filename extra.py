import tkinter as tk

def add_label():
    global current_y
    label_text = "Label {}".format(label_count)
    label = tk.Label(text_widget, text=label_text)
    text_widget.window_create("insert", window=label)
    
    # Update the vertical position for the next label
    current_y += 100

    # Scroll to show the newly added label
    text_widget.see("end")

    label_count += 1

root = tk.Tk()
root.title("Labels with Adjusted Position")

text_widget = tk.Text(root)
text_widget.pack()

add_button = tk.Button(root, text="Add Label", command=add_label)
add_button.pack()

current_y = 0  # Initial vertical position
label_count = 1  # Counter for labels

root.mainloop()
