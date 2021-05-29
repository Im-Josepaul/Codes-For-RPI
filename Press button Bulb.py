from tkinter import *
import RPi.GPIO as GPIO
import webbrowser
window = Tk()
window.title("LED Press Button")
GPIO.setup(12, GPIO.OUT)  

def callback(link):
    webbrowser.open_new_tab(link)
def button_click(event):
    button["image"] = green_button
    GPIO.output(12, GPIO.HIGH)
def button_release(event):
    button["image"] = red_button
    GPIO.output(12, GPIO.LOW)
    
frame = Frame(master=window)
frame.grid(row=0, column=0)
text_1 = Label(master=frame,text="Complete the connections as shown")
here = Label(master=frame ,text="here", foreground="blue")
here.bind("<Button-1>",lambda e: callback("https://www.makeuseof.com/tag/add-button-raspberry-pi-project/"))
text_2 = Label(text="No need of connecting the button. Press here:")
red_button = PhotoImage(file="/home/josepaul/Desktop/Codes-For-RPI/Off Button.png")
green_button = PhotoImage(file="/home/josepaul/Desktop/Codes-For-RPI/On Button.png")
button = Button(master=window,image=red_button)
button.bind("<ButtonPress-1>", button_click)
button.bind("<ButtonRelease-1>", button_release)

text_1.pack(side=LEFT)
here.pack(side=LEFT)
text_2.grid(row=1, column=0, padx=5)
button.grid(row=2, column=0, pady=5)

window.mainloop()