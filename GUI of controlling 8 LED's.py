import PySimpleGUI as sg    #Importing GUI
import webbrowser
#import RPi.GPIO as GPIO     #Importing GPIO pins of RPI

#GPIO.setmode(GPIO.BOARD)    #GPIO modes are set to board.
#GPIO.setwarnings(False)
ledPin = [7,11,12,13,15,16,18,22]
#for ele in ledPin:
#    GPIO.setup(ele, GPIO.OUT)

#   Here we are starting our Front-End of the programme.

layout= [
    [sg.Text("You can light all LED's connected to your Raspberry Pi using this software.")],
    [sg.Text("Please make sure all connections are made as shown"), sg.Text("here.", key="-HERE-",text_color="Blue", enable_events=True)],
    [sg.Text("Press the below buttons to switch ON and OFF the LED's.")],
    [sg.Text("Button 1"),           #   Here we are starting to give All buttons their names on to of them
    sg.Text("Button 2"),            #   for identifying which all buttons are used for each LED's.
    sg.Text("Button 3"),
    sg.Text("Button 4"),
    sg.Text("Button 5"),
    sg.Text("Button 6"),
    sg.Text("Button 7"),
    sg.Text("Button 8"),
    ],
    [sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON1-", pad=((8,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON2-", pad=((22,0),(5,0))),      #   Here we are making 8 buttons for each LED's 
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON3-", pad=((20,0),(5,0))),      #   which are used for turning on the LED's.
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON4-", pad=((22,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON5-", pad=((22,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON6-", pad=((21,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON7-", pad=((21,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/On Button.png", enable_events= True, key="-ON8-", pad=((21,0),(5,0))),
    ],
    [sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF1-", pad=((8,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF2-", pad=((22,0),(5,0))),    #   Here we are making 8 buttons for each LED's
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF3-", pad=((20,0),(5,0))),    #   which are used for turning off the LED's.
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF4-", pad=((22,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF5-", pad=((22,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF6-", pad=((21,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF7-", pad=((21,0),(5,0))),
    sg.Button(size=(20,20), image_filename = "/home/josepaul/Test Files/Off Button.png", enable_events= True, key="-OFF8-", pad=((21,0),(5,0))),
    ],
    [sg.Button("Exit", pad=((0,0),(10,0)))]
    ]
window = sg.Window("Light all LED's", layout, font="MathJax_Main")  #   Setting up the window

#   Here we ending the Front-End of the programme.

#   Here we are starting the Back-End for our programme.

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-HERE-" :
        webbrowser.open("https://content.instructables.com/ORIG/F35/L2SN/HN82KGOY/F35L2SNHN82KGOY.jpg?auto=webp&frame=1&fit=bounds&md=7ecfac69cf5815098a44df7b0e88d441", new=1)
    elif event == "-ON1-" :
        GPIO.output(ledPin[0], GPIO.HIGH)
    elif event == "-ON2-" :
        GPIO.output(ledPin[1], GPIO.HIGH)
    elif event == "-ON3-" :
            GPIO.output(ledPin[2], GPIO.HIGH)
    elif event == "-ON4-" :
            GPIO.output(ledPin[3], GPIO.HIGH)
    elif event == "-ON5-" :
            GPIO.output(ledPin[4], GPIO.HIGH)
    elif event == "-ON6-" :
            GPIO.output(ledPin[5], GPIO.HIGH)
    elif event == "-ON7-" :
            GPIO.output(ledPin[6], GPIO.HIGH)
    elif event == "-ON8-" :
            GPIO.output(ledPin[7], GPIO.HIGH)
    elif event == "-OFF1-" :
            GPIO.output(ledPin[0], GPIO.LOW)
    elif event == "-OFF2-" :
            GPIO.output(ledPin[1], GPIO.LOW)
    elif event == "-OFF3-" :
            GPIO.output(ledPin[2], GPIO.LOW)
    elif event == "-OFF4-" :
            GPIO.output(ledPin[3], GPIO.LOW)
    elif event == "-OFF5-" :
            GPIO.output(ledPin[4], GPIO.LOW)
    elif event == "-OFF6-" :
            GPIO.output(ledPin[5], GPIO.LOW)
    elif event == "-OFF7-" :
            GPIO.output(ledPin[6], GPIO.LOW)
    elif event == "-OFF8-" :
            GPIO.output(ledPin[7], GPIO.LOW)

    
#   Here we end the Back-End of the programme.

window.close()

#   End of Code