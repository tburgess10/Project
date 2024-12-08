import sqlite3
from tkinter import *
from tkinter import ttk
from customtkinter import *
from SoilAppComponentFiles import NewWindowComponents

def insert_data(tab1_widgets, tab2_widgets, tab3_widgets):
    
    # replace the line below with the path to your soil databse, 
    # still trying to figure out a way to make it easily 
    # accessable to everyone regardless of path if possible.
    db_path = r"C:\Users\granb\Downloads\Soil_framework.sqlite"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # get sample details entries
    DataRecieved = tab1_widgets["dataRecieved"]["DataRecievedE"].get()
    DataSampled = tab1_widgets["dataRecieved"]["DataSampledE"].get()
    DateCompleted = tab1_widgets["dataRecieved"]["DataCompletedE"].get()
    ProjectNum = tab1_widgets["dataRecieved"]["ProjectNumE"].get()
    PlantNum = tab1_widgets["dataRecieved"]["PlantNumE"].get()
    RouteNum = tab1_widgets["dataRecieved"]["RouteNumE"].get()
    CityOrCounty = tab1_widgets["cityCounty"]["CityOrCountyCB"].get()
    FieldSampleNum = tab1_widgets["fieldSample"]["FieldSampleE"].get()
    SubmittedBy = tab1_widgets["fieldSample"]["SubmittedByE"].get()
    Station = tab1_widgets["station"]["StationE1"].get()+"+"+tab1_widgets["station"]["StationE2"].get()
    SampleLocation = tab1_widgets["sampleLocStructure"]["SampleLocationE"].get()
    StructureBoring = tab1_widgets["sampleLocStructure"]["StructureBoringE"].get()
    Start = tab1_widgets["startEnd"]["StartE"].get()
    End = tab1_widgets["startEnd"]["EndE"].get()
    material_value = tab1_widgets["materialRadioButton"]["materialVar"].get()
    material_mapping = {
        0: "SOIL",
        1: "CMA",
        2: "OTHER",
        3: "AGGREGATE",
        4: "PROFICIENCY",
    }
    material_name = material_mapping.get(material_value, "Unknown")
    materialDesc = tab1_widgets["materialDesc"]["get_material_description"]()
    UPCCode = tab1_widgets["timeCharge"]["UPCCodeE"].get()
    DepartmentCode = tab1_widgets["timeCharge"]["DepartmentCodeE"].get()
    TaskCode = tab1_widgets["timeCharge"]["TaskCodeE"].get()
    ActivityCode = tab1_widgets["timeCharge"]["ActivityCodeE"].get()
    selected_tests = tab1_widgets["testsRequired"]["get_selected_tests"]()
    TestedBy = tab1_widgets["testTitle"]["TestedByCB"].get()
    Title = tab1_widgets["testTitle"]["TitleCB"].get()
    Remarks = tab1_widgets["remarks"]["get_remarks_description"]()
    
    try:
        cursor.execute("""
            INSERT INTO SampleDetails (DateReceived, DateSampled, DateCompleted, ProjectNumber,
            PlantNumber, RouteNumber, CityCounty, FieldNumber, SubmittedBy, Station, SampleLocation, 
            Structure, StartDepth, EndDepth, Material, Description, UPCcode, DepartmentCode, TaskCode, 
            Activitycode, TestsRequired, TestedBy, Title, Remarks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (DataRecieved, DataSampled, DateCompleted, ProjectNum, PlantNum, RouteNum, 
            CityOrCounty, FieldSampleNum, SubmittedBy, Station, SampleLocation, StructureBoring, 
            Start, End, material_name, materialDesc, UPCCode, DepartmentCode, TaskCode, ActivityCode, 
            selected_tests, TestedBy, Title, Remarks))
    
        conn.commit()
        print("Data inserted into Sample Details successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)

    # get atterberg tab entries
    LiquidLimitTareNumber = tab2_widgets["atterberg"]["CupLiqE"].get()
    LiquidLimitTareWeight = tab2_widgets["atterberg"]["CupWLiqE"].get()
    LiquidLimitWeight = tab2_widgets["atterberg"]["WetLiqE"].get()
    LiquidLimitDryWeight = tab2_widgets["atterberg"]["DryLiq"].get()
    LiquidLimitNumberOfBlows = tab2_widgets["atterberg"]["BlowsE"].get()
    LiquidLimitNotObtained = tab2_widgets["atterberg"]["firstBool"]()
    PlasticLimitTareNumber = tab2_widgets["atterberg"]["CupPlasE"].get()
    PlasticLimitTareWeight = tab2_widgets["atterberg"]["CupWPlasE"].get()
    PlasticLimitWetWeight = tab2_widgets["atterberg"]["WetPlasE"].get()
    PlasticLimitDryWeight = tab2_widgets["atterberg"]["DryPlas"].get()
    PlasticLimitNotObtained = tab2_widgets["atterberg"]["secondBool"]()

    try:
        cursor.execute("""
            INSERT INTO Atterberg (LiquidLimitTareNumber, LiquidLimitTareWeight, LiquidLimitWeight, 
            LiquidLimitDryWeight, LiquidLimitNumberOfBlows, LiquidLimitNotObtained, 
            PlasticLimitTareNumber, PlasticLimitTareWeight, PlasticLimitWetWeight, 
            PlasticLimitDryWeight, PlasticLimitNotObtained)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (LiquidLimitTareNumber, LiquidLimitTareWeight, LiquidLimitWeight, 
            LiquidLimitDryWeight, LiquidLimitNumberOfBlows, LiquidLimitNotObtained, 
            PlasticLimitTareNumber, PlasticLimitTareWeight, PlasticLimitWetWeight, 
            PlasticLimitDryWeight, PlasticLimitNotObtained))

        conn.commit()
        print("Data inserted into Atterberg successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    
    # Get Proctor tab entries
    dateCom = tab3_widgets["dateCompleted"]["dateComE"].get()
    moldWeight = tab3_widgets["moldFrame"]["moldWeightE"].get()
    moldNum = tab3_widgets["moldFrame"]["moldNumCB"].get()
    WoCSL1 = tab3_widgets["pointFrame"]["WoCSLE1"].get()
    WoCSL2 = tab3_widgets["pointFrame"]["WoCSLE2"].get()
    WoCSL3 = tab3_widgets["pointFrame"]["WoCSLE3"].get()
    WoCSL4 = tab3_widgets["pointFrame"]["WoCSLE4"].get()
    WoCSL5 = tab3_widgets["pointFrame"]["WoCSLE5"].get()
    WoCSL6 = tab3_widgets["pointFrame"]["WoCSLE6"].get()
    WoCSL7 = tab3_widgets["pointFrame"]["WoCSLE7"].get()
    dishNum1 = tab3_widgets["pointFrame"]["dishNumE1"].get()
    dishNum2 = tab3_widgets["pointFrame"]["dishNumE2"].get()
    dishNum3 = tab3_widgets["pointFrame"]["dishNumE3"].get()
    dishNum4 = tab3_widgets["pointFrame"]["dishNumE4"].get()
    dishNum5 = tab3_widgets["pointFrame"]["dishNumE5"].get()
    dishNum6 = tab3_widgets["pointFrame"]["dishNumE6"].get()
    dishNum7 = tab3_widgets["pointFrame"]["dishNumE7"].get()
    WoD1 = tab3_widgets["pointFrame"]["WoDE1"].get()
    WoD2 = tab3_widgets["pointFrame"]["WoDE2"].get()
    WoD3 = tab3_widgets["pointFrame"]["WoDE3"].get()
    WoD4 = tab3_widgets["pointFrame"]["WoDE4"].get()
    WoD5 = tab3_widgets["pointFrame"]["WoDE5"].get()
    WoD6 = tab3_widgets["pointFrame"]["WoDE6"].get()
    WoD7 = tab3_widgets["pointFrame"]["WoDE7"].get()
    WoDaWS1 = tab3_widgets["pointFrame"]["WoDaWSE1"].get()
    WoDaWS2 = tab3_widgets["pointFrame"]["WoDaWSE2"].get()
    WoDaWS3 = tab3_widgets["pointFrame"]["WoDaWSE3"].get()
    WoDaWS4 = tab3_widgets["pointFrame"]["WoDaWSE4"].get()
    WoDaWS5 = tab3_widgets["pointFrame"]["WoDaWSE5"].get()
    WoDaWS6 = tab3_widgets["pointFrame"]["WoDaWSE6"].get()
    WoDaWS7 = tab3_widgets["pointFrame"]["WoDaWSE7"].get()
    WoDaDS1 = tab3_widgets["pointFrame"]["WoDaDSE1"].get()
    WoDaDS2 = tab3_widgets["pointFrame"]["WoDaDSE2"].get()
    WoDaDS3 = tab3_widgets["pointFrame"]["WoDaDSE3"].get()
    WoDaDS4 = tab3_widgets["pointFrame"]["WoDaDSE4"].get()
    WoDaDS5 = tab3_widgets["pointFrame"]["WoDaDSE5"].get()
    WoDaDS6 = tab3_widgets["pointFrame"]["WoDaDSE6"].get()
    WoDaDS7 = tab3_widgets["pointFrame"]["WoDaDSE7"].get()
    
    try:
        cursor.execute("""
            INSERT INTO Atterberg ()
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, ())

        conn.commit()
        print("Data inserted into Proctor successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)

    conn.close()

def open_info_menu():
    new_window = Toplevel(root)
    new_window.title("Info")
    new_window.resizable(False, False)

    new_window.columnconfigure(0, weight=1)
    new_window.rowconfigure(0, weight=1)

    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    window_width = int(root.winfo_screenwidth() / 2.0)
    window_height = int(root.winfo_screenheight() / 2.0)
    position_x = root_x + (root_width - window_width) // 2
    position_y = root_y + (root_height - window_height) // 2
    new_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    infoL = CTkLabel(
        new_window, 
        text="Click the new button to get started with inputting sample data\nwhen finished click the submit button."
    )
    infoL.grid(column=0, row=0, sticky="NSEW")



def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Sample")
    new_window.resizable(False, False)

    new_window.columnconfigure(0, weight=1)
    new_window.rowconfigure(0, weight=1)

    # Notebook tabs
    notebook = ttk.Notebook(new_window)
    notebook.grid(column=0, row=0, sticky="NSEW")
    tab1 = NewWindowComponents.create_tab1(notebook)
    tab2 = NewWindowComponents.create_tab2(notebook)
    tab3 = NewWindowComponents.create_tab3(notebook)
    tab4 = NewWindowComponents.create_tab4(notebook)
    #tab5 = NewWindowComponents.create_tab5(notebook)

    tab1_widgets = tab1.widgets
    tab2_widgets = tab2.widgets
    tab3_widgets = tab3.widgets

    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    # submit and cancel button frame
    BottomButtonsFrame = ttk.Frame(new_window)
    BottomButtonsFrame.grid(column = 0, row = 20, columnspan = 7, sticky = "")

    # Geometry
    window_width = int(root.winfo_screenwidth() / 1.5)
    window_height = int(root.winfo_screenheight() / .8)
    position_x = root_x + (root_width - window_width) // 2
    position_y = root_y + (root_height - window_height) // 2
    new_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Extra padding at the top
    top_space = Label(tab1, text="")
    top_space.grid(row=0, column=0, columnspan=5, pady=(10, 0))

    # submit and cancel button
    SubmitB = CTkButton(BottomButtonsFrame, 
        text = "Submit", 
        command=lambda: insert_data(tab1_widgets, tab2_widgets, tab3_widgets),
        border_color="#1751BD", 
        border_width=2)
    CancelB = CTkButton(BottomButtonsFrame, 
        text = "Cancel", 
        command=new_window.destroy,
        border_color="#1751BD", 
        border_width=2)

    # submit and cancel button layout
    SubmitB.grid(column = 0, row = 0, sticky = (N, W), pady = (10, 10), padx=(0, 5))
    CancelB.grid(column = 7, row = 0, sticky = (N, E), pady = (10, 10), padx=(5, 0))

root = CTk()
root.title("Soil App")
root.option_add('*tearOff', FALSE)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width / 1.5)
window_height = int(screen_height / 1.5)
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

mainframe = CTkFrame(root, corner_radius=20)
mainframe.grid(column = 0, row = 0, sticky = (N, W))


# Top buttons
New = CTkButton(mainframe, text = "New", width=65, height = 25, border_color="#1751BD", border_width=2, command = open_new_window)
New.grid(column = 0, row = 0, sticky = (N, W))
Open = CTkButton(mainframe, text = "Open", width=65, height = 25, border_color="#1751BD", border_width=2)
Open.grid(column = 1, row = 0, sticky = (N, W))
Save = CTkButton(mainframe, text = "Save", width=65, height = 25, border_color="#1751BD", border_width=2)
Save.grid(column = 2, row = 0, sticky = (N, W))
Info = CTkButton(mainframe, text = "Info", width=65, height = 25, border_color="#1751BD", border_width=2, command=open_info_menu)
Info.grid(column = 3, row = 0, sticky = (N, W))

root.mainloop()
