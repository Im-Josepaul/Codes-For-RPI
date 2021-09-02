import PySimpleGUI as sg    #Importing GUI
import webbrowser
import RPi.GPIO as GPIO     #Importing GPIO pins of RPI

GPIO.setmode(GPIO.BOARD)    #GPIO modes are set to board.
GPIO.setwarnings(False)
ledPin = 12
GPIO.setup(ledPin, GPIO.OUT) #GPIO Pin 12 is setuped as output pin.

#   Here we are starting our Front-End of the programme.

layout= [
    [sg.Text("You can light a bulb connected to your Raspberry Pi using this software.")],
    [sg.Text("Please make sure all connections are made as shown"), sg.Text("here.", key="-HERE-",text_color="Blue", enable_events=True)],
    [sg.Text("Press the below button to switch ON and OFF the bulb.")],
    [sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON-", pad=((170,0),(0,0))), 
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF-", pad=((20,0),(0,0)))],
    [sg.Button("Exit")]
    ]
window = sg.Window("Light a bulb", layout, font="MathJax_Main")

#   Here we ending the Front-End of the programme.

#   Here we are starting the Back-End for our programme.

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-HERE-" :
        webbrowser.open("https://www.makeuseof.com/tag/raspberry-pi-control-led/", new=1)
    elif event == "-ON-" :
        GPIO.output(ledPin, GPIO.HIGH)
    elif event == "-OFF-" :
        GPIO.output(ledPin, GPIO.LOW)
        
#   Here we end the Back-End of the programme.

window.close()

#   End of Code