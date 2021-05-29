from tkinter import *
import time
import webbrowser
window = Tk()
window.title("Ultrasonic sensor")
window.geometry("430x80")
TRIG = 16
ECHO = 18
i=0
#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)

def window_2():
    window_2 = Tk()
    window_2.title("Measure Distance")

    sensor = PhotoImage(file="/home/josepaul/Desktop/Codes-For-RPI/HC-SR04 sensor 2.png")
    sensor_img = Label(master=window_2, image=sensor)
    sensor_img.grid(row=0, column=0)
    text_3 = Label(master=window_2, text="HC-SR04 sensor detected.")
    text_3.grid(row=1, column=0)
    seperator = Label(master=window_2, text="_"* 50)
    seperator.grid(row=2, column=0, sticky="ew")
    frm_distance = Frame(master=window_2)
    frm_distance.grid(row=3, column=0, pady=10)
    distance = Label(master=frm_distance, text="Distance = ")
    en3_distance = Entry(master=frm_distance, width=10)
    distance.pack(side=LEFT)
    en3_distance.pack(side=LEFT)

    sensor_check()
    en3_distance.insert(0,distance)
    window_2.mainloop()

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

    except KeyboardInterrupt:
        GPIO.cleanup()
  
def callback(link):
    webbrowser.open_new_tab(link)

def open_2():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    if GPIO.input(ECHO)==1:
        window.destroy()
        window_2()

text_2_frm = Frame(master=window)
text_2_frm.grid(row=1, column=0, sticky="ns", padx=10)
text_1 = Label(master=window, text="Place an object infront of the sensor to detect sensor.")
text_1.grid(row=0, column=0)
text_2 = Label(master=text_2_frm, text="If sensor isn't detected, check your connections as shown")
here = Label(master=text_2_frm, text="here", fg="Blue")
text_2.pack(side=LEFT)
here.bind("<Button-1>",lambda e: callback("https://www.electronicshub.org/wp-content/uploads/2018/02/Raspberry-Pi-Ultrasonic-Sensor-Interface-Circuit-Diagram.jpg"))
here.pack(side=LEFT)

window.mainloop()