from tkinter import *
window = Tk()
window.title("Increase and Decrease")
window.rowconfigure(0, weight = 1, minsize = 50)
window.columnconfigure([0,1,2], weight = 1, minsize = 50)

def increase():
    value = int(lbl_no["text"])
    lbl_no["text"] = value + 1
def decrease():
    value = int(lbl_no["text"])
    lbl_no["text"] = value - 1

dec_btn = Button(master=window, text="-", command=decrease)
dec_btn.grid(row=0, column=0, sticky="nsew")

lbl_no = Label(master=window, text="0")
lbl_no.grid(row=0, column=1, sticky="nsew")

inc_btn = Button(master=window, text="+", command=increase)
inc_btn.grid(row=0, column=2, sticky="nsew")

window.mainloop()