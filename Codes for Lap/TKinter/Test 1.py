import tkinter as tk
window = tk.Tk()
greetings = tk.Label(text="Python rocks!")
entry = tk.Entry()
output = tk.Entry()
name = entry.get()
entry.insert(0,"Python")
entry.delete(0)
output.insert(0,"coconut")

greetings.pack()
entry.pack()
output.pack()
window.mainloop()