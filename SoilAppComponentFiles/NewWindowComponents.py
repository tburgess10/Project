from tkinter import *
from tkinter import ttk
from customtkinter import *

# Tab 1 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setup_station_frame(tab):
    stationFrame = ttk.Frame(tab)
    stationFrame.grid(column=2, row=10, columnspan=3, sticky=(N, W), padx=(10, 0))

    StationL = CTkLabel(tab, 
        text="Station", 
        height=10, 
        font=("Segoe UI", 12))
    StationL.grid(column=0, row=10, columnspan=2, sticky=(N, W), pady = (3, 3))
    StationPlusL = CTkLabel(stationFrame, 
        text="+", 
        height=10)
    StationPlusL.grid(column=1, row=0, sticky=(N, W), pady=(3, 3))

    StationTV1 = StringVar()
    StationTV2 = StringVar()

    StationE1 = CTkEntry(stationFrame, 
        textvariable= StationTV1, 
        font=("Segoe UI", 12), 
        width=52, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    StationE2 = CTkEntry(stationFrame, 
        textvariable= StationTV2, 
        font=("Segoe UI", 12), 
        width=53, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    StationE1.grid(column=0, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 3))
    StationE2.grid(column=2, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))

    return stationFrame, {"StationE1": StationE1, "StationE2": StationE2}

def setup_start_end_frame(tab):
    startEndFrame = ttk.Frame(tab)
    startEndFrame.grid(column=0, row=13, columnspan=5, sticky=(N, W))

    StartL = CTkLabel(startEndFrame, 
        text="Start", 
        height=10, 
        font=("Segoe UI", 12))
    EndL1 = CTkLabel(startEndFrame, 
        text="ft   End", 
        height=10, 
        font=("Segoe UI", 12))
    EndL2 = CTkLabel(startEndFrame, 
        text="ft", 
        height=10, 
        font=("Segoe UI", 12))
    StartL.grid(column=0, row=0, sticky=(N, W), pady=(3, 3))
    EndL1.grid(column=2, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))
    EndL2.grid(column=4, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))

    StartTV = StringVar()
    EndTV = StringVar()

    StartE = CTkEntry(startEndFrame, 
        textvariable= StartTV, 
        font=("Segoe UI", 12), 
        width=40, 
        height=10, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    EndE = CTkEntry(startEndFrame, 
        textvariable= EndTV, 
        font=("Segoe UI", 12), 
        width=40, 
        height=10, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    StartE.grid(column=1, row=0, sticky=(N, W), pady = (3, 3), padx = (33, 0))
    EndE.grid(column=3, row=0, sticky=(N, W), pady = (3, 3), padx = (21, 0))

    return startEndFrame, {"StartE": StartE, "EndE": EndE}

def setup_dataRecieved_to_routeNum_frame(tab):
    dataRecievedRouteNumFrame = ttk.Frame(tab)
    dataRecievedRouteNumFrame.grid(column=0, row=1, columnspan=5, rowspan=6)

    DataRecievedL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Data Received", 
        height=10, 
        font=("Segoe UI", 12),
        justify="left")
    DataSampledL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Data Sampled", 
        height=10, 
        font=("Segoe UI", 12))
    DataCompletedL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Date Completed", 
        height=10, 
        font=("Segoe UI", 12))
    ProjectNumL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Project #", 
        height=10, 
        font=("Segoe UI", 12))
    PlantNumL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Plant #", 
        height=10, 
        font=("Segoe UI", 12))
    RouteNumL = CTkLabel(dataRecievedRouteNumFrame, 
        text="Route #", 
        height=10, 
        font=("Segoe UI", 12))
    DataRecievedL.grid(column=0, row=1, columnspan=2, sticky=(N, W), pady = (3, 3))
    DataSampledL.grid(column=0, row=2, columnspan=2, sticky=(N, W), pady = (3, 3))
    DataCompletedL.grid(column=0, row=3, columnspan=2, sticky=(N, W), pady = (3, 3))
    ProjectNumL.grid(column=0, row=4, columnspan=2, sticky=(N, W), pady = (3, 3))
    PlantNumL.grid(column=0, row=5, columnspan=2, sticky=(N, W), pady = (3, 3))
    RouteNumL.grid(column=0, row=6, columnspan=2, sticky=(N, W), pady = (3, 3))

    DataRecievedE = StringVar()
    DataSampledE = StringVar()
    DataCompletedE = StringVar()
    ProjectNumE = StringVar()
    PlantNumE = StringVar()
    RouteNumE = StringVar()

    DataRecievedE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= DataRecievedE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    DataSampledE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= DataSampledE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    DataCompletedE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= DataCompletedE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    ProjectNumE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= ProjectNumE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    PlantNumE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= 
        PlantNumE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    RouteNumE = CTkEntry(dataRecievedRouteNumFrame, 
        textvariable= RouteNumE, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    DataRecievedE.grid(column=2, row=1, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataSampledE.grid(column=2, row=2, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    ProjectNumE.grid(column=2, row=4, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    PlantNumE.grid(column=2, row=5, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    RouteNumE.grid(column=2, row=6, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))

    return dataRecievedRouteNumFrame, {"DataRecievedE": DataRecievedE, "DataSampledE": DataSampledE,
        "DataCompletedE": DataCompletedE, "ProjectNumE": ProjectNumE, "PlantNumE": PlantNumE, "RouteNumE": RouteNumE}

def setup_city_county_frame(tab):
    cityCountyFrame = ttk.Frame(tab)
    cityCountyFrame.grid(column=0, row=7, columnspan=5, sticky=(N,W))

    CityOrCountyL = CTkLabel(cityCountyFrame, 
        text="City or County", 
        height=10, 
        font=("Segoe UI", 12))
    CityOrCountyL.grid(column=0, row=7, columnspan=2, sticky=(N, W), pady = (3, 3))

    cityCountyVAR = StringVar()

    CityOrCountyCB = CTkEntry(cityCountyFrame, 
        textvariable=cityCountyVAR, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    CityOrCountyCB.grid(column = 2, row = 7, sticky=(N, W), pady = (3, 3), padx = (20, 0))

    return cityCountyFrame, {"CityOrCountyCB": CityOrCountyCB}

def setup_fieldSample_to_submitted_frame(tab):
    fieldSampleSubmittedFrame = ttk.Frame(tab)
    fieldSampleSubmittedFrame.grid(column=0, row=8, columnspan=5, rowspan=2, sticky=(N,W))

    FieldSampleL = CTkLabel(fieldSampleSubmittedFrame, 
        text="Field Sample #", 
        height=10, 
        font=("Segoe UI", 12))
    SubmittedByL = CTkLabel(fieldSampleSubmittedFrame, 
        text="Submitted By", 
        height=10, 
        font=("Segoe UI", 12))
    FieldSampleL.grid(column=0, row=8, columnspan=2, sticky=(N, W), pady = (3, 3))
    SubmittedByL.grid(column=0, row=9, columnspan=2, sticky=(N, W), pady = (3, 3))

    FieldSampleTV = StringVar()
    SubmittedByTV = StringVar()

    FieldSampleE = CTkEntry(fieldSampleSubmittedFrame, 
        textvariable= FieldSampleTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    SubmittedByE = CTkEntry(fieldSampleSubmittedFrame, 
        textvariable= SubmittedByTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    FieldSampleE.grid(column=2, row=8, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (18, 0))
    SubmittedByE.grid(column=2, row=9, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (18, 0))

    return fieldSampleSubmittedFrame, {"FieldSampleE": FieldSampleE, "SubmittedByE": SubmittedByE}

def setup_sampleLoc_to_structureB_frame(tab):
    sampleLocStructureBFrame = ttk.Frame(tab)
    sampleLocStructureBFrame.grid(column=0, row=11, columnspan=5, rowspan=2, sticky=(N,W))

    SampleLocationL = CTkLabel(sampleLocStructureBFrame, 
        text="Sample Location", 
        height=10, 
        font=("Segoe UI", 12))
    StructureBoringL = CTkLabel(sampleLocStructureBFrame, 
        text="Structure/Boring", 
        height=10, 
        font=("Segoe UI", 12))
    SampleLocationL.grid(column=0, row=11, columnspan=2, sticky=(N, W), pady = (3, 3))
    StructureBoringL.grid(column=0, row=12, columnspan=2, sticky=(N, W), pady = (3, 3))

    SampleLocationTV = StringVar()
    StructureBoringTV = StringVar()

    SampleLocationE = CTkEntry(sampleLocStructureBFrame, 
        textvariable= SampleLocationTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    StructureBoringE = CTkEntry(sampleLocStructureBFrame, 
        textvariable= StructureBoringTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    SampleLocationE.grid(column=2, row=11, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (9, 0))
    StructureBoringE.grid(column=2, row=12, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (9, 0))

    return sampleLocStructureBFrame, {"SampleLocationE": SampleLocationE, "StructureBoringE": StructureBoringE}

def setup_material_radio_buttons_frame(tab):
    materialRadioButtonsFrame = ttk.Frame(tab)
    materialRadioButtonsFrame.grid(column=0, row=14, columnspan=5, rowspan=2, sticky=(N,W), pady=(5, 0))

    innerMaterialRadioBFrame = ttk.Frame(materialRadioButtonsFrame)
    innerMaterialRadioBFrame.grid(column = 2, row = 0, columnspan = 3, sticky = (N, W))

    MaterialL = CTkLabel(materialRadioButtonsFrame, 
        text="Material", 
        height=10, 
        font=("Segoe UI", 12))
    MaterialL.grid(column=0, row=0, columnspan=2, sticky=(N, W), pady = (10, 0))

    materialVar = IntVar(value=0)

    SoilRB = CTkRadioButton(innerMaterialRadioBFrame, 
        value=0, 
        variable= materialVar, 
        text= "SOIL", 
        radiobutton_width=10, 
        radiobutton_height=10, 
        width=30, 
        height=10, 
        font=("Segoe UI", 10),
        border_width_unchecked=1,
        border_color="#BABBBE")
    CMARB = CTkRadioButton(innerMaterialRadioBFrame, 
        value=1, 
        variable= materialVar, 
        text= "CMA", 
        radiobutton_width=10, 
        radiobutton_height=10, 
        width=30, 
        height=10, 
        font=("Segoe UI", 10),
        border_width_unchecked=1,
        border_color="#BABBBE")
    OtheRB = CTkRadioButton(innerMaterialRadioBFrame, 
        value=2, 
        variable= materialVar, 
        text= "OTHER", 
        radiobutton_width=10, 
        radiobutton_height=10, 
        width=30, 
        height=10, 
        font=("Segoe UI", 10),
        border_width_unchecked=1,
        border_color="#BABBBE")
    AggregatRB = CTkRadioButton(materialRadioButtonsFrame, 
        value=3, 
        variable= materialVar, 
        text= "AGGREGATE", 
        radiobutton_width=10, 
        radiobutton_height=10, 
        width=10, 
        height=10, 
        font=("Segoe UI", 10),
        border_width_unchecked=1,
        border_color="#BABBBE")
    ProficienRB = CTkRadioButton(materialRadioButtonsFrame, 
        value=4, 
        variable= materialVar, 
        text= "PROFICIENCY", 
        radiobutton_width=10, 
        radiobutton_height=10, 
        width=10, 
        height=10, 
        font=("Segoe UI", 10),
        border_width_unchecked=1,
        border_color="#BABBBE")
    SoilRB.grid(column = 0, row = 0, sticky = (N, W), padx = (10, 0))
    CMARB.grid(column = 1, row = 0, sticky = (N, W), padx = (15, 0))
    OtheRB.grid(column = 2, row = 0, sticky = (N, W), padx = (15, 0))
    AggregatRB.grid(column = 2, row = 1, sticky = (N, W), padx = (15, 0))
    ProficienRB.grid(column = 3, row = 1, sticky = (N, W), padx = (10, 0))

    return materialRadioButtonsFrame, {"materialVar": materialVar}

def setup_material_desc_frame(tab):
    materialDescFrame = ttk.Frame(tab)
    materialDescFrame.grid(column = 0, row = 16, columnspan = 5, rowspan = 3, sticky = (N, W))

    MaterialDescriptionL = CTkLabel(materialDescFrame, 
        text="Material\nDescription", 
        height=10, 
        justify="left", 
        font=("Segoe UI", 12))
    MaterialDescriptionL.grid(column=0, row=0, columnspan=2, sticky=(N, W), pady = (15, 0))
    
    materialDescT = CTkTextbox(materialDescFrame, 
        font = ("Segoe UI", 12), 
        width = 120, 
        height = 70, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    materialDescT.grid(column = 2, row = 0, sticky = (N, W), padx=(38, 0), pady=(10, 0))

    def get_material_description():
        return materialDescT.get("1.0", "end-1c")

    
    def set_material_description(value):
        materialDescT.delete("1.0", "end")
        materialDescT.insert("1.0", value)

    return materialDescFrame, {
        "MaterialDescT": materialDescT,
        "get_material_description": get_material_description,
        "set_material_description": set_material_description,
    }

def setup_time_charge_info_frame(tab):
    TimeChargeInfoFrame = ttk.Frame(tab)
    TimeChargeInfoFrame.grid(column = 6, row = 2, rowspan = 5, sticky = (N, W), padx = (60, 0))

    TimeChargeInfoTopFrame = ttk.Frame(tab)
    TimeChargeInfoTopFrame.grid(column=6, row=1, sticky=(N,W), padx=(60, 0))

    TimeChargeInfoL = CTkLabel(TimeChargeInfoTopFrame, 
        text = "TIME CHARGE INFORMATION",
        height=10, 
        font=("Segoe UI", 12))
    UPCCodeL = CTkLabel(TimeChargeInfoFrame, 
        text = "UPC Code",
        height=10, 
        font=("Segoe UI", 12))
    DepartmentCodeL = CTkLabel(TimeChargeInfoFrame, 
        text = "Department Code",
        height=10, 
        font=("Segoe UI", 12))
    TaskCodeL = CTkLabel(TimeChargeInfoFrame, 
        text = "Task Code",
        height=10, 
        font=("Segoe UI", 12))
    ActivityCodeL = CTkLabel(TimeChargeInfoFrame, 
        text = "Activity Code",
        height=10, 
        font=("Segoe UI", 12))
    TimeChargeInfoL.grid(column = 0, row = 0, sticky=(N, W), pady = (0, 5), padx = (35, 0))
    UPCCodeL.grid(column = 0, row = 2, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    DepartmentCodeL.grid(column = 0, row = 3, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    TaskCodeL.grid(column = 0, row = 4, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    ActivityCodeL.grid(column = 0, row = 5, sticky=(N, W), pady = (3, 3), padx = (0, 5))

    UPCCodeTV = StringVar()
    DepartmentCodeTV = StringVar()
    TaskCodeTV = StringVar()
    ActivityCodeTV = StringVar()

    UPCCodeE = CTkEntry(TimeChargeInfoFrame, 
        textvariable= UPCCodeTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    DepartmentCodeE = CTkEntry(TimeChargeInfoFrame, 
        textvariable= DepartmentCodeTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    TaskCodeE = CTkEntry(TimeChargeInfoFrame, 
        textvariable= TaskCodeTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    ActivityCodeE = CTkEntry(TimeChargeInfoFrame, 
        textvariable= ActivityCodeTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    UPCCodeE.grid(column = 1, row = 2, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    DepartmentCodeE.grid(column = 1, row = 3, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    TaskCodeE.grid(column = 1, row = 4, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    ActivityCodeE.grid(column = 1, row = 5, sticky=(N, W), pady = (3, 3), padx = (5, 0))

    return TimeChargeInfoFrame, {"UPCCodeE": UPCCodeE, "DepartmentCodeE": DepartmentCodeE, 
        "TaskCodeE": TaskCodeE, "ActivityCodeE": ActivityCodeE}

def setup_tests_required_frame(tab):
    TestsRequiredFrame = ttk.Frame(tab)
    TestsRequiredFrame.grid(column = 6, row = 7, rowspan = 6, sticky = (N, W), padx = (60, 0))

    TestsRequiredL = CTkLabel(TestsRequiredFrame, 
        text = "Tests Required",
        height=10, 
        font=("Segoe UI", 12))
    TestsRequiredL.grid(column = 0, row = 0, sticky=(N, W), padx = (0, 22))

    # Variables for checkboxes
    classificatioBool = StringVar(value="FALSE")
    ProctorBool = StringVar(value="FALSE")
    CaliBool = StringVar(value="FALSE")
    UnconBool = StringVar(value="FALSE")
    SoilResBool = StringVar(value="FALSE")
    PHBool = StringVar(value="FALSE")

    # Checkboxes
    classificatioC = CTkCheckBox(
        TestsRequiredFrame,
        text="CLASSIFICATION",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=classificatioBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    ProctorC = CTkCheckBox(
        TestsRequiredFrame,
        text="PROCTOR",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=ProctorBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    CaliC = CTkCheckBox(
        TestsRequiredFrame,
        text="CALIFORNIA BEARING RATIO",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=CaliBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    UnconC = CTkCheckBox(
        TestsRequiredFrame,
        text="UNCONFINED STRENGTH",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=UnconBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    SoilResC = CTkCheckBox(
        TestsRequiredFrame,
        text="SOIL RESISTIVITY",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=SoilResBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    pHC = CTkCheckBox(
        TestsRequiredFrame,
        text="pH",
        onvalue="TRUE",
        offvalue="FALSE",
        variable=PHBool,
        border_width=1,
        corner_radius=0,
        checkbox_width=10,
        checkbox_height=10,
        border_color="#BABBBE",
        text_color="#414143"
    )
    classificatioC.grid(column = 1, row = 0, sticky = (N, W))
    ProctorC.grid(column = 1, row = 1, sticky = (N, W))
    CaliC.grid(column = 1, row = 2, sticky = (N, W))
    UnconC.grid(column = 1, row = 3, sticky = (N, W))
    SoilResC.grid(column = 1, row = 4, sticky = (N, W))
    pHC.grid(column = 1, row = 5, sticky = (N, W))

    def get_selected_tests():
        tests = []
        if classificatioBool.get() == "TRUE":
            tests.append("CLASSIFICATION")
        if ProctorBool.get() == "TRUE":
            tests.append("PROCTOR")
        if CaliBool.get() == "TRUE": 
            tests.append("CALIFORNIA BEARING RATIO")
        if UnconBool.get() == "TRUE":
            tests.append("UNCONFINED STRENGTH")
        if SoilResBool.get() == "TRUE":
            tests.append("SOIL RESISTIVITY")
        if PHBool.get() == "TRUE":
            tests.append("pH")
        return " + ".join(tests)
    
    return TestsRequiredFrame, {"get_selected_tests": get_selected_tests,}

def setup_test_title_frame(tab):
    TestTitleFrame = ttk.Frame(tab)
    TestTitleFrame.grid(column = 6, row = 14, rowspan = 2, sticky = (N, W), padx = (60, 0))

    TestedByL = CTkLabel(TestTitleFrame, 
        text = "Tested by:",
        height=10, 
        font=("Segoe UI", 12))
    TitleL = CTkLabel(TestTitleFrame, 
        text = "Title:",
        height=10, 
        font=("Segoe UI", 12))
    TestedByL.grid(column = 0, row = 0, sticky = (N, W), pady = (0, 3))
    TitleL.grid(column = 0, row = 1, sticky = (N, W), pady = (3, 0))

    TestedByTV = StringVar()
    TitleTV = StringVar()

    TestedByCB = CTkEntry(TestTitleFrame, 
        textvariable= TestedByTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    TitleCB = CTkEntry(TestTitleFrame, 
        textvariable= TitleTV, 
        font=("Segoe UI", 12), 
        width=120, 
        height=20, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    TestedByCB.grid(column = 1, row = 0, sticky=(N, W), padx = (49, 0), pady=(0, 5))
    TitleCB.grid(column = 1, row = 1, sticky=(N, W), padx = (49, 0))

    return TestTitleFrame, {"TestedByCB": TestedByCB, "TitleCB": TitleCB}

def setup_remarks_frame(tab):
    RemarksFrame = ttk.Frame(tab)
    RemarksFrame.grid(column = 6, row = 16, rowspan = 2, sticky = (N, W), padx = (60, 0), pady = (30, 0))

    RemarksL = CTkLabel(RemarksFrame, 
        text = "Remarks",
        height=10, 
        font=("Segoe UI", 12))
    RemarksL.grid(column = 0, row = 0, sticky = (N, W), pady = (20, 0))

    RemarksT = CTkTextbox(RemarksFrame, 
        font = ("Segoe UI", 12), 
        width = 120, 
        height = 70, 
        corner_radius=0, 
        border_width=1,
        border_color="#BABBBE")
    RemarksT.grid(column = 1, row = 0, sticky = (N, W), padx = (57, 0), pady = (0, 20))

    def get_remarks_description():
        return RemarksT.get("1.0", "end-1c")

    def set_remarks_description(value):
        RemarksT.delete("1.0", "end")
        RemarksT.insert("1.0", value)

    return RemarksFrame, {
        "RemarksT": RemarksT,
        "get_remarks_description": get_remarks_description,
        "set_remarks_description": set_remarks_description,
    }

def create_tab1(notebook):
    style = ttk.Style()
    style.configure("TNotebook.Tab", font=("Segoe UI", 14))

    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Details")
    tab1['padding'] = (30, 0, 0, 0)

    stationFrame, station_widgets = setup_station_frame(tab1)
    startEndFrame, startEnd_widgets = setup_start_end_frame(tab1)
    dataRecievedRouteNumFrame, dataRecieved_widgets = setup_dataRecieved_to_routeNum_frame(tab1)
    cityCountyFrame, cityCounty_widgets = setup_city_county_frame(tab1)
    fieldSampleSubmittedFrame, fieldSample_widgets = setup_fieldSample_to_submitted_frame(tab1)
    sampleLocStructureBFrame, sampleLocStructure_widgets = setup_sampleLoc_to_structureB_frame(tab1)
    materialRadioButtonsFrame, materialRadioButton_widgets = setup_material_radio_buttons_frame(tab1)
    materialDescFrame, materialDesc_widgets = setup_material_desc_frame(tab1)
    TimeChargeInfoFrame, timeCharge_widgets = setup_time_charge_info_frame(tab1)
    TestsRequiredFrame, testsRequired_widgets = setup_tests_required_frame(tab1)
    TestTitleFrame, testTitle_widgets = setup_test_title_frame(tab1)
    RemarksFrame, remarks_widgets = setup_remarks_frame(tab1)

    tab1.widgets = {
        "station": station_widgets,
        "startEnd": startEnd_widgets,
        "dataRecieved": dataRecieved_widgets,
        "cityCounty": cityCounty_widgets,
        "fieldSample": fieldSample_widgets,
        "sampleLocStructure": sampleLocStructure_widgets,
        "materialRadioButton": materialRadioButton_widgets,
        "materialDesc": materialDesc_widgets,
        "timeCharge": timeCharge_widgets,
        "testsRequired": testsRequired_widgets,
        "testTitle": testTitle_widgets,
        "remarks": remarks_widgets
    }

    return tab1

# Tab 2 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_atterberg_Frame(tab):
    atterbergFrame = ttk.Labelframe(tab, text='Atterberg', padding=(20, 20, 20, 20))
    atterbergFrame.grid(column=1, row=1, sticky=(N,W))

    LiquedLimL = ttk.Label(atterbergFrame, text="Liquid Limit")
    PlasticLimL = ttk.Label(atterbergFrame, text="Plastic Limit")
    CupNumL = ttk.Label(atterbergFrame, text="Cup #")
    CupWeightL = ttk.Label(atterbergFrame, text="Cup Weight")
    WetWeightL = ttk.Label(atterbergFrame, text="Wet Weight")
    DryWeightL = ttk.Label(atterbergFrame, text="Dry Weight")
    NumBlowsL = ttk.Label(atterbergFrame, text="# Blows")
    CannotBeL = ttk.Label(atterbergFrame, text="Cannot Be Determined")
    LiquedLimL.grid(column=1, row=0, sticky=(N,W), padx=(10, 10))
    PlasticLimL.grid(column=2, row=0, sticky=(N,W))
    CupNumL.grid(column=0, row=1, sticky=(N,W), padx=(50, 0), pady=(5, 5))
    CupWeightL.grid(column=0, row=2, sticky=(N,W), padx=(50, 0), pady=(5, 5))
    WetWeightL.grid(column=0, row=3, sticky=(N,W), padx=(50, 0), pady=(5, 5))
    DryWeightL.grid(column=0, row=4, sticky=(N,W), padx=(50, 0), pady=(5, 5))
    NumBlowsL.grid(column=0, row=5, sticky=(N,W), padx=(50, 0), pady=(5, 5))
    CannotBeL.grid(column=0, row=6, sticky=(N,W))

    CupLiqTV = StringVar()
    CupPlasTV = StringVar()
    CupWLiqTV = StringVar()
    CupWPlasTV = StringVar()
    WetLiqTV = StringVar()
    WetPlasTV = StringVar()
    DryLiqTV = StringVar()
    DryPlasTV = StringVar()
    BlowsETV = StringVar()

    CupLiqE = ttk.Entry(atterbergFrame, textvariable= CupLiqTV,  width=10)
    CupPlasE = ttk.Entry(atterbergFrame, textvariable= CupPlasTV, width=10)
    CupWLiqE = ttk.Entry(atterbergFrame, textvariable= CupWLiqTV, width=10)
    CupWPlasE = ttk.Entry(atterbergFrame, textvariable= CupWPlasTV, width=10)
    WetLiqE = ttk.Entry(atterbergFrame, textvariable= WetLiqTV, width=10)
    WetPlasE = ttk.Entry(atterbergFrame, textvariable= WetPlasTV, width=10)
    DryLiq = ttk.Entry(atterbergFrame, textvariable= DryLiqTV, width=10)
    DryPlas = ttk.Entry(atterbergFrame, textvariable= DryPlasTV, width=10)
    BlowsE = ttk.Entry(atterbergFrame, textvariable= BlowsETV, width=10)
    CupLiqE.grid(column=1, row=1)
    CupPlasE.grid(column=2, row=1)
    CupWLiqE.grid(column=1, row=2)
    CupWPlasE.grid(column=2, row=2)
    WetLiqE.grid(column=1, row=3)
    WetPlasE.grid(column=2, row=3)
    DryLiq.grid(column=1, row=4)
    DryPlas.grid(column=2, row=4)
    BlowsE.grid(column=1, row=5)
    
    firstBool = StringVar(value="FALSE")
    firstC = Checkbutton(
        atterbergFrame,
        onvalue="TRUE",
        offvalue="FALSE",
        variable=firstBool
    )
    secondBool = StringVar(value="FALSE")
    secondC = Checkbutton(
        atterbergFrame,
        onvalue="TRUE",
        offvalue="FALSE",
        variable=secondBool
    )
    firstC.grid(column=1, row=6)
    secondC.grid(column=2, row=6)

    return atterbergFrame, {"CupLiqE": CupLiqE, 
        "CupPlasE": CupPlasE, "CupWLiqE": CupWLiqE,
        "CupWPlasE": CupWPlasE, "WetLiqE": WetLiqE,
        "WetPlasE": WetPlasE, "DryLiq": DryLiq,
        "DryPlas": DryPlas, "BlowsE": BlowsE, 
        "firstBool": lambda: firstBool.get(),
        "secondBool": lambda: secondBool.get(),
        "firstCheckbutton": firstC,
        "secondCheckbutton": secondC}

def setup_field_moisture_frame(tab):
    fieldMoistureFrame = ttk.Labelframe(tab, text='Field Moisture', padding=(20, 20, 20, 20))
    fieldMoistureFrame.grid(column=2, row=1)

    cupNumL = ttk.Label(fieldMoistureFrame, text="Cup #")
    cupWeightL = ttk.Label(fieldMoistureFrame, text="Cup Weight")
    wetWeightL = ttk.Label(fieldMoistureFrame, text="Wet Weight")
    dryWeightL = ttk.Label(fieldMoistureFrame, text="Dry Weight")
    fieldMoistL = ttk.Label(fieldMoistureFrame, text="Field Moisture if\n      provided")
    cupNumL.grid(column=0, row=0, sticky=(N,W))
    cupWeightL.grid(column=0, row=1, sticky=(N,W))
    wetWeightL.grid(column=0, row=2, sticky=(N,W))
    dryWeightL.grid(column=0, row=3, sticky=(N,W))
    fieldMoistL.grid(column=0, row=4, sticky=(N,W))

    cupNumTV = StringVar()
    cupWeightTV = StringVar()
    wetWeightTV = StringVar()
    dryWeightTV = StringVar()
    fieldMoistTV = StringVar()

    cupNumE = ttk.Entry(fieldMoistureFrame, textvariable= cupNumTV, width=10)
    cupWeightE = ttk.Entry(fieldMoistureFrame, textvariable= cupWeightTV, width=10)
    wetWeightE = ttk.Entry(fieldMoistureFrame, textvariable= wetWeightTV, width=10)
    dryWeightE = ttk.Entry(fieldMoistureFrame, textvariable= dryWeightTV, width=10)
    fieldMoistE = ttk.Entry(fieldMoistureFrame, textvariable= fieldMoistTV, width=10)
    cupNumE.grid(column=1, row=0, sticky=(N,W), pady=(0,3), padx=(7, 0))
    cupWeightE.grid(column=1, row=1, sticky=(N,W), pady=(3,3), padx=(7, 0))
    wetWeightE.grid(column=1, row=2, sticky=(N,W), pady=(3,3), padx=(7, 0))
    dryWeightE.grid(column=1, row=3, sticky=(N,W), pady=(3,3), padx=(7, 0))
    fieldMoistE.grid(column=1, row=4, sticky=(N,W), pady=(9,0), padx=(7, 0))
    return fieldMoistureFrame, {"cupNumE": cupNumE, "cupWeightE": cupWeightE,
        "wetWeightE": wetWeightE, "dryWeightE": dryWeightE, "fieldMoistE": fieldMoistE}

def create_tab2(notebook):
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Atterberg")
    tab2.grid_rowconfigure(0, weight=1)
    tab2.grid_rowconfigure(1, weight=0)
    tab2.grid_rowconfigure(2, weight=1)

    tab2.grid_columnconfigure(0, weight=1)
    tab2.grid_columnconfigure(1, weight=0)
    tab2.grid_columnconfigure(2, weight=1)

    atterbergFrame, atterberg_widgets = setup_atterberg_Frame(tab2)
    fieldMoistureFrame, moisture_widgets = setup_field_moisture_frame(tab2)

    tab2.widgets = {
        "atterberg": atterberg_widgets,
        "moisture": moisture_widgets
    }

    return tab2

# Tab 3 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_date_completed_frame(tab):
    dateCompletedFrame = ttk.Frame(tab, padding=(20, 20, 20, 20))
    dateCompletedFrame.grid(column=0, row=0, sticky=(N,W))

    style = ttk.Style()
    style.configure("TEntry", highlightthickness=2) 
    dateComL = ttk.Label(dateCompletedFrame, text="Date Completed")
    dateComL.grid(column=0, row=0, sticky=(N,W), padx=(0, 10))

    dateComTV = StringVar()

    dateComE = ttk.Entry(dateCompletedFrame, width=10, textvariable= dateComTV, style="TEntry")
    dateComE.grid(column=1, row=0)

    return dateCompletedFrame, {"dateComE": dateComE}

def setup_mold_frame(tab):
    moldFrame = ttk.Frame(tab)
    moldFrame.grid(column=0, row=1)

    moldWeightL = ttk.Label(moldFrame, text="Weight of Mold (grams)")
    moldNumL = ttk.Label(moldFrame, text="Mold #")
    style = ttk.Style()
    style.configure("TCombobox", highlightthickness=2)
    style2 = ttk.Style()
    style2.configure("TEntry", highlightthickness=2) 
    moldWeightL.grid(column=0, row=0, sticky=(N,W), padx=(0, 10))
    moldNumL.grid(column=0, row=1, sticky=(N,E), padx=(0, 10), pady=(5, 0))

    moldWeightTV = StringVar()
    moldNumTV = StringVar()

    moldWeightE = ttk.Entry(moldFrame, textvariable= moldWeightTV, width=10, style="TEntry")
    moldWeightE.grid(column=1, row=0, sticky=(N,W), pady=(0, 5))
    moldNumCB = ttk.Combobox(moldFrame, textvariable= moldNumTV, width=7, style="TCombobox")
    moldNumCB.grid(column=1, row=1, sticky=(N,W), pady=(5, 0))

    return moldFrame, {"moldWeightE": moldWeightE, "moldNumCB": moldNumCB}

def setup_point_frame(tab):
    pointFrame = ttk.Frame(tab)
    pointFrame.grid(column=0, row=2, sticky=(N,W))

    pointL1 = ttk.Label(pointFrame, text="Point")
    pointL1.grid(column=0, row=1, sticky=(N,W), padx=(0, 10), pady=(5, 5))
    pointL2 = ttk.Label(pointFrame, text="Point")
    pointL2.grid(column=0, row=2, sticky=(N,W), pady=(5, 5))
    pointL3 = ttk.Label(pointFrame, text="Point")
    pointL3.grid(column=0, row=3, sticky=(N,W), pady=(5, 5))
    pointL4 = ttk.Label(pointFrame, text="Point")
    pointL4.grid(column=0, row=4, sticky=(N,W), pady=(5, 5))
    pointL5 = ttk.Label(pointFrame, text="Point")
    pointL5.grid(column=0, row=5, sticky=(N,W), pady=(5, 5))
    pointL6 = ttk.Label(pointFrame, text="Point")
    pointL6.grid(column=0, row=6, sticky=(N,W), pady=(5, 5))
    pointL7 = ttk.Label(pointFrame, text="Point")
    pointL7.grid(column=0, row=7, sticky=(N,W), pady=(5, 0))

    WoCSL = ttk.Label(pointFrame, text="   Weight of \n Compacted \n     Sample \n     (grams)")
    WoCSL.grid(column=1, row=0, sticky=(N,W), pady=(0, 10))

    WoCSLTV1 = StringVar()
    WoCSLTV2 = StringVar()
    WoCSLTV3 = StringVar()
    WoCSLTV4 = StringVar()
    WoCSLTV5 = StringVar()
    WoCSLTV6 = StringVar()
    WoCSLTV7 = StringVar()

    WoCSLE1 = ttk.Entry(pointFrame, textvariable= WoCSLTV1, width=10)
    WoCSLE1.grid(column=1, row=1, sticky=(N,W), padx=(0, 10))
    WoCSLE2 = ttk.Entry(pointFrame, textvariable= WoCSLTV2, width=10)
    WoCSLE2.grid(column=1, row=2, sticky=(N,W))
    WoCSLE3 = ttk.Entry(pointFrame, textvariable= WoCSLTV3, width=10)
    WoCSLE3.grid(column=1, row=3, sticky=(N,W))
    WoCSLE4 = ttk.Entry(pointFrame, textvariable= WoCSLTV4, width=10)
    WoCSLE4.grid(column=1, row=4, sticky=(N,W))
    WoCSLE5 = ttk.Entry(pointFrame, textvariable= WoCSLTV5, width=10)
    WoCSLE5.grid(column=1, row=5, sticky=(N,W))
    WoCSLE6 = ttk.Entry(pointFrame, textvariable= WoCSLTV6, width=10)
    WoCSLE6.grid(column=1, row=6, sticky=(N,W))
    WoCSLE7 = ttk.Entry(pointFrame, textvariable= WoCSLTV7, width=10)
    WoCSLE7.grid(column=1, row=7, sticky=(N,W))

    dishNumL = ttk.Label(pointFrame, text="Dish Number")
    dishNumL.grid(column=2, row=0, sticky=(S,W), pady=(0, 10))

    dishNumTV1 = StringVar()
    dishNumTV2 = StringVar()
    dishNumTV3 = StringVar()
    dishNumTV4 = StringVar()
    dishNumTV5 = StringVar()
    dishNumTV6 = StringVar()
    dishNumTV7 = StringVar()

    dishNumE1 = ttk.Entry(pointFrame, textvariable= dishNumTV1, width=10)
    dishNumE1.grid(column=2, row=1, sticky=(N,W), padx=(0, 10))
    dishNumE2 = ttk.Entry(pointFrame, textvariable= dishNumTV2, width=10)
    dishNumE2.grid(column=2, row=2, sticky=(N,W))
    dishNumE3 = ttk.Entry(pointFrame, textvariable= dishNumTV3, width=10)
    dishNumE3.grid(column=2, row=3, sticky=(N,W))
    dishNumE4 = ttk.Entry(pointFrame, textvariable= dishNumTV4, width=10)
    dishNumE4.grid(column=2, row=4, sticky=(N,W))
    dishNumE5 = ttk.Entry(pointFrame, textvariable= dishNumTV5, width=10)
    dishNumE5.grid(column=2, row=5, sticky=(N,W))
    dishNumE6 = ttk.Entry(pointFrame, textvariable= dishNumTV6, width=10)
    dishNumE6.grid(column=2, row=6, sticky=(N,W))
    dishNumE7 = ttk.Entry(pointFrame, textvariable= dishNumTV7, width=10)
    dishNumE7.grid(column=2, row=7, sticky=(N,W))

    WoDL = ttk.Label(pointFrame, text="   Weight of \n Dish (grams)")
    WoDL.grid(column=3, row=0, sticky=(S), pady=(0, 10))

    WoDTV1 = StringVar()
    WoDTV2 = StringVar()
    WoDTV3 = StringVar()
    WoDTV4 = StringVar()
    WoDTV5 = StringVar()
    WoDTV6 = StringVar()
    WoDTV7 = StringVar()

    WoDE1 = ttk.Entry(pointFrame, textvariable= WoDTV1, width=10)
    WoDE1.grid(column=3, row=1, sticky=(N,W), padx=(0, 10))
    WoDE2 = ttk.Entry(pointFrame, textvariable= WoDTV2, width=10)
    WoDE2.grid(column=3, row=2, sticky=(N,W))
    WoDE3 = ttk.Entry(pointFrame, textvariable= WoDTV3, width=10)
    WoDE3.grid(column=3, row=3, sticky=(N,W))
    WoDE4 = ttk.Entry(pointFrame, textvariable= WoDTV4, width=10)
    WoDE4.grid(column=3, row=4, sticky=(N,W))
    WoDE5 = ttk.Entry(pointFrame, textvariable= WoDTV5, width=10)
    WoDE5.grid(column=3, row=5, sticky=(N,W))
    WoDE6 = ttk.Entry(pointFrame, textvariable= WoDTV6, width=10)
    WoDE6.grid(column=3, row=6, sticky=(N,W))
    WoDE7 = ttk.Entry(pointFrame, textvariable= WoDTV7, width=10)
    WoDE7.grid(column=3, row=7, sticky=(N,W))

    WoDaWSL = ttk.Label(pointFrame, text="Weight of \n Dish and \n Wet Soil \n (grams)")
    WoDaWSL.grid(column=4, row=0, sticky=(S), pady=(0, 10))

    WoDaWSTV1 = StringVar()
    WoDaWSTV2 = StringVar()
    WoDaWSTV3 = StringVar()
    WoDaWSTV4 = StringVar()
    WoDaWSTV5 = StringVar()
    WoDaWSTV6 = StringVar()
    WoDaWSTV7 = StringVar()

    WoDaWSE1 = ttk.Entry(pointFrame, textvariable= WoDaWSTV1, width=10)
    WoDaWSE1.grid(column=4, row=1, sticky=(N,W), padx=(0, 10))
    WoDaWSE2 = ttk.Entry(pointFrame, textvariable= WoDaWSTV2, width=10)
    WoDaWSE2.grid(column=4, row=2, sticky=(N,W))
    WoDaWSE3 = ttk.Entry(pointFrame, textvariable= WoDaWSTV3, width=10)
    WoDaWSE3.grid(column=4, row=3, sticky=(N,W))
    WoDaWSE4 = ttk.Entry(pointFrame, textvariable= WoDaWSTV4, width=10)
    WoDaWSE4.grid(column=4, row=4, sticky=(N,W))
    WoDaWSE5 = ttk.Entry(pointFrame, textvariable= WoDaWSTV5, width=10)
    WoDaWSE5.grid(column=4, row=5, sticky=(N,W))
    WoDaWSE6 = ttk.Entry(pointFrame, textvariable= WoDaWSTV6, width=10)
    WoDaWSE6.grid(column=4, row=6, sticky=(N,W))
    WoDaWSE7 = ttk.Entry(pointFrame, textvariable= WoDaWSTV7, width=10)
    WoDaWSE7.grid(column=4, row=7, sticky=(N,W))

    WoDaDSL = ttk.Label(pointFrame, text="Weight of \n Dish and \n Dry Soil \n (grams)")
    WoDaDSL.grid(column=5, row=0, sticky=(S), pady=(0, 10))

    WoDaDSTV1 = StringVar()
    WoDaDSTV2 = StringVar()
    WoDaDSTV3 = StringVar()
    WoDaDSTV4 = StringVar()
    WoDaDSTV5 = StringVar()
    WoDaDSTV6 = StringVar()
    WoDaDSTV7 = StringVar()

    WoDaDSE1 = ttk.Entry(pointFrame, textvariable= WoDaDSTV1, width=10)
    WoDaDSE1.grid(column=5, row=1, sticky=(N,W))
    WoDaDSE2 = ttk.Entry(pointFrame, textvariable= WoDaDSTV2, width=10)
    WoDaDSE2.grid(column=5, row=2, sticky=(N,W))
    WoDaDSE3 = ttk.Entry(pointFrame, textvariable= WoDaDSTV3, width=10)
    WoDaDSE3.grid(column=5, row=3, sticky=(N,W))
    WoDaDSE4 = ttk.Entry(pointFrame, textvariable= WoDaDSTV4, width=10)
    WoDaDSE4.grid(column=5, row=4, sticky=(N,W))
    WoDaDSE5 = ttk.Entry(pointFrame, textvariable= WoDaDSTV5, width=10)
    WoDaDSE5.grid(column=5, row=5, sticky=(N,W))
    WoDaDSE6 = ttk.Entry(pointFrame, textvariable= WoDaDSTV6, width=10)
    WoDaDSE6.grid(column=5, row=6, sticky=(N,W))
    WoDaDSE7 = ttk.Entry(pointFrame, textvariable= WoDaDSTV7, width=10)
    WoDaDSE7.grid(column=5, row=7, sticky=(N,W))

    return pointFrame, {"WoCSLE1": WoCSLE1, 
        "WoCSLE2": WoCSLE2, "WoCSLE3": WoCSLE3,
        "WoCSLE4": WoCSLE4, "WoCSLE5": WoCSLE5,
        "WoCSLE6": WoCSLE6, "WoCSLE7": WoCSLE7,
        "dishNumE1": dishNumE1, "dishNumE2": dishNumE2,
        "dishNumE3": dishNumE3, "dishNumE4": dishNumE4, 
        "dishNumE5": dishNumE5, "dishNumE6": dishNumE6, 
        "dishNumE7": dishNumE7, "WoDE1": WoDE1, "WoDE2": WoDE2,
        "WoDE3": WoDE3, "WoDE4": WoDE4, "WoDE5": WoDE5, 
        "WoDE6": WoDE6, "WoDE7": WoDE7, "WoDaWSE1": WoDaWSE1, 
        "WoDaWSE2": WoDaWSE2, "WoDaWSE3": WoDaWSE3, 
        "WoDaWSE4": WoDaWSE4, "WoDaWSE5": WoDaWSE5, 
        "WoDaWSE6": WoDaWSE6, "WoDaWSE7": WoDaWSE7, 
        "WoDaDSE1": WoDaDSE1, "WoDaDSE2": WoDaDSE2, 
        "WoDaDSE3": WoDaDSE3, "WoDaDSE4": WoDaDSE4, 
        "WoDaDSE5": WoDaDSE5, "WoDaDSE6": WoDaDSE6, 
        "WoDaDSE7": WoDaDSE7}

def create_tab3(notebook):
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Proctor")

    dateCompletedFrame, dateCompleted_widgets = setup_date_completed_frame(tab3)
    dateCompletedFrame.grid(column=0, row=0, sticky=(N, W))

    contentContainer = ttk.Frame(tab3)
    contentContainer.grid(column=0, row=1, sticky=(N, S, E, W))

    tab3.rowconfigure(1, weight=1)
    tab3.columnconfigure(0, weight=1)

    centerFrame = ttk.Frame(contentContainer)
    centerFrame.grid(column=1, row=0, sticky=(N, S, E, W))

    contentContainer.columnconfigure(0, weight=1)
    contentContainer.columnconfigure(1, weight=0)
    contentContainer.columnconfigure(2, weight=1)

    moldFrame, moldFrame_widgets = setup_mold_frame(centerFrame)
    pointFrame, pointFrame_widgets = setup_point_frame(centerFrame)
    moldFrame.grid(column=0, row=0, pady=(10, 0), columnspan=5, sticky="")
    pointFrame.grid(column=0, row=1, pady=(10, 0), sticky=(N, S))

    tab3.widgets = {
        "dateCompleted": dateCompleted_widgets,
        "moldFrame": moldFrame_widgets,
        "pointFrame": pointFrame_widgets
    }

    return tab3

# Tab 4 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_main_frame(tab):
    mainFrame = ttk.Frame(tab)
    mainFrame.grid(column=1, row=1)

    TotalWeightL = ttk.Label(mainFrame, text="Total Weight")
    TotalWeightL.grid(column=0, row=1, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    OneHalfL = ttk.Label(mainFrame, text="1 1/2\"")
    OneHalfL.grid(column=0, row=2, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    OneL = ttk.Label(mainFrame, text="1\"")
    OneL.grid(column=0, row=3, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    ThreeFourthsL = ttk.Label(mainFrame, text="3/4\"")
    ThreeFourthsL.grid(column=0, row=4, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    ThreeEigthsL = ttk.Label(mainFrame, text="3/8\"")
    ThreeEigthsL.grid(column=0, row=5, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    NumFourL = ttk.Label(mainFrame, text="#4")
    NumFourL.grid(column=0, row=6, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    NumTenL = ttk.Label(mainFrame, text="#10")
    NumTenL.grid(column=0, row=7, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    gramsL = ttk.Label(mainFrame, text="(grams)")
    gramsL.grid(column=1, row=0, pady=(0, 10), sticky="")

    TotalWeightTV = StringVar()
    OneHalfTV = StringVar()
    OneTV = StringVar()
    ThreeFourthsTV = StringVar()
    ThreeEigthsTV = StringVar()
    NumFourTV = StringVar()
    NumTenTV = StringVar()

    TotalWeightE = ttk.Entry(mainFrame, textvariable= TotalWeightTV, width=10)
    TotalWeightE.grid(column=1, row=1, sticky=(N,W), pady=(3, 3))
    OneHalfE = ttk.Entry(mainFrame, textvariable= OneHalfTV, width=10)
    OneHalfE.grid(column=1, row=2, sticky=(N,W), pady=(3, 3))
    OneE = ttk.Entry(mainFrame, textvariable= OneTV, width=10)
    OneE.grid(column=1, row=3, sticky=(N,W), pady=(3, 3))
    ThreeFourthsE = ttk.Entry(mainFrame, textvariable= ThreeFourthsTV, width=10)
    ThreeFourthsE.grid(column=1, row=4, sticky=(N,W), pady=(3, 3))
    ThreeEigthsE = ttk.Entry(mainFrame, textvariable= ThreeEigthsTV, width=10)
    ThreeEigthsE.grid(column=1, row=5, sticky=(N,W), pady=(3, 3))
    NumFourE = ttk.Entry(mainFrame, textvariable= NumFourTV, width=10)
    NumFourE.grid(column=1, row=6, sticky=(N,W), pady=(3, 3))
    NumTenE = ttk.Entry(mainFrame, textvariable= NumTenTV, width=10)
    NumTenE.grid(column=1, row=7, sticky=(N,W), pady=(3, 3))

    FinesWeightL = ttk.Label(mainFrame, text="Fines Weight")
    FinesWeightL.grid(column=2, row=1, sticky=(N,E), padx=(20, 10))
    NumTwentyL = ttk.Label(mainFrame, text="#20")
    NumTwentyL.grid(column=2, row=2, sticky=(N,E), padx=(0, 10))
    NumFortyL = ttk.Label(mainFrame, text="#40")
    NumFortyL.grid(column=2, row=3, sticky=(N,E), padx=(0, 10))
    NumSixtyL = ttk.Label(mainFrame, text="#60")
    NumSixtyL.grid(column=2, row=4, sticky=(N,E), padx=(0, 10))
    NumEightyL = ttk.Label(mainFrame, text="#80")
    NumEightyL.grid(column=2, row=5, sticky=(N,E), padx=(0, 10))
    NumHundredL = ttk.Label(mainFrame, text="#100")
    NumHundredL.grid(column=2, row=6, sticky=(N,E), padx=(0, 10))
    NumTwoHundredL = ttk.Label(mainFrame, text="#200")
    NumTwoHundredL.grid(column=2, row=7, sticky=(N,E), padx=(0, 10))

    gramsL2 = ttk.Label(mainFrame, text="(grams)")
    gramsL2.grid(column=3, row=0, pady=(0, 10), sticky="")

    FinesWeightTV = StringVar()
    NumTwentyTV = StringVar()
    NumFortyTV = StringVar()
    NumSixtyTV = StringVar()
    NumEightyTV = StringVar()
    NumHundredTV = StringVar()
    NumTwoHundredTV = StringVar()

    FinesWeightE = ttk.Entry(mainFrame, textvariable= FinesWeightTV, width=10)
    FinesWeightE.grid(column=3, row=1, sticky=(N,W))
    NumTwentyE = ttk.Entry(mainFrame, textvariable= NumTwentyTV, width=10)
    NumTwentyE.grid(column=3, row=2, sticky=(N,W))
    NumFortyE = ttk.Entry(mainFrame, textvariable= NumFortyTV, width=10)
    NumFortyE.grid(column=3, row=3, sticky=(N,W))
    NumSixtyE = ttk.Entry(mainFrame, textvariable= NumSixtyTV, width=10)
    NumSixtyE.grid(column=3, row=4, sticky=(N,W))
    NumEightyE = ttk.Entry(mainFrame, textvariable= NumEightyTV, width=10)
    NumEightyE.grid(column=3, row=5, sticky=(N,W))
    NumHundredE = ttk.Entry(mainFrame, textvariable= NumHundredTV, width=10)
    NumHundredE.grid(column=3, row=6, sticky=(N,W))
    NumTwoHundredE = ttk.Entry(mainFrame, textvariable= NumTwoHundredTV, width=10)
    NumTwoHundredE.grid(column=3, row=7, sticky=(N,W))

    return mainFrame, {"TotalWeightE": TotalWeightE, 
        "OneHalfE": OneHalfE, "OneE": OneE, "ThreeFourthsE": ThreeFourthsE, 
        "ThreeEigthsE": ThreeEigthsE, "NumFourE": NumFourE, "NumTenE": NumTenE,
        "FinesWeightE": FinesWeightE, "NumTwentyE": NumTwentyE, "NumFortyE": NumFortyE,
        "NumSixtyE": NumSixtyE, "NumEightyE": NumEightyE, "NumHundredE": NumHundredE, 
        "NumTwoHundredE": NumTwoHundredE}

def create_tab4(notebook):
    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text="Gradation")
    
    tab4.columnconfigure(0, weight=1)
    tab4.columnconfigure(1, weight=0)
    tab4.columnconfigure(2, weight=1)

    tab4.rowconfigure(0, weight=1)
    tab4.rowconfigure(1, weight=0)
    tab4.rowconfigure(2, weight=1)

    mainFrame, mainFrame_widgets = setup_main_frame(tab4)
    mainFrame.grid(column=1, row=1, sticky="nsew")

    tab4.widgets = {
        "mainFrame": mainFrame_widgets
    }

    return tab4

# Tab 5 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_date_completed_frame2(tab):
    dateCompletedFrame = ttk.Frame(tab, padding=(20, 20, 0, 20))
    dateCompletedFrame.grid(column=0, row=0, sticky=(N,W), pady=(0, 20))

    style = ttk.Style()
    style.configure("TEntry", highlightthickness=2) 
    dateComL = ttk.Label(dateCompletedFrame, text="Date Completed")
    dateComL.grid(column=0, row=0, sticky=(N,W), padx=(0, 10))

    dateComTV = StringVar()

    dateComE = ttk.Entry(dateCompletedFrame, textvariable= dateComTV, width=9, style="TEntry")
    dateComE.grid(column=1, row=0)

    return dateCompletedFrame, {"dateComTV": dateComTV}

def setup_soak_unsoak_frame(tab):
    soakUnsoakFrame = ttk.Frame(tab)
    soakUnsoakFrame.grid(column=0, row=1, rowspan=3)

    zeroTwoFiveL = ttk.Label(soakUnsoakFrame, text="0.025", font=("Segoe UI", 8))
    zeroTwoFiveL.grid(column=0, row=1, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    zeroFiveZeroL = ttk.Label(soakUnsoakFrame, text="0.050", font=("Segoe UI", 8))
    zeroFiveZeroL.grid(column=0, row=2, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    zeroSevenFiveL = ttk.Label(soakUnsoakFrame, text="0.075", font=("Segoe UI", 8))
    zeroSevenFiveL.grid(column=0, row=3, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    oneZeroZeroL = ttk.Label(soakUnsoakFrame, text="0.100", font=("Segoe UI", 8))
    oneZeroZeroL.grid(column=0, row=4, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    oneFiveZeroL = ttk.Label(soakUnsoakFrame, text="0.150", font=("Segoe UI", 8))
    oneFiveZeroL.grid(column=0, row=5, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    twoZeroZeroL = ttk.Label(soakUnsoakFrame, text="0.200", font=("Segoe UI", 8))
    twoZeroZeroL.grid(column=0, row=6, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    twoFiveZeroL = ttk.Label(soakUnsoakFrame, text="0.250", font=("Segoe UI", 8))
    twoFiveZeroL.grid(column=0, row=7, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    threeZeroZeroL = ttk.Label(soakUnsoakFrame, text="0.300", font=("Segoe UI", 8))
    threeZeroZeroL.grid(column=0, row=8, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    threeFiveZeroL = ttk.Label(soakUnsoakFrame, text="0.350", font=("Segoe UI", 8))
    threeFiveZeroL.grid(column=0, row=9, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    fourZeroZeroL = ttk.Label(soakUnsoakFrame, text="0.400", font=("Segoe UI", 8))
    fourZeroZeroL.grid(column=0, row=10, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    fourFiveZeroL = ttk.Label(soakUnsoakFrame, text="0.450", font=("Segoe UI", 8))
    fourFiveZeroL.grid(column=0, row=11, sticky=(N,E), padx=(0, 10), pady=(3, 0))
    fiveZeroZeroL = ttk.Label(soakUnsoakFrame, text="0.500", font=("Segoe UI", 8))
    fiveZeroZeroL.grid(column=0, row=12, sticky=(N,E), padx=(0, 10), pady=(3, 0))

    unsoakedLoadL = ttk.Label(soakUnsoakFrame, text="Unsoaked \nLoad (lbs)", font=("Segoe UI", 8))
    unsoakedLoadL.grid(column=1, row=0, pady=(0, 5))

    zeroTwoFiveUTV = StringVar()
    zeroFiveZeroUTV = StringVar()
    zeroSevenFiveUTV = StringVar()
    oneZeroZeroUTV = StringVar()
    oneFiveZeroUTV = StringVar()
    twoZeroZeroUTV = StringVar()
    twoFiveZeroUTV = StringVar()
    threeZeroZeroUTV = StringVar()
    threeFiveZeroUTV = StringVar()
    fourZeroZeroUTV = StringVar()
    fourFiveZeroUTV = StringVar()
    fiveZeroZeroUTV = StringVar()

    zeroTwoFiveUE = ttk.Entry(soakUnsoakFrame, textvariable= zeroTwoFiveUTV, width=8, font=("Segoe UI", 8))
    zeroTwoFiveUE.grid(column=1, row=1, pady=(3, 3), padx=(0, 3))
    zeroFiveZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= zeroFiveZeroUTV, width=8, font=("Segoe UI", 8))
    zeroFiveZeroUE.grid(column=1, row=2, pady=(3, 3), padx=(0, 3))
    zeroSevenFiveUE = ttk.Entry(soakUnsoakFrame, textvariable= zeroSevenFiveUTV, width=8, font=("Segoe UI", 8))
    zeroSevenFiveUE.grid(column=1, row=3, pady=(3, 3), padx=(0, 3))
    oneZeroZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= oneZeroZeroUTV, width=8, font=("Segoe UI", 8))
    oneZeroZeroUE.grid(column=1, row=4, pady=(3, 3), padx=(0, 3))
    oneFiveZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= oneFiveZeroUTV, width=8, font=("Segoe UI", 8))
    oneFiveZeroUE.grid(column=1, row=5, pady=(3, 3), padx=(0, 3))
    twoZeroZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= twoZeroZeroUTV, width=8, font=("Segoe UI", 8))
    twoZeroZeroUE.grid(column=1, row=6, pady=(3, 3), padx=(0, 3))
    twoFiveZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= twoFiveZeroUTV, width=8, font=("Segoe UI", 8))
    twoFiveZeroUE.grid(column=1, row=7, pady=(3, 3), padx=(0, 3))
    threeZeroZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= threeZeroZeroUTV, width=8, font=("Segoe UI", 8))
    threeZeroZeroUE.grid(column=1, row=8, pady=(3, 3), padx=(0, 3))
    threeFiveZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= threeFiveZeroUTV, width=8, font=("Segoe UI", 8))
    threeFiveZeroUE.grid(column=1, row=9, pady=(3, 3), padx=(0, 3))
    fourZeroZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= fourZeroZeroUTV, width=8, font=("Segoe UI", 8))
    fourZeroZeroUE.grid(column=1, row=10, pady=(3, 3), padx=(0, 3))
    fourFiveZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= fourFiveZeroUTV, width=8, font=("Segoe UI", 8))
    fourFiveZeroUE.grid(column=1, row=11, pady=(3, 3), padx=(0, 3))
    fiveZeroZeroUE = ttk.Entry(soakUnsoakFrame, textvariable= fiveZeroZeroUTV, width=8, font=("Segoe UI", 8))
    fiveZeroZeroUE.grid(column=1, row=12, pady=(3, 3), padx=(0, 3))

    soakedLoadL = ttk.Label(soakUnsoakFrame, text="  Soaked \nLoad (lbs)", font=("Segoe UI", 8))
    soakedLoadL.grid(column=2, row=0, pady=(0, 5))

    zeroTwoFiveSTV = StringVar()
    zeroFiveZeroSTV = StringVar()
    zeroSevenFiveSTV = StringVar()
    oneZeroZeroSTV = StringVar()
    oneFiveZeroSTV = StringVar()
    twoZeroZeroSTV = StringVar()
    twoFiveZeroSTV = StringVar()
    threeZeroZeroSTV = StringVar()
    threeFiveZeroSTV = StringVar()
    fourZeroZeroSTV = StringVar()
    fourFiveZeroSTV = StringVar()
    fiveZeroZeroSTV = StringVar()

    zeroTwoFiveSE = ttk.Entry(soakUnsoakFrame, textvariable= zeroTwoFiveSTV, width=8, font=("Segoe UI", 8))
    zeroTwoFiveSE.grid(column=2, row=1, padx=(3, 0))
    zeroFiveZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= zeroFiveZeroSTV, width=8, font=("Segoe UI", 8))
    zeroFiveZeroSE.grid(column=2, row=2, padx=(3, 0))
    zeroSevenFiveSE = ttk.Entry(soakUnsoakFrame, textvariable= zeroSevenFiveSTV, width=8, font=("Segoe UI", 8))
    zeroSevenFiveSE.grid(column=2, row=3, padx=(3, 0))
    oneZeroZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= oneZeroZeroSTV, width=8, font=("Segoe UI", 8))
    oneZeroZeroSE.grid(column=2, row=4, padx=(3, 0))
    oneFiveZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= oneFiveZeroSTV, width=8, font=("Segoe UI", 8))
    oneFiveZeroSE.grid(column=2, row=5, padx=(3, 0))
    twoZeroZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= twoZeroZeroSTV, width=8, font=("Segoe UI", 8))
    twoZeroZeroSE.grid(column=2, row=6, padx=(3, 0))
    twoFiveZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= twoFiveZeroSTV, width=8, font=("Segoe UI", 8))
    twoFiveZeroSE.grid(column=2, row=7, padx=(3, 0))
    threeZeroZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= threeZeroZeroSTV, width=8, font=("Segoe UI", 8))
    threeZeroZeroSE.grid(column=2, row=8, padx=(3, 0))
    threeFiveZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= threeFiveZeroSTV, width=8, font=("Segoe UI", 8))
    threeFiveZeroSE.grid(column=2, row=9, padx=(3, 0))
    fourZeroZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= fourZeroZeroSTV, width=8, font=("Segoe UI", 8))
    fourZeroZeroSE.grid(column=2, row=10, padx=(3, 0))
    fourFiveZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= fourFiveZeroSTV, width=8, font=("Segoe UI", 8))
    fourFiveZeroSE.grid(column=2, row=11, padx=(3, 0))
    fiveZeroZeroSE = ttk.Entry(soakUnsoakFrame, textvariable= fiveZeroZeroSTV, width=8, font=("Segoe UI", 8))
    fiveZeroZeroSE.grid(column=2, row=12, padx=(3, 0))

    return soakUnsoakFrame, {"zeroTwoFiveUE": zeroTwoFiveUE, 
        "zeroFiveZeroUE": zeroFiveZeroUE, "zeroSevenFiveUE": zeroSevenFiveUE,
        "oneZeroZeroUE": oneZeroZeroUE, "oneFiveZeroUE": oneFiveZeroUE, 
        "twoZeroZeroUE": twoZeroZeroUE, "twoFiveZeroUE": twoFiveZeroUE, 
        "threeZeroZeroUE": threeZeroZeroUE, "threeFiveZeroUE": threeFiveZeroUE, 
        "fourZeroZeroUE": fourZeroZeroUE, "fourFiveZeroUE": fourFiveZeroUE, 
        "fiveZeroZeroUE": fiveZeroZeroUE, "zeroTwoFiveSE": zeroTwoFiveSE, 
        "zeroFiveZeroSE": zeroFiveZeroSE, "zeroSevenFiveSE": zeroSevenFiveSE, 
        "oneZeroZeroSE": oneZeroZeroSE, "oneFiveZeroSE": oneFiveZeroSE, 
        "twoZeroZeroSE": twoZeroZeroSE, "twoFiveZeroSE": twoFiveZeroSE, 
        "threeZeroZeroSE": threeZeroZeroSE, "threeFiveZeroSE": threeFiveZeroSE, 
        "fourZeroZeroSE": fourZeroZeroSE, "fourFiveZeroSE": fourFiveZeroSE, 
        "fiveZeroZeroSE": fiveZeroZeroSE}

def setup_weight_frame(tab):
    weightFrame = ttk.Frame(tab, padding=(20, 20, 0, 20))
    weightFrame.grid(column=1, row=0, columnspan=3, sticky=(N,W))

    WoMaWSL = ttk.Label(weightFrame, text="Weight of Mold & Wet Soil", font=("Segoe UI", 8))
    WoMaWSL.grid(column=0, row=1, sticky=(N,E), padx=(0, 5))
    WoML = ttk.Label(weightFrame, text="Weight of Mold (grams)", font=("Segoe UI", 8))
    WoML.grid(column=0, row=2, sticky=(N,E), padx=(0, 5))

    unsoakedML = ttk.Label(weightFrame, text="Unsoaked\n    Mold", font=("Segoe UI", 8))
    unsoakedML.grid(column=1, row=0, pady=(0, 10))

    WoMaWSTV1 = StringVar()
    WoMLTV1 = StringVar()

    WoMaWSE1 = ttk.Entry(weightFrame, textvariable= WoMaWSTV1, width=8, font=("Segoe UI", 8))
    WoMaWSE1.grid(column=1, row=1, pady=(0, 3), padx=(3, 3))
    WoMLE1 = ttk.Entry(weightFrame, textvariable= WoMLTV1, width=8, font=("Segoe UI", 8))
    WoMLE1.grid(column=1, row=2, pady=(3, 0), padx=(3, 3))

    soakedML = ttk.Label(weightFrame, text="Soaked\n  Mold", font=("Segoe UI", 8))
    soakedML.grid(column=2, row=0, pady=(0, 10))

    WoMaWSTV2 = StringVar()
    WoMLTV2 = StringVar()

    WoMaWSE2 = ttk.Entry(weightFrame, textvariable= WoMaWSTV2, width=8, font=("Segoe UI", 8))
    WoMaWSE2.grid(column=2, row=1, pady=(0, 3), padx=(3, 3))
    WoMLE2 = ttk.Entry(weightFrame, textvariable= WoMLTV2, width=8, font=("Segoe UI", 8))
    WoMLE2.grid(column=2, row=2, pady=(3, 0), padx=(3, 3))

    MoldAfterImmersionL = ttk.Label(weightFrame, text=" Mold After\n Immersion", font=("Segoe UI", 8))
    MoldAfterImmersionL.grid(column=3, row=0, pady=(0, 10))

    WoMaWSTV3 = StringVar()
    WoMLTV3 = StringVar()

    WoMaWSE3 = ttk.Entry(weightFrame, textvariable= WoMaWSTV3, width=8, font=("Segoe UI", 8))
    WoMaWSE3.grid(column=3, row=1, pady=(0, 3), padx=(3, 0))
    WoMLE3 = ttk.Entry(weightFrame, textvariable= WoMLTV3, width=8, font=("Segoe UI", 8))
    WoMLE3.grid(column=3, row=2, pady=(3, 0), padx=(3, 0))

    return weightFrame, {"WoMaWSE1": WoMaWSE1, 
        "WoMLE1": WoMLE1, "WoMaWSE2": WoMaWSE2, 
        "WoMLE2": WoMLE2, "WoMaWSE3": WoMaWSE3,
        "WoMLE3": WoMLE2}

def setup_reading_frame(tab):
    readingFrame = ttk.Frame(tab)
    readingFrame.grid(column=0, row=0, sticky=(N))

    RBIL = ttk.Label(readingFrame, text="Reading Before Immersion", font=("Segoe UI", 8))
    RBIL.grid(column=0, row=0)
    RAIL = ttk.Label(readingFrame, text="Reading After Immersion", font=("Segoe UI", 8))
    RAIL.grid(column=0, row=1)

    RBITV = StringVar()
    RAITV = StringVar()

    RBIE = ttk.Entry(readingFrame, textvariable= RBITV, width=8, font=("Segoe UI", 8))
    RBIE.grid(column=1, row=0, padx=(5, 0), pady=(0, 3))
    RAIE = ttk.Entry(readingFrame, textvariable= RAITV, width=8, font=("Segoe UI", 8))
    RAIE.grid(column=1, row=1, padx=(5, 0), pady=(3, 0))

    return readingFrame, {"RBIE": RBIE, "RAIE": RAIE}

def setup_blows_per_layer_frame(tab):
    blowsPerLayerFrame = ttk.Frame(tab)
    blowsPerLayerFrame.grid(column=1, row=0, sticky=(N), pady=(15, 0), padx=(30, 0))

    BPLL = ttk.Label(blowsPerLayerFrame, text="Blows Per Layer", font=("Segoe UI", 8))
    BPLL.grid(column=0, row=0)

    BPLTV = StringVar()

    BPLE = ttk.Entry(blowsPerLayerFrame, textvariable= BPLTV, width=8, font=("Segoe UI", 8))
    BPLE.grid(column=1, row=0, padx=(5, 0))

    return blowsPerLayerFrame, {"BPLE": BPLE}

def setup_moisture_frame(tab):
    moistureFrame = ttk.Frame(tab, padding=(0,0,0,10))
    moistureFrame.grid(column=1, row=2, sticky=(N))

    BeginMoistureUnL = ttk.Label(moistureFrame, text="Begin Moisture (unsoaked)", font=("Segoe UI", 8))
    BeginMoistureUnL.grid(column=0, row=1, sticky=(N,E), padx=(0, 5))
    EndMoistureUnL = ttk.Label(moistureFrame, text="End Moisture (unsoaked)", font=("Segoe UI", 8))
    EndMoistureUnL.grid(column=0, row=2, sticky=(N,E), padx=(0, 5))
    BeginMoistureSoL = ttk.Label(moistureFrame, text="Begin Moisture (soaked)", font=("Segoe UI", 8))
    BeginMoistureSoL.grid(column=0, row=3, sticky=(N,E), padx=(0, 5))
    EndMoistureSoL = ttk.Label(moistureFrame, text="End Moisture (soaked)", font=("Segoe UI", 8))
    EndMoistureSoL.grid(column=0, row=4, sticky=(N,E), padx=(0, 5))
    TopInchML = ttk.Label(moistureFrame, text="Top Inch Moisture", font=("Segoe UI", 8))
    TopInchML.grid(column=0, row=5, sticky=(N,E), padx=(0, 5))
    BucketML = ttk.Label(moistureFrame, text="Bucket Moisture", font=("Segoe UI", 8))
    BucketML.grid(column=0, row=6, sticky=(N,E), padx=(0, 5))

    cupL = ttk.Label(moistureFrame, text="Cup #", font=("Segoe UI", 8))
    cupL.grid(column=1, row=0)

    cupTV1 = StringVar()
    cupTV2 = StringVar()
    cupTV3 = StringVar()
    cupTV4 = StringVar()
    cupTV5 = StringVar()
    cupTV6 = StringVar()

    cupE1 = ttk.Entry(moistureFrame, textvariable= cupTV1, width=8, font=("Segoe UI", 8))
    cupE1.grid(column=1, row=1, pady=(0, 3), padx=(0, 3))
    cupE2 = ttk.Entry(moistureFrame, textvariable= cupTV2, width=8, font=("Segoe UI", 8))
    cupE2.grid(column=1, row=2, pady=(3, 3), padx=(0, 3))
    cupE3 = ttk.Entry(moistureFrame, textvariable= cupTV3, width=8, font=("Segoe UI", 8))
    cupE3.grid(column=1, row=3, pady=(3, 3), padx=(0, 3))
    cupE4 = ttk.Entry(moistureFrame, textvariable= cupTV4, width=8, font=("Segoe UI", 8))
    cupE4.grid(column=1, row=4, pady=(3, 3), padx=(0, 3))
    cupE5 = ttk.Entry(moistureFrame, textvariable= cupTV5, width=8, font=("Segoe UI", 8))
    cupE5.grid(column=1, row=5, pady=(3, 3), padx=(0, 3))
    cupE6 = ttk.Entry(moistureFrame, textvariable= cupTV6, width=8, font=("Segoe UI", 8))
    cupE6.grid(column=1, row=6, pady=(3, 0), padx=(0, 3))

    cupWeightL = ttk.Label(moistureFrame, text="Cup Weight\n    (grams)", font=("Segoe UI", 8))
    cupWeightL.grid(column=2, row=0, pady=(0, 5))

    cupWTV1 = StringVar()
    cupWTV2 = StringVar()
    cupWTV3 = StringVar()
    cupWTV4 = StringVar()
    cupWTV5 = StringVar()
    cupWTV6 = StringVar()

    cupWE1 = ttk.Entry(moistureFrame, textvariable= cupWTV1, width=8, font=("Segoe UI", 8))
    cupWE1.grid(column=2, row=1, padx=(3, 0))
    cupWE2 = ttk.Entry(moistureFrame, textvariable= cupWTV2, width=8, font=("Segoe UI", 8))
    cupWE2.grid(column=2, row=2, padx=(3, 0))
    cupWE3 = ttk.Entry(moistureFrame, textvariable= cupWTV3, width=8, font=("Segoe UI", 8))
    cupWE3.grid(column=2, row=3, padx=(3, 0))
    cupWE4 = ttk.Entry(moistureFrame, textvariable= cupWTV4, width=8, font=("Segoe UI", 8))
    cupWE4.grid(column=2, row=4, padx=(3, 0))
    cupWE5 = ttk.Entry(moistureFrame, textvariable= cupWTV5, width=8, font=("Segoe UI", 8))
    cupWE5.grid(column=2, row=5, padx=(3, 0))
    cupWE6 = ttk.Entry(moistureFrame, textvariable= cupWTV6, width=8, font=("Segoe UI", 8))
    cupWE6.grid(column=2, row=6, padx=(3, 0))

    wetWeightL = ttk.Label(moistureFrame, text="Wet Weight\n    (grams)", font=("Segoe UI", 8))
    wetWeightL.grid(column=3, row=0, pady=(0, 5))

    wetTV1 = StringVar()
    wetTV2 = StringVar()
    wetTV3 = StringVar()
    wetTV4 = StringVar()
    wetTV5 = StringVar()
    wetTV6 = StringVar()

    wetE1 = ttk.Entry(moistureFrame, textvariable= wetTV1, width=8, font=("Segoe UI", 8))
    wetE1.grid(column=3, row=1)
    wetE2 = ttk.Entry(moistureFrame, textvariable= wetTV2, width=8, font=("Segoe UI", 8))
    wetE2.grid(column=3, row=2)
    wetE3 = ttk.Entry(moistureFrame, textvariable= wetTV3, width=8, font=("Segoe UI", 8))
    wetE3.grid(column=3, row=3)
    wetE4 = ttk.Entry(moistureFrame, textvariable= wetTV4, width=8, font=("Segoe UI", 8))
    wetE4.grid(column=3, row=4)
    wetE5 = ttk.Entry(moistureFrame, textvariable= wetTV5, width=8, font=("Segoe UI", 8))
    wetE5.grid(column=3, row=5)
    wetE6 = ttk.Entry(moistureFrame, textvariable= wetTV6, width=8, font=("Segoe UI", 8))
    wetE6.grid(column=3, row=6)

    dryWeightL = ttk.Label(moistureFrame, text="Dry Weight\n   (grams)", font=("Segoe UI", 8))
    dryWeightL.grid(column=4, row=0, pady=(0, 5))

    dryTV1 = StringVar()
    dryTV2 = StringVar()
    dryTV3 = StringVar()
    dryTV4 = StringVar()
    dryTV5 = StringVar()
    dryTV6 = StringVar()

    dryE1 = ttk.Entry(moistureFrame, textvariable= dryTV1, width=8, font=("Segoe UI", 8))
    dryE1.grid(column=4, row=1)
    dryE2 = ttk.Entry(moistureFrame, textvariable= dryTV2, width=8, font=("Segoe UI", 8))
    dryE2.grid(column=4, row=2)
    dryE3 = ttk.Entry(moistureFrame, textvariable= dryTV3, width=8, font=("Segoe UI", 8))
    dryE3.grid(column=4, row=3)
    dryE4 = ttk.Entry(moistureFrame, textvariable= dryTV4, width=8, font=("Segoe UI", 8))
    dryE4.grid(column=4, row=4)
    dryE5 = ttk.Entry(moistureFrame, textvariable= dryTV5, width=8, font=("Segoe UI", 8))
    dryE5.grid(column=4, row=5)
    dryE6 = ttk.Entry(moistureFrame, textvariable= dryTV6, width=8, font=("Segoe UI", 8))
    dryE6.grid(column=4, row=6)

    return moistureFrame, {"cupE1": cupE1,
        "cupE2": cupE2, "cupE3": cupE3, 
        "cupE4": cupE4, "cupE5": cupE5, 
        "cupE6": cupE6, "cupWE1": cupWE1, 
        "cupWE2": cupWE2, "cupWE3": cupWE3, 
        "cupWE4": cupWE4, "cupWE5": cupWE5,
        "cupWE6": cupWE6, "wetE1": wetE1, 
        "wetE2": wetE2, "wetE3": wetE3, 
        "wetE4": wetE4, "wetE5": wetE5, 
        "wetE6": wetE6, "dryE1": dryE1, 
        "dryE2": dryE2, "dryE3": dryE3, 
        "dryE4": dryE4, "dryE5": dryE5, 
        "dryE6": dryE6}

def setup_plus_four_frame(tab):
    plusFourFrame = ttk.Labelframe(tab, text="Plus #4's", padding=(60, 0, 30, 20))
    plusFourFrame.grid(column=1, row=3)
    
    weightL = ttk.Label(plusFourFrame, text="Weight\n(grams)", font=("Segoe UI", 8))
    weightL.grid(column=1, row=0, pady=(0, 5))

    DryWeightAirL = ttk.Label(plusFourFrame, text="Dry Weight in Air", font=("Segoe UI", 8))
    DryWeightAirL.grid(column=0, row=1, padx=(0, 5))
    SSDWeightAirL = ttk.Label(plusFourFrame, text="SSD Weight in Air", font=("Segoe UI", 8))
    SSDWeightAirL.grid(column=0, row=2, padx=(0, 5))
    WeightWaterL = ttk.Label(plusFourFrame, text="Weight in Water", font=("Segoe UI", 8))
    WeightWaterL.grid(column=0, row=3, padx=(0, 5))

    DryWeightAirTV = StringVar()
    SSDWeightAirTV = StringVar()
    WeightWaterTV = StringVar()

    DryWeightAirE = ttk.Entry(plusFourFrame, textvariable= DryWeightAirTV, width=8, font=("Segoe UI", 8))
    DryWeightAirE.grid(column=1, row=1, pady=(0, 3))
    SSDWeightAirE = ttk.Entry(plusFourFrame, textvariable= SSDWeightAirTV, width=8, font=("Segoe UI", 8))
    SSDWeightAirE.grid(column=1, row=2, pady=(3, 3))
    WeightWaterE = ttk.Entry(plusFourFrame, textvariable= WeightWaterTV, width=8, font=("Segoe UI", 8))
    WeightWaterE.grid(column=1, row=3, pady=(3, 0))

    return plusFourFrame, {"DryWeightAirE": DryWeightAirE, 
        "SSDWeightAirE": SSDWeightAirE, "WeightWaterE": WeightWaterE}


def create_tab5(notebook):
    tab5 = ttk.Frame(notebook, padding=(20, 0, 0, 0))
    notebook.add(tab5, text="CBR")

    containerFrame = ttk.Frame(tab5, padding=(0, 0, 0, 10))
    containerFrame.grid(column=1, row=1)

    dateCompletedFrame, dateCompleted_widgets = setup_date_completed_frame2(tab5)
    soakUnsoakFrame, soakUnsoak_widgets = setup_soak_unsoak_frame(tab5)
    weightFrame, weightFrame_widgets = setup_weight_frame(tab5)
    readingFrame, readingFrame_widgets = setup_reading_frame(containerFrame)
    blowsPerLayerFrame, blowsPerLayer_widgets = setup_blows_per_layer_frame(containerFrame)
    moistureFrame, moistureFrame_widgets = setup_moisture_frame(tab5)
    plusFourFrame, plusFourFrame_widgets = setup_plus_four_frame(tab5)

    tab5.widgets = {
        "dateCompleted": dateCompleted_widgets,
        "soakUnsoak": soakUnsoak_widgets,
        "weightFrame": weightFrame_widgets,
        "readingFrame": readingFrame_widgets,
        "blowsPerLayer": blowsPerLayer_widgets,
        "moistureFrame": moistureFrame_widgets,
        "plusFour": plusFourFrame_widgets
    }

    return tab5