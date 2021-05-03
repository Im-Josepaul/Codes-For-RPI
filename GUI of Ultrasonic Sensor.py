import PySimpleGUI as sg    #Importing nessessary libraries
import webbrowser
import RPi.GPIO as GPIO
import time

sg.theme("Black")   #Importing theme

GPIO.setmode(GPIO.BOARD)   #Setting RPi Board mode
TRIG = 16          #These are the two pins of RPi where Trig and Echo pins of
ECHO = 18          #HC-SR04 should be connected. We can change this if needed. 
i=0
GPIO.setup(TRIG,GPIO.OUT)  #Setting 16th pin as output pin
GPIO.setup(ECHO,GPIO.IN)   #Setting 18th pin as input pin 

#Front-End of the programme starts here.

def second_screen():        #Second screen is defined as function. We need this later.
    layout = [
        [sg.Image(filename="/home/josepaul/Desktop/Codes-For-RPI/HC-SR04 sensor 2.png",key="-IMAGE-")],
        [sg.Text("HC-SR04 Sensor detected.")],
        [sg.Text("_" * 60)],
    [                               #Setting Layout of second screen
        sg.Text("Distance"),
        sg.In(size=(10,1), enable_events="False",disabled="True", key="-DISTANCE-")
    ],
    [sg.Text(key="-FAR-")]
    ]
    window = sg.Window("Distance Measuring Software", layout, modal = False, element_justification="centre")
    while True:
            event, values = window.read()
            GPIO.output(TRIG, True)
            time.sleep(0.00001)         #Activating sensor by activating TRIG pin
            GPIO.output(TRIG, False)    #A signal is transmitted when TRIG pin is HIGH

            while GPIO.input(ECHO)==0:      #When TRIG pin is activated, this command will activate simultaneously
                pulse_start = time.time()   #The time at which the signal from sensor is propogated is noted here.

            while GPIO.input(ECHO)==1:      #When signal reaches the reciever of the sensor, ECHO pin will become HIGH.
                pulse_end = time.time()     #The time at which the signal is recieved by sensor is noted here.

    pulse_duration = pulse_end - pulse_start    #The time taken by signal from Transmitter to Reciever of the sensor is calculated.

    distance = pulse_duration * 17150           #Thus we can calculate distance from sensor to the Body.

    distance = round(distance+1.15, 2)
    while True:
        if event == sg.WIN_CLOSED:
            break
        elif distance<=5:
            window.Element("-DISTANCE-").Update(default_text = distance)    #The distance is updated to a textbox.
            window.Element("-FAR-").Update("You are too near.")
            i=1
        elif distance>5 and distance>=20:
            window.Element("-DISTANCE-").Update(default_text = distance)
            window.Element("-FAR-").Update("You are too far.")              #Proximity of sensor is updated to a text.
            i=1
        time.sleep(2)    
    window.close()

First_Screen = [
    [sg.Text("Place an object infront of the sensor to detect sensor")],    #First screen is defined here.
    [sg.Text("If sensor isn't detected, check your connection as shown"),sg.Text("here.", text_color="blue", key="-LINK-", enable_events=True)],
    [sg.Button("Click Here", key="-BUTTON-")]
]

window = sg.Window("Distance Measuring Software",First_Screen, element_justification="centre")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-LINK-":
        webbrowser.open("https://www.electronicshub.org/wp-content/uploads/2018/02/Raspberry-Pi-Ultrasonic-Sensor-Interface-Circuit-Diagram.jpg", new=1)
    if GPIO.input(ECHO)==0:
        second_screen()
        break
    
window.close()