import tkinter as tk
window = tk.Tk()

ent_text = tk.Entry(width=40,bg="white",fg="black")
ent_text.insert(0,"What is your name?")

ent_text.pack()
window.mainloop()