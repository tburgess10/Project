from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


# function to upload graphs to the main page
def UploadGraphs(tab):

    # Create a frame for the plot
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=BOTH, expand=True)

    # Generate some data for the plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, label="Sine Wave")
    ax.set_title("Sine Wave Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()

    # Embed the Matplotlib figure in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=BOTH, expand=True)



# Create the main tkinter window
root = Tk()
root.title("Matplotlib with Tkinter")
UploadGraphs(root)

# Run the tkinter main loop
root.mainloop()
