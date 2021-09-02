from tkinter import *
from tkinter import ttk
window_2 = Tk()
window_2.title("Measure Distance")

sensor = PhotoImage(file="/home/josepaul/Desktop/Codes-For-RPI/Off Button.png")
sensor_img = Label(master=window_2 ,image=sensor)
sensor_img.grid(row=0, column=0)
text_3 = Label(master=window_2, text="HC-SR04 sensor detected.")
text_3.grid(row=1, column=0)
frm_seperator = Frame(master=window_2)
frm_seperator.grid(row=2, column=0)
seperator = ttk.Separator(master=frm_seperator, orient="horizontal")
seperator.pack(fill=X)
frm_distance = Frame(master=window_2)
frm_distance.grid(row=3, column=0)
distance = Label(master=frm_distance, text="Distance = ")
en3_distance = Entry(master=frm_distance, width=10)
distance.pack(side=LEFT)
en3_distance.pack(side=LEFT)

window_2.mainloop()
