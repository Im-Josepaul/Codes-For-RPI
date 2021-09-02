import tkinter as tk
from tkinter.constants import BOTTOM, LEFT
window = tk.Tk()

frm_1 = tk.Frame(master=window, borderwidth=50)
text = tk.Label(master=frm_1 ,text = "Enter text here.")
text_box = tk.Text(master=frm_1, width=20,height=5)
value_1 = "Hello"
frm_2 = tk.Frame(master=window, borderwidth=50)
text_2 = tk.Label(master=frm_2, text="Entered text is: ")
box = tk.Entry(master=frm_2)
box.insert(0,value_1)

frm_1.pack()
text.pack()
text_box.pack()
frm_2.pack()
text_2.pack()
box.pack()
window.mainloop()