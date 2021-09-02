from playsound import playsound
from gtts import gTTS
from tkinter import *
window = Tk()
window.title("Google Text to Speech Converter")
window.geometry("250x230")
window.resizable(False,False)

def GTTS():
	tts = gTTS(enter_text.get(1.0,END), lang="en-uk")
	tts.save("user_input.mp3")
	playsound("user_input.mp3")

frm_all = Frame(master=window)
frm_all.pack(fill=Y)
text_1 = Label(master=frm_all, text="Enter the text here: ")
text_1.grid(row=0,column=0, sticky="ew")
enter_text = Text(master=frm_all, width=30, height=10)
enter_text.grid(row=1,column=0, sticky="ew")
buttn = Button(master=frm_all, text="Convert", command=GTTS)
buttn.grid(row=2, column=0, sticky="ew")

window.mainloop()