import RPi.GPIO as GPIO  #Importing RPi.GPIO library as GPIO
GPIO.setmode(GPIO.BOARD) #Setting board mode
ledPin = 12
buttonPin = 16           #assigning pin number for each purpouse

#Here we are using RPI board pin numbers, not GPIO numbers.

GPIO.setup(ledPin, GPIO.OUT)                                #Setting up input and output 
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)
