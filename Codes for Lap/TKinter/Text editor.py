from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename   #These are part of Tkinter. We need to call it seperately.
window = Tk()
window.title("Python Text Editor")
window.rowconfigure(0, weight= 2, minsize=500)          #Setting column's to autosize
window.columnconfigure([1], weight= 2, minsize= 500)    #Setting row's to autosize

def new_file():                                                         
    menu_bar = Menu(master=window, activeborderwidth=2, cursor="dot")

    file = Menu(menu_bar, tearoff=0)                        #   I don't need to tell this, but this is the same line of code that is
    file.add_command(label="New File", command=new_file)    #   written in the bottom of this code. I thought of addding this as a 
    file.add_command(label="Open File", command=open_file)  #   function and call it here, inside new_file function, but that will
    file.add_command(label="Save", command=save_file)       #   make an error. So I need to do this in this way
    file.add_separator()
    file.add_command(label="Exit", command=exit)    
    menu_bar.add_cascade(label="File", menu=file)
    
    themes = Menu(menu_bar, tearoff=0)
    themes.add_command(label="Light", command=Light)
    themes.add_command(label="Grey", command=Grey)
    themes.add_command(label="Dark", command=Dark)
    themes.add_command(label="Hacker", command=hacker)
    menu_bar.add_cascade(label="Themes", menu=themes)

    window.config(menu=menu_bar)

    scroll = Scrollbar(master=window)
    scroll.grid(row=0,column=2, sticky="ns")
    editor = Text(master=window, yscrollcommand=scroll.set)
    scroll.config(command=editor.yview)
    editor.grid(row=0, column=1, padx=(0,5), sticky="nsew")
    
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(                                     #   Here we use the Tkinter parts that we called before
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    editor.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        editor.insert(END, text)
    window.title(f"Python Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(                                   #   I know you will start to understand this code. Good thing.
        defaultextension="txt",                                     #   I copied this from a website, so who cares!
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = editor.get(1.0, END)
        output_file.write(text)
    window.title(f"Python Text Editor - {filepath}")
def exit():
    window.destroy()

def Light():
    editor["bg"] = "White"
    editor["fg"] = "Black"
    editor.config(insertbackground="Black")
    menu_bar["background"] = "White"
def Grey():
    editor["bg"] = "Grey"
    editor["fg"] = "White"
    editor.config(insertbackground="White")
    menu_bar["background"] = "White"
def Dark():
    editor["bg"] = "Black"
    editor["fg"] = "White"
    editor.config(insertbackground="White")
    menu_bar["background"] = "Grey"
def hacker():
    editor["bg"] = "Black"
    editor["fg"] = "#33fe00"
    editor.config(insertbackground="#33fe00")
    menu_bar["background"] = "#33fe00"

menu_bar = Menu(master=window, activeborderwidth=2, cursor="dot")

file = Menu(menu_bar, tearoff=0)
file.add_command(label="New File", command=new_file)
file.add_command(label="Open File", command=open_file)
file.add_command(label="Save", command=save_file)
file.add_separator()
file.add_command(label="Exit", command=exit)    
menu_bar.add_cascade(label="File", menu=file)

themes = Menu(menu_bar, tearoff=0)
themes.add_command(label="Light", command=Light)
themes.add_command(label="Grey", command=Grey)
themes.add_command(label="Dark", command=Dark)
themes.add_command(label="Hacker", command=hacker)
menu_bar.add_cascade(label="Themes", menu=themes)

window.config(menu=menu_bar) 

scroll = Scrollbar(master=window)
scroll.grid(row=0,column=2, sticky="ns")
editor = Text(master=window, yscrollcommand=scroll.set)
scroll.config(command=editor.yview)
editor.grid(row=0, column=1, padx=(0,5), sticky="nsew")

window.mainloop()
