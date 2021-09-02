from tkinter import  *
from playsound import playsound
window = Tk()
window.title("Music Player")
window.geometry("230x160")
window.resizable(False, False) 

def play():
    index = music_list.get(ANCHOR)
    if index == "  Rakita Rakita":
        playsound("/home/josepaul/Downloads/Rakita-Rakita-Rakita-MassTamilan.io.mp3")
        play_text["text"] = "Now Playing Rakita Rakita " 
    elif index == "  Vengamavan":
        playsound("/home/josepaul/Downloads/Vengamavan-MassTamilan.org.mp3")
        play_text["text"] = "Now Playing Vengamavan"
    elif index == "  Master the Blaster":
        playsound("/home/josepaul/Downloads/Master-the-Blaster-MassTamilan.io.mp3")
        play_text["text"] = "Now Playing Master the Blaster"
    elif index == "  Ethir Neechal":
        playsound("/home/josepaul/Downloads/Ethir-Neechal.mp3")
        play_text["text"] = "Now Playing Ethir Neechal"
    else:
        play_text["text"] = "Invalid Selection"

text = Label(window, text="Select a music in this list")
text.grid(row=0, column=0)

music_list = Listbox(master=window, width=16, height=4)
music_list.grid(row=1, column=0, ipadx=5)
music_list.insert(1, "  Rakita Rakita")
music_list.insert(2, "  Vengamavan")
music_list.insert(3, "  Master the Blaster")
music_list.insert(4, "  Ethir Neechal")

play_button = Button(window, text="Play", command=play)
play_button.grid(row=2,column=0, pady=5)
play_text = Label(window, text="")
play_text.grid(row=3, column=0)

window.mainloop()