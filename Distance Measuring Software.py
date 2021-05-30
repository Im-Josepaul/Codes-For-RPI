from tkinter import *
import RPi.GPIO as GPIO
import time
import webbrowser
window = Tk()
window.title("Distance Measuring Software")
window.geometry("350x250")
TRIG = 16
ECHO = 18
i=0
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings = False
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def callback(link):
    webbrowser.open_new_tab(link)
def sensor_check():
    try:
        while True:
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
            
            pulse_duration = pulse_end - pulse_start
            
            distance = pulse_duration * 17150
            
            distance = round(distance+1.15, 2)

            en3_distance.insert(0,distance)

    except KeyboardInterrupt:
        GPIO.cleanup()

sensor = PhotoImage(file="/home/josepaul/Desktop/Codes-For-RPI/HC-SR04 sensor 2.png")
sensor_img = Label(master=window, image=sensor)
sensor_img.grid(row=0, column=0)

text = Label(master=window, text="If distance isn't visible in the box, then")
text.grid(row=1, column=0)

frame_here = Frame(master=window)
frame_here.grid(row=2, column=0)
text_1 = Label(master=frame_here, text="check your connections as shown")
text_1.pack(side=LEFT)
here = Label(master=frame_here, text="here", fg="Blue")
here.pack(side=LEFT)
here.bind("<Button-1>",lambda e: callback("https://www.electronicshub.org/wp-content/uploads/2018/02/Raspberry-Pi-Ultrasonic-Sensor-Interface-Circuit-Diagram.jpg"))

seperator = Label(master=window, text="_"* 50)
seperator.grid(row=3, column=0)

frm_distance = Frame(master=window)
frm_distance.grid(row=4, column=0, pady=10)
distance = Label(master=frm_distance, text="Distance = ")
en3_distance = Entry(master=frm_distance, width=10)
distance.pack(side=LEFT)
en3_distance.pack(side=LEFT)

window.mainloop()
