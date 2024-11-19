from tkinter import *
from tkinter import ttk
from SoilAppComponentFiles import NewWindowComponents

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Sample")
    new_window.resizable(True, True)

    # Notebook tabs
    notebook = ttk.Notebook(new_window)
    notebook.grid(column=0, row=0, sticky="NSEW")
    tab1 = NewWindowComponents.create_tab1(notebook)
    tab2 = NewWindowComponents.create_tab2(notebook)
    tab3 = NewWindowComponents.create_tab3(notebook)
    tab4 = NewWindowComponents.create_tab4(notebook)
    tab5 = NewWindowComponents.create_tab5(notebook)

    # submit and cancel button frame
    BottomButtonsFrame = ttk.Frame(new_window)
    BottomButtonsFrame.grid(column = 0, row = 20, columnspan = 7, sticky = "")

    # Geometry
    new_window_resolution = "600x600"
    window_width = int(root.winfo_screenwidth() / 2.1)
    window_height = int(root.winfo_screenheight() / 1.2)
    position_x = int((root.winfo_screenwidth() - window_width) / 2)
    position_y = int((root.winfo_screenheight() - window_height) / 2.4)
    #new_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    new_window.geometry(f"{new_window_resolution}+{position_x}+{position_y}")
    # Extra padding at the top
    top_space = Label(tab1, text="")
    top_space.grid(row=0, column=0, columnspan=5, pady=(10, 0))

    # submit and cancel button
    SubmitB = ttk.Button(BottomButtonsFrame, text = "Submit")
    CancelB = ttk.Button(BottomButtonsFrame, text = "Cancel", command=new_window.destroy)

    # submit and cancel button layout
    SubmitB.grid(column = 0, row = 0, sticky = (N, W), pady = (15, 0), padx=(0, 5))
    CancelB.grid(column = 7, row = 0, sticky = (N, E), pady = (15, 0), padx=(5, 0))

root = Tk()
root.title("Soil App")
root.option_add('*tearOff', FALSE)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)


window_width = int(root.winfo_screenwidth() / 1.5)
window_height = int(root.winfo_screenheight() / 1.5)
position_x = int((root.winfo_screenwidth() - window_width) / 2)
position_y = int((root.winfo_screenheight() - window_height) / 2)

window_res = "380x300"

root.geometry(f"{window_res}+{position_x}+{position_y}")

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W))

# Top buttons
New = ttk.Button(mainframe, text = "New", style="Custom.TButton", command = open_new_window)
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
