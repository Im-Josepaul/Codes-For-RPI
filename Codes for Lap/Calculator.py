#We are starting Front End here
import PySimpleGUI as gy   #We are importing GUI as gy

Screen = [      #screen is the place where all numbers are displayed. 
     [
        gy.In(enable_events= True, size= (40,2), key="-screen-")
    ],
    [
        gy.Text("_" *40)
    ],
    [
        gy.Button(button_text="1", enable_events=True, key = "-ONE-"),
        gy.Button(button_text="2", enable_events=True, key = "-TWO-"),
        gy.Button(button_text="3", enable_events=True, key = "-THREE-"),
        gy.Button(button_text="+", enable_events=True, key = "-ADD-")
    ],
    [
        gy.Button(button_text="4", enable_events=True, key = "-FOUR-"),
        gy.Button(button_text="5", enable_events=True, key = "-FIVE-"),
        gy.Button(button_text="6", enable_events=True, key = "-SIX-"),
        gy.Button(button_text="-", size=(1,1), enable_events=True, key = "-MINUS-"),
        gy.Button(button_text="=", enable_events=True, key = "-EQUALTO-")
    ],
    [
        gy.Button(button_text="7", enable_events=True, key = "-SEVEN-"),
        gy.Button(button_text="8", enable_events=True, key = "-EIGHT-"),
        gy.Button(button_text="9", enable_events=True, key = "-NINE-"),
        gy.Button(button_text="X", size=(1,1), enable_events=True, key = "-MULTIPLY-")
    ],
    [
        gy.Button(button_text="0", pad=(50,0), enable_events=True, key = "-ZERO-"),
        gy.Button(button_text="/", size=(1,1), enable_events=True, key = "-DIVISION-")
    ]
]


layout = [      #This is our layout
    [
        gy.Column(Screen),
        gy.Button("Exit")
    ]
]

window = gy.Window("Calculator", layout)    #Here we defined our window.

#Our Front End ends here.

#We are starting the back end

while True:
    event, values = window.read()
    if event == "Exit" or event == gy.WIN_CLOSED:
        break
    if event == "-ONE-":
        Num_1 = int(values["-screen-"])


window.close()

