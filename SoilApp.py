from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Soil App")
root.option_add('*tearOff', FALSE)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

root.geometry(
    str(int(root.winfo_screenwidth() / 2))+
    "x"+
    str(int(root.winfo_screenheight() / 2))+
    "+"+
    str(int(root.winfo_screenwidth() / 4))+
    "+"+
    str(int(root.winfo_screenheight() / 4)))

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

# Top buttons
New = ttk.Button(mainframe, text = "New")
New.grid(column = 0, row = 0, sticky = (N, W))
Open = ttk.Button(mainframe, text = "Open")
Open.grid(column = 1, row = 0, sticky = (N, W))
Save = ttk.Button(mainframe, text = "Save")
Save.grid(column = 2, row = 0, sticky = (N, W))
Info = ttk.Button(mainframe, text = "Info")
Info.grid(column = 3, row = 0, sticky = (N, W))
Help = ttk.Button(mainframe, text = "Help")
Help.grid(column = 4, row = 0, sticky = (N, W))


root.mainloop()
