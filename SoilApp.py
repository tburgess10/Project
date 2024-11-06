from tkinter import *
from tkinter import ttk

def open_new_window():

    # windows and frames
    new_window = Toplevel(root)
    new_window.title("New Sample")
    new_window.resizable(False, False)

    stationFrame = ttk.Frame(new_window)
    stationFrame.grid(column = 2, row = 10, columnspan = 3, sticky = (N, W), padx = (10, 0))

    startEndFrame = ttk.Frame(new_window)
    startEndFrame.grid(column = 0, row = 13, columnspan = 5, sticky = (N, W))

    MaterialRadioButtonsFrame = ttk.Frame(new_window)
    MaterialRadioButtonsFrame.grid(column = 1, row = 14, columnspan = 3, sticky = (N, W), padx = (10, 0), pady = (5, 5))

    innerMaterialRadioBFrame = ttk.Frame(MaterialRadioButtonsFrame)
    innerMaterialRadioBFrame.grid(column = 0, row = 1, columnspan = 3, sticky = (N, W))

    materialDescFrame = ttk.Frame(new_window)
    materialDescFrame.grid(column = 2, row = 15, columnspan = 3, rowspan = 3, sticky = (N, W), padx = (10, 0))

    TimeChargeInfoFrame = ttk.Frame(new_window)
    TimeChargeInfoFrame.grid(column = 6, row = 2, rowspan = 5, sticky = (N, W), padx = (60, 0))

    TestsRequiredFrame = ttk.Frame(new_window)
    TestsRequiredFrame.grid(column = 6, row = 7, rowspan = 6, sticky = (N, W), padx = (60, 0))

    TestTitleFrame = ttk.Frame(new_window)
    TestTitleFrame.grid(column = 6, row = 14, rowspan = 2, sticky = (N, W), padx = (60, 0))

    RemarksFrame = ttk.Frame(new_window)
    RemarksFrame.grid(column = 6, row = 15, rowspan = 2, sticky = (N, W), padx = (60, 0), pady = (30, 0))

    BottomButtonsFrame = ttk.Frame(new_window)
    BottomButtonsFrame.grid(column = 0, row = 20, columnspan = 7, sticky = (N, S, W, E))

    # Geometry
    window_width = int(root.winfo_screenwidth() / 2.1)
    window_height = int(root.winfo_screenheight() / 1.3)
    position_x = int((root.winfo_screenwidth() - window_width) / 2)
    position_y = int((root.winfo_screenheight() - window_height) / 2)
    new_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Extra padding at the top
    top_space = Label(new_window, text="")
    top_space.grid(row=0, column=0, columnspan=5, pady=(10, 0))

    # Label widgets
    DataRecievedL = ttk.Label(new_window, text="Data Received")
    DataSampledL = ttk.Label(new_window, text="Data Sampled")
    DataCompletedL = ttk.Label(new_window, text="Date Completed")
    ProjectNumL = ttk.Label(new_window, text="Project #")
    PlantNumL = ttk.Label(new_window, text="Plant #")
    RouteNumL = ttk.Label(new_window, text="Route #")
    CityOrCountyL = ttk.Label(new_window, text="City or County")
    FieldSampleL = ttk.Label(new_window, text="Field Sample #")
    SubmittedByL = ttk.Label(new_window, text="Submitted By")
    StationL = ttk.Label(new_window, text="Station")
    StationPlusL = ttk.Label(stationFrame, text="+")
    SampleLocationL = ttk.Label(new_window, text="Sample Location")
    StructureBoringL = ttk.Label(new_window, text="Structure/Boring")
    StartL = ttk.Label(startEndFrame, text="Start")
    EndL1 = ttk.Label(startEndFrame, text="ft   End")
    EndL2 = ttk.Label(startEndFrame, text="ft")
    MaterialL = ttk.Label(new_window, text="Material")
    MaterialDescriptionL = ttk.Label(new_window, text="Material\nDescription")
    TimeChargeInfoL = ttk.Label(new_window, text = "TIME CHARGE INFORMATION")
    UPCCodeL = ttk.Label(TimeChargeInfoFrame, text = "UPC Code")
    DepartmentCodeL = ttk.Label(TimeChargeInfoFrame, text = "Department Code")
    TaskCodeL = ttk.Label(TimeChargeInfoFrame, text = "Task Code")
    ActivityCodeL = ttk.Label(TimeChargeInfoFrame, text = "Activity Code")
    TestsRequiredL = ttk.Label(TestsRequiredFrame, text = "Tests Required")
    TestedByL = ttk.Label(TestTitleFrame, text = "Tested by:")
    TitleL = ttk.Label(TestTitleFrame, text = "Title:")
    RemarksL = ttk.Label(RemarksFrame, text = "Remarks")

    # Label widget grid layouts
    DataRecievedL.grid(column=0, row=1, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    DataSampledL.grid(column=0, row=2, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    DataCompletedL.grid(column=0, row=3, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    ProjectNumL.grid(column=0, row=4, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    PlantNumL.grid(column=0, row=5, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    RouteNumL.grid(column=0, row=6, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    CityOrCountyL.grid(column=0, row=7, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    FieldSampleL.grid(column=0, row=8, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    SubmittedByL.grid(column=0, row=9, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StationL.grid(column=0, row=10, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StationPlusL.grid(column=1, row=0, sticky=(N, W), pady = (3, 3), padx = (0, 0))
    SampleLocationL.grid(column=0, row=11, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StructureBoringL.grid(column=0, row=12, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StartL.grid(column=0, row=0, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    EndL1.grid(column=2, row=0, sticky=(N, W), pady = (3, 3), padx = (3, 0))
    EndL2.grid(column=4, row=0, sticky=(N, W), pady = (3, 3), padx = (3, 0))
    MaterialL.grid(column=0, row=14, columnspan=2, sticky=(N, W), pady = (10, 0), padx = (20, 0))
    MaterialDescriptionL.grid(column=0, row=15, columnspan=2, sticky=(N, W), pady = (15, 0), padx = (20, 0))
    TimeChargeInfoL.grid(column = 6, row = 1, sticky=(N, W), pady = (0, 5), padx = (100, 0))
    UPCCodeL.grid(column = 0, row = 1, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    DepartmentCodeL.grid(column = 0, row = 2, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    TaskCodeL.grid(column = 0, row = 3, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    ActivityCodeL.grid(column = 0, row = 4, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    TestsRequiredL.grid(column = 0, row = 0, sticky=(N, W), padx = (0, 22))
    TestedByL.grid(column = 0, row = 0, sticky = (N, W), pady = (0, 3))
    TitleL.grid(column = 0, row = 1, sticky = (N, W), pady = (3, 0))
    RemarksL.grid(column = 0, row = 0, sticky = (N, W), pady = (20, 0))

    # Entry widgets
    DataRecievedE = ttk.Entry(new_window, font=("Segoe UI", 8))
    DataSampledE = ttk.Entry(new_window, font=("Segoe UI", 8))
    DataCompletedE = ttk.Entry(new_window, font=("Segoe UI", 8))
    ProjectNumE = ttk.Entry(new_window, font=("Segoe UI", 8))
    PlantNumE = ttk.Entry(new_window, font=("Segoe UI", 8))
    RouteNumE = ttk.Entry(new_window, font=("Segoe UI", 8))
    FieldSampleE = ttk.Entry(new_window, font=("Segoe UI", 8))
    SubmittedByE = ttk.Entry(new_window, font=("Segoe UI", 8))
    StationE1 = ttk.Entry(stationFrame, font=("Segoe UI", 8), width=8)
    StationE2 = ttk.Entry(stationFrame, font=("Segoe UI", 8), width=8)
    SampleLocationE = ttk.Entry(new_window, font=("Segoe UI", 8))
    StructureBoringE = ttk.Entry(new_window, font=("Segoe UI", 8))
    StartE = ttk.Entry(startEndFrame, font=("Segoe UI", 8), width=7)
    EndE = ttk.Entry(startEndFrame, font=("Segoe UI", 8), width=7)
    UPCCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    DepartmentCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    TaskCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    ActivityCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))

    # Entry widget grid layouts
    DataRecievedE.grid(column=2, row=1, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    DataSampledE.grid(column=2, row=2, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    ProjectNumE.grid(column=2, row=4, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    PlantNumE.grid(column=2, row=5, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    RouteNumE.grid(column=2, row=6, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    FieldSampleE.grid(column=2, row=8, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    SubmittedByE.grid(column=2, row=9, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    StationE1.grid(column=0, row=0, sticky=(N, W), pady = (3, 3), padx = (0, 3))
    StationE2.grid(column=2, row=0, sticky=(N, W), pady = (3, 3), padx = (3, 0))
    SampleLocationE.grid(column=2, row=11, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    StructureBoringE.grid(column=2, row=12, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    StartE.grid(column=1, row=0, sticky=(N, W), pady = (3, 3), padx = (26, 0))
    EndE.grid(column=3, row=0, sticky=(N, W), pady = (3, 3), padx = (21, 0))
    UPCCodeE.grid(column = 1, row = 1, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    DepartmentCodeE.grid(column = 1, row = 2, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    TaskCodeE.grid(column = 1, row = 3, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    ActivityCodeE.grid(column = 1, row = 4, sticky=(N, W), pady = (3, 3), padx = (5, 0))

    # Combobox widgets
    CityOrCountyCB = ttk.Combobox(new_window, width = 17)
    TestedByCB = ttk.Combobox(TestTitleFrame, width = 17)
    TitleCB = ttk.Combobox(TestTitleFrame, width = 17)

    # Combobox widget grid layouts
    CityOrCountyCB.grid(column = 2, row = 7, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    TestedByCB.grid(column = 1, row = 0, sticky=(N, W), padx = (49, 0))
    TitleCB.grid(column = 1, row = 1, sticky=(N, W), padx = (49, 0))
    
    # RadioButton widgets
    style = ttk.Style()
    style.configure("Custom.TRadiobutton", font=("Segoe UI", 8), padding=(0,0))
    SoilRB = ttk.Radiobutton(MaterialRadioButtonsFrame, value=0,text = "SOIL", style="Custom.TRadiobutton")
    CMARB = ttk.Radiobutton(MaterialRadioButtonsFrame, value=1, text = "CMA", style="Custom.TRadiobutton")
    OtheRB = ttk.Radiobutton(MaterialRadioButtonsFrame, value=2,text = "OTHE", style="Custom.TRadiobutton")
    AggregatRB = ttk.Radiobutton(innerMaterialRadioBFrame, value=3,text = "AGGREGAT", style="Custom.TRadiobutton")
    ProficienRB = ttk.Radiobutton(innerMaterialRadioBFrame, value=4,text = "PROFICIEN", style="Custom.TRadiobutton")

    # RadioButton widget grid layouts
    SoilRB.grid(column = 0, row = 0, sticky = (N, W), padx = (10, 0))
    CMARB.grid(column = 1, row = 0, sticky = (N, W))
    OtheRB.grid(column = 2, row = 0, sticky = (N, W))
    AggregatRB.grid(column = 0, row = 0, sticky = (N, W), padx = (10, 0))
    ProficienRB.grid(column = 1, row = 0, sticky = (N, W), padx = (10, 0))

    # text widgets
    materialDescT = Text(materialDescFrame, height = 5, width = 20, font = ("Segoe UI", 8))
    RemarksT = Text(RemarksFrame, height = 5, width = 20, font = ("Segoe UI", 8))

    # text widget grid layouts
    materialDescT.grid(column = 0, row = 0, sticky = (N, W))
    RemarksT.grid(column = 1, row = 0, sticky = (N, W), padx = (57, 0), pady = (0, 20))

    # checkbox widgets
    classificatioBool = StringVar(value="classOff")
    classificatioC = Checkbutton(
        TestsRequiredFrame,
        text="CLASSIFICATION",
        onvalue="classOn",
        offvalue="classOff",
        variable=classificatioBool
    )
    ProctorBool = StringVar(value="procOff")
    ProctorC = Checkbutton(
        TestsRequiredFrame,
        text="PROCTOR",
        onvalue="procOn",
        offvalue="procOff",
        variable=ProctorBool
    )
    CaliBool = StringVar(value="caliOff")
    CaliC = Checkbutton(
        TestsRequiredFrame,
        text="CALIFORNIA BEARING RATIO",
        onvalue="caliOn",
        offvalue="caliOff",
        variable=CaliBool
    )
    UnconBool = StringVar(value="unconOff")
    UnconC = Checkbutton(
        TestsRequiredFrame,
        text="UNCONFINED STRENGTH",
        onvalue="unconOn",
        offvalue="unconOff",
        variable=UnconBool
    )
    SoilResBool = StringVar(value="SoilResOff")
    SoilResC = Checkbutton(
        TestsRequiredFrame,
        text="SOIL RESISTIVITY",
        onvalue="SoilResOn",
        offvalue="SoilResOff",
        variable=SoilResBool
    )
    PHBool = StringVar(value="PHOff")
    pHC = Checkbutton(
        TestsRequiredFrame,
        text="pH",
        onvalue="PHOn",
        offvalue="PHOff",
        variable=PHBool
    )

    # checkbox widget grid layouts
    classificatioC.grid(column = 1, row = 0, sticky = (N, W))
    ProctorC.grid(column = 1, row = 1, sticky = (N, W))
    CaliC.grid(column = 1, row = 2, sticky = (N, W))
    UnconC.grid(column = 1, row = 3, sticky = (N, W))
    SoilResC.grid(column = 1, row = 4, sticky = (N, W))
    pHC.grid(column = 1, row = 5, sticky = (N, W))

    # button widgets
    SubmitB = ttk.Button(BottomButtonsFrame, text = "Submit")
    CancelB = ttk.Button(BottomButtonsFrame, text = "Cancel", command=new_window.destroy)

    # button widget gridy layouts
    SubmitB.grid(column = 0, row = 0, sticky = (N, W), padx = (215, 20))
    CancelB.grid(column = 7, row = 0, sticky = (N, E))

root = Tk()
root.title("Soil App")
root.option_add('*tearOff', FALSE)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

window_width = int(root.winfo_screenwidth() / 1.5)
window_height = int(root.winfo_screenheight() / 1.5)

print(window_width)
print(window_height)

position_x = int((root.winfo_screenwidth() - window_width) / 2)
position_y = int((root.winfo_screenheight() - window_height) / 2)

root.geometry(f"853x480+{position_x}+{position_y}")

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

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
