from tkinter import *
window = Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=175)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
