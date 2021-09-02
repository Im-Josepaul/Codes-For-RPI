from tkinter import *
window = Tk()
window.title("Detials Entry Form")

frame = Frame(master=window, relief=SUNKEN, borderwidth=5)
frame.pack()

labels = [
    "First Name: ",
    "Last Name: ",
    "Address Line 1: ",
    "Address Line 2: ",
    "City: ",
    "State/Provine: ",
    "Postal Code: ",
    "Country: "
]

for idx,text in enumerate(labels):
    lab = Label(master=frame, text=text)
    ent = Entry(master=frame, width=50)
    lab.grid(row=idx, column=0, pady=3)
    ent.grid(row=idx, column=1,pady=3)

frm_button = Frame()
frm_button.pack(fill=X, ipadx=5, ipady=5)

Submit = Button(master=frm_button, text="Submit")
Submit.pack(side=RIGHT, padx=10, ipadx=10)

Clear = Button(master=frm_button, text="Clear")
Clear.pack(side=RIGHT, ipadx=10)

window.mainloop()