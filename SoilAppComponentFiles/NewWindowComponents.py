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

# Tab 3 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_date_completed_frame(tab):
    dateCompletedFrame = ttk.Frame(tab, padding=(20, 20, 20, 20))
    dateCompletedFrame.grid(column=0, row=0, sticky=(N,W))
    style = ttk.Style()
    style.configure("TEntry", highlightthickness=2) 
    dateComL = ttk.Label(dateCompletedFrame, text="Date Completed")
    dateComL.grid(column=0, row=0, sticky=(N,W), padx=(0, 10))
    dateComE = ttk.Entry(dateCompletedFrame, width=10, style="TEntry")
    dateComE.grid(column=1, row=0)
    return dateCompletedFrame

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
    moldWeightE = ttk.Entry(moldFrame, width=10, style="TEntry")
    moldWeightE.grid(column=1, row=0, sticky=(N,W), pady=(0, 5))
    moldNumCB = ttk.Combobox(moldFrame, width=7, style="TCombobox")
    moldNumCB.grid(column=1, row=1, sticky=(N,W), pady=(5, 0))
    return moldFrame

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
    WoCSLE1 = ttk.Entry(pointFrame, width=10)
    WoCSLE1.grid(column=1, row=1, sticky=(N,W), padx=(0, 10))
    WoCSLE2 = ttk.Entry(pointFrame, width=10)
    WoCSLE2.grid(column=1, row=2, sticky=(N,W))
    WoCSLE3 = ttk.Entry(pointFrame, width=10)
    WoCSLE3.grid(column=1, row=3, sticky=(N,W))
    WoCSLE4 = ttk.Entry(pointFrame, width=10)
    WoCSLE4.grid(column=1, row=4, sticky=(N,W))
    WoCSLE5 = ttk.Entry(pointFrame, width=10)
    WoCSLE5.grid(column=1, row=5, sticky=(N,W))
    WoCSLE6 = ttk.Entry(pointFrame, width=10)
    WoCSLE6.grid(column=1, row=6, sticky=(N,W))
    WoCSLE7 = ttk.Entry(pointFrame, width=10)
    WoCSLE7.grid(column=1, row=7, sticky=(N,W))

    dishNumL = ttk.Label(pointFrame, text="Dish Number")
    dishNumL.grid(column=2, row=0, sticky=(S,W), pady=(0, 10))
    dishNumE1 = ttk.Entry(pointFrame, width=10)
    dishNumE1.grid(column=2, row=1, sticky=(N,W), padx=(0, 10))
    dishNumE2 = ttk.Entry(pointFrame, width=10)
    dishNumE2.grid(column=2, row=2, sticky=(N,W))
    dishNumE3 = ttk.Entry(pointFrame, width=10)
    dishNumE3.grid(column=2, row=3, sticky=(N,W))
    dishNumE4 = ttk.Entry(pointFrame, width=10)
    dishNumE4.grid(column=2, row=4, sticky=(N,W))
    dishNumE5 = ttk.Entry(pointFrame, width=10)
    dishNumE5.grid(column=2, row=5, sticky=(N,W))
    dishNumE6 = ttk.Entry(pointFrame, width=10)
    dishNumE6.grid(column=2, row=6, sticky=(N,W))
    dishNumE7 = ttk.Entry(pointFrame, width=10)
    dishNumE7.grid(column=2, row=7, sticky=(N,W))

    WoDL = ttk.Label(pointFrame, text="   Weight of \n Dish (grams)")
    WoDL.grid(column=3, row=0, sticky=(S), pady=(0, 10))
    WoDE1 = ttk.Entry(pointFrame, width=10)
    WoDE1.grid(column=3, row=1, sticky=(N,W), padx=(0, 10))
    WoDE2 = ttk.Entry(pointFrame, width=10)
    WoDE2.grid(column=3, row=2, sticky=(N,W))
    WoDE3 = ttk.Entry(pointFrame, width=10)
    WoDE3.grid(column=3, row=3, sticky=(N,W))
    WoDE4 = ttk.Entry(pointFrame, width=10)
    WoDE4.grid(column=3, row=4, sticky=(N,W))
    WoDE5 = ttk.Entry(pointFrame, width=10)
    WoDE5.grid(column=3, row=5, sticky=(N,W))
    WoDE6 = ttk.Entry(pointFrame, width=10)
    WoDE6.grid(column=3, row=6, sticky=(N,W))
    WoDE7 = ttk.Entry(pointFrame, width=10)
    WoDE7.grid(column=3, row=7, sticky=(N,W))

    WoDaWSL = ttk.Label(pointFrame, text="Weight of \n Dish and \n Wet Soil \n (grams)")
    WoDaWSL.grid(column=4, row=0, sticky=(S), pady=(0, 10))
    WoDaWSE1 = ttk.Entry(pointFrame, width=10)
    WoDaWSE1.grid(column=4, row=1, sticky=(N,W), padx=(0, 10))
    WoDaWSE2 = ttk.Entry(pointFrame, width=10)
    WoDaWSE2.grid(column=4, row=2, sticky=(N,W))
    WoDaWSE3 = ttk.Entry(pointFrame, width=10)
    WoDaWSE3.grid(column=4, row=3, sticky=(N,W))
    WoDaWSE4 = ttk.Entry(pointFrame, width=10)
    WoDaWSE4.grid(column=4, row=4, sticky=(N,W))
    WoDaWSE5 = ttk.Entry(pointFrame, width=10)
    WoDaWSE5.grid(column=4, row=5, sticky=(N,W))
    WoDaWSE6 = ttk.Entry(pointFrame, width=10)
    WoDaWSE6.grid(column=4, row=6, sticky=(N,W))
    WoDaWSE7 = ttk.Entry(pointFrame, width=10)
    WoDaWSE7.grid(column=4, row=7, sticky=(N,W))

    WoDaDSL = ttk.Label(pointFrame, text="Weight of \n Dish and \n Dry Soil \n (grams)")
    WoDaDSL.grid(column=5, row=0, sticky=(S), pady=(0, 10))
    WoDaDSE1 = ttk.Entry(pointFrame, width=10)
    WoDaDSE1.grid(column=5, row=1, sticky=(N,W))
    WoDaDSE2 = ttk.Entry(pointFrame, width=10)
    WoDaDSE2.grid(column=5, row=2, sticky=(N,W))
    WoDaDSE3 = ttk.Entry(pointFrame, width=10)
    WoDaDSE3.grid(column=5, row=3, sticky=(N,W))
    WoDaDSE4 = ttk.Entry(pointFrame, width=10)
    WoDaDSE4.grid(column=5, row=4, sticky=(N,W))
    WoDaDSE5 = ttk.Entry(pointFrame, width=10)
    WoDaDSE5.grid(column=5, row=5, sticky=(N,W))
    WoDaDSE6 = ttk.Entry(pointFrame, width=10)
    WoDaDSE6.grid(column=5, row=6, sticky=(N,W))
    WoDaDSE7 = ttk.Entry(pointFrame, width=10)
    WoDaDSE7.grid(column=5, row=7, sticky=(N,W))

    return pointFrame

def create_tab3(notebook):
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Proctor")

    dateCompletedFrame = setup_date_completed_frame(tab3)
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

    moldFrame = setup_mold_frame(centerFrame)
    pointFrame = setup_point_frame(centerFrame)
    moldFrame.grid(column=0, row=0, pady=(10, 0), columnspan=5, sticky="")
    pointFrame.grid(column=0, row=1, pady=(10, 0), sticky=(N, S))

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

    TotalWeightE = ttk.Entry(mainFrame, width=10)
    TotalWeightE.grid(column=1, row=1, sticky=(N,W), pady=(3, 3))
    OneHalfE = ttk.Entry(mainFrame, width=10)
    OneHalfE.grid(column=1, row=2, sticky=(N,W), pady=(3, 3))
    OneE = ttk.Entry(mainFrame, width=10)
    OneE.grid(column=1, row=3, sticky=(N,W), pady=(3, 3))
    ThreeFourthsE = ttk.Entry(mainFrame, width=10)
    ThreeFourthsE.grid(column=1, row=4, sticky=(N,W), pady=(3, 3))
    ThreeEigthsE = ttk.Entry(mainFrame, width=10)
    ThreeEigthsE.grid(column=1, row=5, sticky=(N,W), pady=(3, 3))
    NumFourE = ttk.Entry(mainFrame, width=10)
    NumFourE.grid(column=1, row=6, sticky=(N,W), pady=(3, 3))
    NumTenE = ttk.Entry(mainFrame, width=10)
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

    FinesWeightE = ttk.Entry(mainFrame, width=10)
    FinesWeightE.grid(column=3, row=1, sticky=(N,W))
    NumTwentyE = ttk.Entry(mainFrame, width=10)
    NumTwentyE.grid(column=3, row=2, sticky=(N,W))
    NumFortyE = ttk.Entry(mainFrame, width=10)
    NumFortyE.grid(column=3, row=3, sticky=(N,W))
    NumSixtyE = ttk.Entry(mainFrame, width=10)
    NumSixtyE.grid(column=3, row=4, sticky=(N,W))
    NumEightyE = ttk.Entry(mainFrame, width=10)
    NumEightyE.grid(column=3, row=5, sticky=(N,W))
    NumHundredE = ttk.Entry(mainFrame, width=10)
    NumHundredE.grid(column=3, row=6, sticky=(N,W))
    NumTwoHundredE = ttk.Entry(mainFrame, width=10)
    NumTwoHundredE.grid(column=3, row=7, sticky=(N,W))
    return mainFrame

def create_tab4(notebook):
    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text="Gradation")
    
    tab4.columnconfigure(0, weight=1)
    tab4.columnconfigure(1, weight=0)
    tab4.columnconfigure(2, weight=1)

    tab4.rowconfigure(0, weight=1)
    tab4.rowconfigure(1, weight=0)
    tab4.rowconfigure(2, weight=1)

    mainFrame = setup_main_frame(tab4)
    mainFrame.grid(column=1, row=1, sticky="nsew")

    return tab4

# Tab 5 functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def setup_date_completed_frame2(tab):
    dateCompletedFrame = ttk.Frame(tab, padding=(20, 20, 0, 20))
    dateCompletedFrame.grid(column=0, row=0, sticky=(N,W), pady=(0, 20))
    style = ttk.Style()
    style.configure("TEntry", highlightthickness=2) 
    dateComL = ttk.Label(dateCompletedFrame, text="Date Completed")
    dateComL.grid(column=0, row=0, sticky=(N,W), padx=(0, 10))
    dateComE = ttk.Entry(dateCompletedFrame, width=9, style="TEntry")
    dateComE.grid(column=1, row=0)
    return dateCompletedFrame

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

    zeroTwoFiveUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroTwoFiveUE.grid(column=1, row=1, pady=(3, 3), padx=(0, 3))
    zeroFiveZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroFiveZeroUE.grid(column=1, row=2, pady=(3, 3), padx=(0, 3))
    zeroSevenFiveUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroSevenFiveUE.grid(column=1, row=3, pady=(3, 3), padx=(0, 3))
    oneZeroZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    oneZeroZeroUE.grid(column=1, row=4, pady=(3, 3), padx=(0, 3))
    oneFiveZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    oneFiveZeroUE.grid(column=1, row=5, pady=(3, 3), padx=(0, 3))
    twoZeroZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    twoZeroZeroUE.grid(column=1, row=6, pady=(3, 3), padx=(0, 3))
    twoFiveZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    twoFiveZeroUE.grid(column=1, row=7, pady=(3, 3), padx=(0, 3))
    threeZeroZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    threeZeroZeroUE.grid(column=1, row=8, pady=(3, 3), padx=(0, 3))
    threeFiveZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    threeFiveZeroUE.grid(column=1, row=9, pady=(3, 3), padx=(0, 3))
    fourZeroZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fourZeroZeroUE.grid(column=1, row=10, pady=(3, 3), padx=(0, 3))
    fourFiveZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fourFiveZeroUE.grid(column=1, row=11, pady=(3, 3), padx=(0, 3))
    fiveZeroZeroUE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fiveZeroZeroUE.grid(column=1, row=12, pady=(3, 3), padx=(0, 3))

    soakedLoadL = ttk.Label(soakUnsoakFrame, text="  Soaked \nLoad (lbs)", font=("Segoe UI", 8))
    soakedLoadL.grid(column=2, row=0, pady=(0, 5))

    zeroTwoFiveSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroTwoFiveSE.grid(column=2, row=1, padx=(3, 0))
    zeroFiveZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroFiveZeroSE.grid(column=2, row=2, padx=(3, 0))
    zeroSevenFiveSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    zeroSevenFiveSE.grid(column=2, row=3, padx=(3, 0))
    oneZeroZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    oneZeroZeroSE.grid(column=2, row=4, padx=(3, 0))
    oneFiveZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    oneFiveZeroSE.grid(column=2, row=5, padx=(3, 0))
    twoZeroZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    twoZeroZeroSE.grid(column=2, row=6, padx=(3, 0))
    twoFiveZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    twoFiveZeroSE.grid(column=2, row=7, padx=(3, 0))
    threeZeroZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    threeZeroZeroSE.grid(column=2, row=8, padx=(3, 0))
    threeFiveZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    threeFiveZeroSE.grid(column=2, row=9, padx=(3, 0))
    fourZeroZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fourZeroZeroSE.grid(column=2, row=10, padx=(3, 0))
    fourFiveZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fourFiveZeroSE.grid(column=2, row=11, padx=(3, 0))
    fiveZeroZeroSE = ttk.Entry(soakUnsoakFrame, width=8, font=("Segoe UI", 8))
    fiveZeroZeroSE.grid(column=2, row=12, padx=(3, 0))

    return soakUnsoakFrame

def setup_weight_frame(tab):
    weightFrame = ttk.Frame(tab, padding=(20, 20, 0, 20))
    weightFrame.grid(column=1, row=0, columnspan=3, sticky=(N,W))

    WoMaWSL = ttk.Label(weightFrame, text="Weight of Mold & Wet Soil", font=("Segoe UI", 8))
    WoMaWSL.grid(column=0, row=1, sticky=(N,E), padx=(0, 5))
    WoML = ttk.Label(weightFrame, text="Weight of Mold (grams)", font=("Segoe UI", 8))
    WoML.grid(column=0, row=2, sticky=(N,E), padx=(0, 5))

    unsoakedML = ttk.Label(weightFrame, text="Unsoaked\n    Mold", font=("Segoe UI", 8))
    unsoakedML.grid(column=1, row=0, pady=(0, 10))
    WoMaWSE1 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMaWSE1.grid(column=1, row=1, pady=(0, 3), padx=(3, 3))
    WoMLE1 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMLE1.grid(column=1, row=2, pady=(3, 0), padx=(3, 3))

    soakedML = ttk.Label(weightFrame, text="Soaked\n  Mold", font=("Segoe UI", 8))
    soakedML.grid(column=2, row=0, pady=(0, 10))
    WoMaWSE2 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMaWSE2.grid(column=2, row=1, pady=(0, 3), padx=(3, 3))
    WoMLE2 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMLE2.grid(column=2, row=2, pady=(3, 0), padx=(3, 3))

    MoldAfterImmersionL = ttk.Label(weightFrame, text=" Mold After\n Immersion", font=("Segoe UI", 8))
    MoldAfterImmersionL.grid(column=3, row=0, pady=(0, 10))
    WoMaWSE3 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMaWSE3.grid(column=3, row=1, pady=(0, 3), padx=(3, 0))
    WoMLE3 = ttk.Entry(weightFrame, width=8, font=("Segoe UI", 8))
    WoMLE3.grid(column=3, row=2, pady=(3, 0), padx=(3, 0))

    return weightFrame

def setup_reading_frame(tab):
    readingFrame = ttk.Frame(tab)
    readingFrame.grid(column=0, row=0, sticky=(N))
    RBIL = ttk.Label(readingFrame, text="Reading Before Immersion", font=("Segoe UI", 8))
    RBIL.grid(column=0, row=0)
    RAIL = ttk.Label(readingFrame, text="Reading After Immersion", font=("Segoe UI", 8))
    RAIL.grid(column=0, row=1)
    RBIE = ttk.Entry(readingFrame, width=8, font=("Segoe UI", 8))
    RBIE.grid(column=1, row=0, padx=(5, 0), pady=(0, 3))
    RAIE = ttk.Entry(readingFrame, width=8, font=("Segoe UI", 8))
    RAIE.grid(column=1, row=1, padx=(5, 0), pady=(3, 0))
    return readingFrame

def setup_blows_per_layer_frame(tab):
    blowsPerLayerFrame = ttk.Frame(tab)
    blowsPerLayerFrame.grid(column=1, row=0, sticky=(N), pady=(15, 0), padx=(30, 0))
    BPLL = ttk.Label(blowsPerLayerFrame, text="Blows Per Layer", font=("Segoe UI", 8))
    BPLL.grid(column=0, row=0)
    BPLE = ttk.Entry(blowsPerLayerFrame, width=8, font=("Segoe UI", 8))
    BPLE.grid(column=1, row=0, padx=(5, 0))
    return blowsPerLayerFrame

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
    cupE1 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE1.grid(column=1, row=1, pady=(0, 3), padx=(0, 3))
    cupE2 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE2.grid(column=1, row=2, pady=(3, 3), padx=(0, 3))
    cupE3 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE3.grid(column=1, row=3, pady=(3, 3), padx=(0, 3))
    cupE4 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE4.grid(column=1, row=4, pady=(3, 3), padx=(0, 3))
    cupE5 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE5.grid(column=1, row=5, pady=(3, 3), padx=(0, 3))
    cupE6 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupE6.grid(column=1, row=6, pady=(3, 0), padx=(0, 3))

    cupWeightL = ttk.Label(moistureFrame, text="Cup Weight\n    (grams)", font=("Segoe UI", 8))
    cupWeightL.grid(column=2, row=0, pady=(0, 5))
    cupWE1 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE1.grid(column=2, row=1, padx=(3, 0))
    cupWE2 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE2.grid(column=2, row=2, padx=(3, 0))
    cupWE3 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE3.grid(column=2, row=3, padx=(3, 0))
    cupWE4 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE4.grid(column=2, row=4, padx=(3, 0))
    cupWE5 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE5.grid(column=2, row=5, padx=(3, 0))
    cupWE6 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    cupWE6.grid(column=2, row=6, padx=(3, 0))

    wetWeightL = ttk.Label(moistureFrame, text="Wet Weight\n    (grams)", font=("Segoe UI", 8))
    wetWeightL.grid(column=3, row=0, pady=(0, 5))
    wetE1 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE1.grid(column=3, row=1)
    wetE2 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE2.grid(column=3, row=2)
    wetE3 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE3.grid(column=3, row=3)
    wetE4 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE4.grid(column=3, row=4)
    wetE5 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE5.grid(column=3, row=5)
    wetE6 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    wetE6.grid(column=3, row=6)

    dryWeightL = ttk.Label(moistureFrame, text="Dry Weight\n   (grams)", font=("Segoe UI", 8))
    dryWeightL.grid(column=4, row=0, pady=(0, 5))
    dryE1 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE1.grid(column=4, row=1)
    dryE2 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE2.grid(column=4, row=2)
    dryE3 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE3.grid(column=4, row=3)
    dryE4 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE4.grid(column=4, row=4)
    dryE5 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE5.grid(column=4, row=5)
    dryE6 = ttk.Entry(moistureFrame, width=8, font=("Segoe UI", 8))
    dryE6.grid(column=4, row=6)

    return moistureFrame

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

    DryWeightAirE = ttk.Entry(plusFourFrame, width=8, font=("Segoe UI", 8))
    DryWeightAirE.grid(column=1, row=1, pady=(0, 3))
    SSDWeightAirE = ttk.Entry(plusFourFrame, width=8, font=("Segoe UI", 8))
    SSDWeightAirE.grid(column=1, row=2, pady=(3, 3))
    WeightWaterE = ttk.Entry(plusFourFrame, width=8, font=("Segoe UI", 8))
    WeightWaterE.grid(column=1, row=3, pady=(3, 0))

    return plusFourFrame


def create_tab5(notebook):
    tab5 = ttk.Frame(notebook, padding=(20, 0, 0, 0))
    notebook.add(tab5, text="CBR")

    containerFrame = ttk.Frame(tab5, padding=(0, 0, 0, 10))
    containerFrame.grid(column=1, row=1)

    dateCompletedFrame = setup_date_completed_frame2(tab5)
    soakUnsoakFrame = setup_soak_unsoak_frame(tab5)
    weightFrame = setup_weight_frame(tab5)
    readingFrame = setup_reading_frame(containerFrame)
    blowsPerLayerFrame = setup_blows_per_layer_frame(containerFrame)
    moistureFrame = setup_moisture_frame(tab5)
    plusFourFrame = setup_plus_four_frame(tab5)

    return tab5