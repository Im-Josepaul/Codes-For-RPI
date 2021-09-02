from tkinter import *
degree_farenheit = u"\N{DEGREE FAHRENHEIT}"                                                 
degree_celsius = (u"\N{DEGREE SIGN}" + "C")
#Creating Window with fixed size #########################################
window = Tk()                                                           ##
window.title(degree_farenheit + " to " + degree_celsius +" Converter")  ##
window.rowconfigure([0,1,2], weight = 1, minsize = 20)                  ##
window.columnconfigure([0,1], weight = 1, minsize = 10)                 ##
##########################################################################  
#Defining event_handler for Submit button ########
def submit():                                   ##
    fahrenheit = ent_temp.get()                 ##
    celsius = (5/9) * (float(fahrenheit) - 32)  ##
    celsius = round(celsius,2)                  ##
    ent_deg.insert(0,celsius)                   ##
##################################################
#Creating Layout #############################################################################
frm_temp = Frame(master=window)                                                             ##
frm_temp.pack()                                                                             ##
                                                                                            ##
lbl_far = Label(master=frm_temp, text="Enter temperature in " + degree_farenheit + " :")    ##
ent_temp = Entry(master=frm_temp, width=30)                                                 ##
lbl_far.grid(row=0, column=0)                                                               ##
ent_temp.grid(row=0, column= 1, pady=5)                                                     ##
                                                                                            ##
lbl_deg = Label(master=frm_temp, text="Temperature in " + degree_celsius + " is :")         ##
ent_deg = Entry(master=frm_temp, width=30)                                                  ##
lbl_deg.grid(row=1, column=0, sticky="w")                                                   ##
ent_deg.grid(row=1, column=1, pady=(5,0),padx=5)                                            ##
                                                                                            ##
frm_button = Frame(master=window)                                                           ##
frm_button.pack(fill=X, ipadx=5,ipady=5)                                                    ##                                  
submit_btn = Button(master=frm_button, text="Submit", command=submit)                       ##                                                                 											    ##
submit_btn.pack(side=RIGHT, ipadx=5, padx=5)                                                ##     
##############################################################################################

window.mainloop()

