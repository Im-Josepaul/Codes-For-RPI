from tkinter import *
window = Tk()
window.rowconfigure([0,1], weight = 1, minsize = 50)
window.columnconfigure(0, weight= 1, minsize = 100)

def pressed(event):
    txt["text"] = "Button is pressed."
def released(event):
    txt["text"] = "Button is released."
    
txt = Label(master=window, text="Button is Released")
txt.grid(row=0, column=0)
btn_1 = Button(master=window, text="Press")
btn_1.grid(row=1, column=0)
btn_1.bind("<ButtonPress-1>", pressed)
btn_1.bind("<ButtonRelease-1>", released)
window.mainloop()