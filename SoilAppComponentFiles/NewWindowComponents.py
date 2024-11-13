from tkinter import *
from tkinter import ttk

# Tab 1 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setup_station_frame(tab):
    stationFrame = ttk.Frame(tab)
    stationFrame.grid(column=2, row=10, columnspan=3, sticky=(N, W), padx=(10, 0))
    StationL = ttk.Label(tab, text="Station")
    StationL.grid(column=0, row=10, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StationPlusL = ttk.Label(stationFrame, text="+")
    StationPlusL.grid(column=1, row=0, sticky=(N, W), pady=(3, 3), padx=(0, 0))
    StationE1 = ttk.Entry(stationFrame, font=("Segoe UI", 8), width=8)
    StationE2 = ttk.Entry(stationFrame, font=("Segoe UI", 8), width=8)
    StationE1.grid(column=0, row=0, sticky=(N, W), pady=(3, 3), padx=(10, 3))
    StationE2.grid(column=2, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))
    return stationFrame

def setup_start_end_frame(tab):
    startEndFrame = ttk.Frame(tab)
    startEndFrame.grid(column=0, row=13, columnspan=5, sticky=(N, W))
    StartL = ttk.Label(startEndFrame, text="Start")
    EndL1 = ttk.Label(startEndFrame, text="ft   End")
    EndL2 = ttk.Label(startEndFrame, text="ft")
    StartL.grid(column=0, row=0, sticky=(N, W), pady=(3, 3), padx=(20, 0))
    EndL1.grid(column=2, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))
    EndL2.grid(column=4, row=0, sticky=(N, W), pady=(3, 3), padx=(3, 0))
    StartE = ttk.Entry(startEndFrame, font=("Segoe UI", 8), width=7)
    EndE = ttk.Entry(startEndFrame, font=("Segoe UI", 8), width=7)
    StartE.grid(column=1, row=0, sticky=(N, W), pady = (3, 3), padx = (26, 0))
    EndE.grid(column=3, row=0, sticky=(N, W), pady = (3, 3), padx = (21, 0))
    return startEndFrame

def setup_dataRecieved_to_routeNum_frame(tab):
    dataRecievedRouteNumFrame = ttk.Frame(tab)
    dataRecievedRouteNumFrame.grid(column=0, row=1, columnspan=5, rowspan=6)
    DataRecievedL = ttk.Label(dataRecievedRouteNumFrame, text="Data Received")
    DataSampledL = ttk.Label(dataRecievedRouteNumFrame, text="Data Sampled")
    DataCompletedL = ttk.Label(dataRecievedRouteNumFrame, text="Date Completed")
    ProjectNumL = ttk.Label(dataRecievedRouteNumFrame, text="Project #")
    PlantNumL = ttk.Label(dataRecievedRouteNumFrame, text="Plant #")
    RouteNumL = ttk.Label(dataRecievedRouteNumFrame, text="Route #")
    DataRecievedL.grid(column=0, row=1, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    DataSampledL.grid(column=0, row=2, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    DataCompletedL.grid(column=0, row=3, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    ProjectNumL.grid(column=0, row=4, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    PlantNumL.grid(column=0, row=5, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    RouteNumL.grid(column=0, row=6, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    DataRecievedE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    DataSampledE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    DataCompletedE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    ProjectNumE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    PlantNumE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    RouteNumE = ttk.Entry(dataRecievedRouteNumFrame, font=("Segoe UI", 8))
    DataRecievedE.grid(column=2, row=1, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataSampledE.grid(column=2, row=2, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    DataCompletedE.grid(column=2, row=3, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    ProjectNumE.grid(column=2, row=4, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    PlantNumE.grid(column=2, row=5, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    RouteNumE.grid(column=2, row=6, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (6, 0))
    return dataRecievedRouteNumFrame

def setup_city_county_frame(tab):
    cityCountyFrame = ttk.Frame(tab)
    cityCountyFrame.grid(column=0, row=7, columnspan=5, sticky=(N,W))
    CityOrCountyL = ttk.Label(cityCountyFrame, text="City or County")
    CityOrCountyL.grid(column=0, row=7, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    CityOrCountyCB = ttk.Combobox(cityCountyFrame, width = 17)
    CityOrCountyCB.grid(column = 2, row = 7, sticky=(N, W), pady = (3, 3), padx = (21, 0))
    return cityCountyFrame

def setup_fieldSample_to_submitted_frame(tab):
    fieldSampleSubmittedFrame = ttk.Frame(tab)
    fieldSampleSubmittedFrame.grid(column=0, row=8, columnspan=5, rowspan=2, sticky=(N,W))
    FieldSampleL = ttk.Label(fieldSampleSubmittedFrame, text="Field Sample #")
    SubmittedByL = ttk.Label(fieldSampleSubmittedFrame, text="Submitted By")
    FieldSampleL.grid(column=0, row=8, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    SubmittedByL.grid(column=0, row=9, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    FieldSampleE = ttk.Entry(fieldSampleSubmittedFrame, font=("Segoe UI", 8))
    SubmittedByE = ttk.Entry(fieldSampleSubmittedFrame, font=("Segoe UI", 8))
    FieldSampleE.grid(column=2, row=8, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (21, 0))
    SubmittedByE.grid(column=2, row=9, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (21, 0))
    return fieldSampleSubmittedFrame

def setup_sampleLoc_to_structureB_frame(tab):
    sampleLocStructureBFrame = ttk.Frame(tab)
    sampleLocStructureBFrame.grid(column=0, row=11, columnspan=5, rowspan=2, sticky=(N,W))
    SampleLocationL = ttk.Label(sampleLocStructureBFrame, text="Sample Location")
    StructureBoringL = ttk.Label(sampleLocStructureBFrame, text="Structure/Boring")
    SampleLocationL.grid(column=0, row=11, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    StructureBoringL.grid(column=0, row=12, columnspan=2, sticky=(N, W), pady = (3, 3), padx = (20, 0))
    SampleLocationE = ttk.Entry(sampleLocStructureBFrame, font=("Segoe UI", 8))
    StructureBoringE = ttk.Entry(sampleLocStructureBFrame, font=("Segoe UI", 8))
    SampleLocationE.grid(column=2, row=11, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    StructureBoringE.grid(column=2, row=12, columnspan=3, sticky=(N, W), pady = (3, 3), padx = (10, 0))
    return sampleLocStructureBFrame

def setup_material_radio_buttons_frame(tab):
    materialRadioButtonsFrame = ttk.Frame(tab)
    materialRadioButtonsFrame.grid(column=0, row=14, columnspan=5, rowspan=2, sticky=(N,W))
    innerMaterialRadioBFrame = ttk.Frame(materialRadioButtonsFrame)
    innerMaterialRadioBFrame.grid(column = 2, row = 0, columnspan = 3, sticky = (N, W))
    MaterialL = ttk.Label(materialRadioButtonsFrame, text="Material")
    MaterialL.grid(column=0, row=0, columnspan=2, sticky=(N, W), pady = (10, 0), padx = (20, 0))
    style = ttk.Style()
    style.configure("Custom.TRadiobutton", font=("Segoe UI", 8), padding=(0,0))
    SoilRB = ttk.Radiobutton(innerMaterialRadioBFrame, value=0,text = "SOIL", style="Custom.TRadiobutton")
    CMARB = ttk.Radiobutton(innerMaterialRadioBFrame, value=1, text = "CMA", style="Custom.TRadiobutton")
    OtheRB = ttk.Radiobutton(innerMaterialRadioBFrame, value=2,text = "OTHER", style="Custom.TRadiobutton")
    AggregatRB = ttk.Radiobutton(materialRadioButtonsFrame, value=3,text = "AGGREGATE", style="Custom.TRadiobutton")
    ProficienRB = ttk.Radiobutton(materialRadioButtonsFrame, value=4,text = "PROFICIENCY", style="Custom.TRadiobutton")
    SoilRB.grid(column = 0, row = 0, sticky = (N, W), padx = (10, 0))
    CMARB.grid(column = 1, row = 0, sticky = (N, W), padx = (15, 0))
    OtheRB.grid(column = 2, row = 0, sticky = (N, W), padx = (15, 0))
    AggregatRB.grid(column = 2, row = 1, sticky = (N, W), padx = (10, 0))
    ProficienRB.grid(column = 3, row = 1, sticky = (N, W), padx = (10, 0))
    return materialRadioButtonsFrame

def setup_material_desc_frame(tab):
    materialDescFrame = ttk.Frame(tab)
    materialDescFrame.grid(column = 0, row = 16, columnspan = 5, rowspan = 3, sticky = (N, W))
    MaterialDescriptionL = ttk.Label(materialDescFrame, text="Material\nDescription")
    MaterialDescriptionL.grid(column=0, row=0, columnspan=2, sticky=(N, W), pady = (15, 0), padx = (20, 0))
    materialDescT = Text(materialDescFrame, height = 5, width = 20, font = ("Segoe UI", 8))
    materialDescT.grid(column = 2, row = 0, sticky = (N, W), padx=(38, 0))
    return materialDescFrame

def setup_time_charge_info_frame(tab):
    TimeChargeInfoFrame = ttk.Frame(tab)
    TimeChargeInfoFrame.grid(column = 6, row = 2, rowspan = 5, sticky = (N, W), padx = (60, 0))
    TimeChargeInfoTopFrame = ttk.Frame(tab)
    TimeChargeInfoTopFrame.grid(column=6, row=1, sticky=(N,W), padx=(60, 0))
    TimeChargeInfoL = ttk.Label(TimeChargeInfoTopFrame, text = "TIME CHARGE INFORMATION")
    UPCCodeL = ttk.Label(TimeChargeInfoFrame, text = "UPC Code")
    DepartmentCodeL = ttk.Label(TimeChargeInfoFrame, text = "Department Code")
    TaskCodeL = ttk.Label(TimeChargeInfoFrame, text = "Task Code")
    ActivityCodeL = ttk.Label(TimeChargeInfoFrame, text = "Activity Code")
    TimeChargeInfoL.grid(column = 0, row = 0, sticky=(N, W), pady = (0, 5), padx = (35, 0))
    UPCCodeL.grid(column = 0, row = 2, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    DepartmentCodeL.grid(column = 0, row = 3, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    TaskCodeL.grid(column = 0, row = 4, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    ActivityCodeL.grid(column = 0, row = 5, sticky=(N, W), pady = (3, 3), padx = (0, 5))
    UPCCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    DepartmentCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    TaskCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    ActivityCodeE = ttk.Entry(TimeChargeInfoFrame, font=("Segoe UI", 8))
    UPCCodeE.grid(column = 1, row = 2, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    DepartmentCodeE.grid(column = 1, row = 3, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    TaskCodeE.grid(column = 1, row = 4, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    ActivityCodeE.grid(column = 1, row = 5, sticky=(N, W), pady = (3, 3), padx = (5, 0))
    return TimeChargeInfoFrame

def setup_tests_required_frame(tab):
    TestsRequiredFrame = ttk.Frame(tab)
    TestsRequiredFrame.grid(column = 6, row = 7, rowspan = 6, sticky = (N, W), padx = (60, 0))
    TestsRequiredL = ttk.Label(TestsRequiredFrame, text = "Tests Required")
    TestsRequiredL.grid(column = 0, row = 0, sticky=(N, W), padx = (0, 22))
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
    classificatioC.grid(column = 1, row = 0, sticky = (N, W))
    ProctorC.grid(column = 1, row = 1, sticky = (N, W))
    CaliC.grid(column = 1, row = 2, sticky = (N, W))
    UnconC.grid(column = 1, row = 3, sticky = (N, W))
    SoilResC.grid(column = 1, row = 4, sticky = (N, W))
    pHC.grid(column = 1, row = 5, sticky = (N, W))
    return TestsRequiredFrame

def setup_test_title_frame(tab):
    TestTitleFrame = ttk.Frame(tab)
    TestTitleFrame.grid(column = 6, row = 14, rowspan = 2, sticky = (N, W), padx = (60, 0))
    TestedByL = ttk.Label(TestTitleFrame, text = "Tested by:")
    TitleL = ttk.Label(TestTitleFrame, text = "Title:")
    TestedByL.grid(column = 0, row = 0, sticky = (N, W), pady = (0, 3))
    TitleL.grid(column = 0, row = 1, sticky = (N, W), pady = (3, 0))
    TestedByCB = ttk.Combobox(TestTitleFrame, width = 17)
    TitleCB = ttk.Combobox(TestTitleFrame, width = 17)
    TestedByCB.grid(column = 1, row = 0, sticky=(N, W), padx = (49, 0))
    TitleCB.grid(column = 1, row = 1, sticky=(N, W), padx = (49, 0))
    return TestTitleFrame

def setup_remarks_frame(tab):
    RemarksFrame = ttk.Frame(tab)
    RemarksFrame.grid(column = 6, row = 16, rowspan = 2, sticky = (N, W), padx = (60, 0), pady = (30, 0))
    RemarksL = ttk.Label(RemarksFrame, text = "Remarks")
    RemarksL.grid(column = 0, row = 0, sticky = (N, W), pady = (20, 0))
    RemarksT = Text(RemarksFrame, height = 5, width = 20, font = ("Segoe UI", 8))
    RemarksT.grid(column = 1, row = 0, sticky = (N, W), padx = (57, 0), pady = (0, 20))
    return RemarksFrame

def create_tab1(notebook):
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Details")

    stationFrame = setup_station_frame(tab1)
    startEndFrame = setup_start_end_frame(tab1)
    dataRecievedRouteNumFrame = setup_dataRecieved_to_routeNum_frame(tab1)
    cityCountyFrame = setup_city_county_frame(tab1)
    fieldSampleSubmittedFrame = setup_fieldSample_to_submitted_frame(tab1)
    sampleLocStructureBFrame = setup_sampleLoc_to_structureB_frame(tab1)
    materialRadioButtonsFrame = setup_material_radio_buttons_frame(tab1)
    materialDescFrame = setup_material_desc_frame(tab1)
    TimeChargeInfoFrame = setup_time_charge_info_frame(tab1)
    TestsRequiredFrame = setup_tests_required_frame(tab1)
    TestTitleFrame = setup_test_title_frame(tab1)
    RemarksFrame = setup_remarks_frame(tab1)

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
    CupLiqE = ttk.Entry(atterbergFrame, width=10)
    CupPlasE = ttk.Entry(atterbergFrame, width=10)
    CupWLiqE = ttk.Entry(atterbergFrame, width=10)
    CupWPlasE = ttk.Entry(atterbergFrame, width=10)
    WetLiqE = ttk.Entry(atterbergFrame, width=10)
    WetPlasE = ttk.Entry(atterbergFrame, width=10)
    DryLiq = ttk.Entry(atterbergFrame, width=10)
    DryPlas = ttk.Entry(atterbergFrame, width=10)
    BlowsE = ttk.Entry(atterbergFrame, width=10)
    CupLiqE.grid(column=1, row=1)
    CupPlasE.grid(column=2, row=1)
    CupWLiqE.grid(column=1, row=2)
    CupWPlasE.grid(column=2, row=2)
    WetLiqE.grid(column=1, row=3)
    WetPlasE.grid(column=2, row=3)
    DryLiq.grid(column=1, row=4)
    DryPlas.grid(column=2, row=4)
    BlowsE.grid(column=1, row=5)
    firstBool = StringVar(value="firstOff")
    firstC = Checkbutton(
        atterbergFrame,
        onvalue="firstOn",
        offvalue="firstOff",
        variable=firstBool
    )
    secondBool = StringVar(value="secondOff")
    secondC = Checkbutton(
        atterbergFrame,
        onvalue="secondOn",
        offvalue="secondOff",
        variable=secondBool
    )
    firstC.grid(column=1, row=6)
    secondC.grid(column=2, row=6)
    return atterbergFrame

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
    cupNumE = ttk.Entry(fieldMoistureFrame, width=10)
    cupWeightE = ttk.Entry(fieldMoistureFrame, width=10)
    wetWeightE = ttk.Entry(fieldMoistureFrame, width=10)
    dryWeightE = ttk.Entry(fieldMoistureFrame, width=10)
    fieldMoistE = ttk.Entry(fieldMoistureFrame, width=10)
    cupNumE.grid(column=1, row=0, sticky=(N,W), pady=(0,3), padx=(7, 0))
    cupWeightE.grid(column=1, row=1, sticky=(N,W), pady=(3,3), padx=(7, 0))
    wetWeightE.grid(column=1, row=2, sticky=(N,W), pady=(3,3), padx=(7, 0))
    dryWeightE.grid(column=1, row=3, sticky=(N,W), pady=(3,3), padx=(7, 0))
    fieldMoistE.grid(column=1, row=4, sticky=(N,W), pady=(9,0), padx=(7, 0))
    return fieldMoistureFrame

def create_tab2(notebook):
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Atterberg")
    tab2.grid_rowconfigure(0, weight=1)
    tab2.grid_rowconfigure(1, weight=0)
    tab2.grid_rowconfigure(2, weight=1)

    tab2.grid_columnconfigure(0, weight=1)
    tab2.grid_columnconfigure(1, weight=0)
    tab2.grid_columnconfigure(2, weight=1)

    atterbergFrame = setup_atterberg_Frame(tab2)
    fieldMoistureFrame = setup_field_moisture_frame(tab2)

    return tab2