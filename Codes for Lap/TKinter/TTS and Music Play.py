from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
from tkinter import *
window = Tk()
window.title("TTS and Music Player")
window.resizable(False,False)

def play_music():
    index = music_list.get(ANCHOR)
    if index == "  Rakita Rakita":
        music_1 = AudioSegment.from_mp3("/home/josepaul/Downloads/Rakita-Rakita-Rakita-MassTamilan.io.mp3")
        play(music_1)
        play_text["text"] = "Now Playing Rakita Rakita " 
    elif index == "  Vengamavan":
        music_2 = AudioSegment.from_mp3("/home/josepaul/Downloads/Vengamavan-MassTamilan.org.mp3")
        play(music_2)
        play_text["text"] = "Now Playing Vengamavan"
    elif index == "  Master the Blaster":
        music_3 = AudioSegment.from_mp3("/home/josepaul/Downloads/Master-the-Blaster-MassTamilan.io.mp3")
        play(music_3)
        play_text["text"] = "Now Playing Master the Blaster"
    elif index == "  Ethir Neechal":
        music_4 = AudioSegment.from_mp3("/home/josepaul/Downloads/Ethir-Neechal.mp3")
        play(music_4)
        play_text["text"] = "Now Playing Ethir Neechal"
    else:
        play_text["text"] = "Invalid Selection"

def GTTS():
    tts = gTTS(enter_text.get(1.0,END), lang="en-uk")
    tts.save("user_input.mp3")
    music = AudioSegment.from_mp3("user_input.mp3")
    play(music)

frm_music = Frame(master=window, padx=5, pady=5)
frm_music.pack(side=LEFT)
frm_TTS = Frame(master=window, pady=5, padx=5)
frm_TTS.pack(side=LEFT)

text = Label(frm_music, text="Select a music in this list")
text.grid(row=0, column=0)

music_list = Listbox(frm_music, width=16, height=4)
music_list.grid(row=1, column=0, ipadx=5)
music_list.insert(1, "  Rakita Rakita")
music_list.insert(2, "  Vengamavan")
music_list.insert(3, "  Master the Blaster")
music_list.insert(4, "  Ethir Neechal")

play_button = Button(frm_music, text="Play", command=play_music)
play_button.grid(row=2,column=0, pady=5)
play_text = Label(frm_music, text="")
play_text.grid(row=3, column=0)

text_1 = Label(master=frm_TTS, text="Enter the text here: ")
text_1.grid(row=0,column=0, sticky="ew")
enter_text = Text(master=frm_TTS, width=30, height=10)
enter_text.grid(row=1,column=0, sticky="ew")
buttn = Button(master=frm_TTS, text="Convert", command=GTTS)
buttn.grid(row=2, column=0)

window.mainloop()