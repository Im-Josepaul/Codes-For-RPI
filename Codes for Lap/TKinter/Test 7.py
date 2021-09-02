from tkinter import *
window = Tk()
window.geometry("200x210") 

def pressed(event):    
    Image.create_image(94,88,image=img_on)
    on_off["text"] = "ON"

def released(event):
    Image.create_image(101,87, image=img_off)
    on_off["text"] = "OFF" 

img_off = PhotoImage(file="/home/josepaul/Downloads/Bulb off.png")    
img_on = PhotoImage(file="/home/josepaul/Downloads/Bulb on.png")

Image = Canvas(window, width=150, height=170)
Image.grid(row=0, column=0)
Image.create_image(100,90, image = img_off)
on_off = Button(window, text="OFF", anchor="w")
on_off.grid(row=2, column=0)
on_off.bind("<ButtonPress-1>", pressed)
on_off.bind("<ButtonRelease-1>", released)

window.mainloop()