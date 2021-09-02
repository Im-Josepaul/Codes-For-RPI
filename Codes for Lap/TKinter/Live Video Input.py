from tkinter import *
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import threading
import datetime
import imutils
import cv2
import os
window = Tk()

class PhotoBoothApp:
    	def __init__(self, vs, outputPath):
            self.vs = vs                                                         #store the video stream object and output path, then initialize
            self.outputPath = outputPath                                         # the most recently read frame, thread for reading frames, and
            self.frame = None                                                    # the thread stop event
            self.thread = None
            self.stopEvent = None

            self.root = Tk()                                                     # initialize the root window and image panel
            self.panel = None
		    
            btn = Button(self.root, text="Snapshot!",                            # create a button, that when pressed, will take the current
			command=self.takeSnapshot)          		                         # frame and save it to file
            btn.pack(side="bottom", fill="both", expand="yes", padx=10,
			pady=10)
		    
            self.stopEvent = threading.Event()                                   # start a thread that constantly pools the video sensor for
            self.thread = threading.Thread(target=self.videoLoop, args=())       # the most recently read frame
            self.thread.start()
		    
            self.root.wm_title("PyImageSearch PhotoBooth")                       # set a callback to handle when the window is closed
            self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

window.title("Live Camera Input")
window.rowconfigure([0,1], weight = 1)
window.columnconfigure(0, weight = 1)
window.geometry("300x260")

blank = Text(window ,width=35, height=12)
blank.grid(row=0, column=0, sticky="nsew")
snapshot = Button(text="Snapshot", master=window)
snapshot.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()