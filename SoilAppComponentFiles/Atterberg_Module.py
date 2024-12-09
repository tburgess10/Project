import sqlite3

class AtterbergLimitsModule:
    def __init__(self, db_connection):
        self.db_connection_path = db_connection
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_connection_path)
        print(f"Connected to database: {self.db_connection_path}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def fetch_all_sample_ids(self):
        """
        Fetch all SampleID values from the database.
        """
        query = "SELECT DISTINCT SampleID FROM Atterberg"  # Adjust table name
        cursor = self.conn.cursor()
        cursor.execute(query)
        sample_ids = [row[0] for row in cursor.fetchall()]
        return sample_ids


    def fetch_data(self, sample_id):
        """Fetches the Atterberg limits data for a given SampleID, skipping rows with invalid data types."""
        cursor = self.conn.cursor()
        query = """
        SELECT SampleID, LiquidLimitTareWeight, LiquidLimitWeight,
               LiquidLimitDryWeight, LiquidLimitNumberOfBlows, LiquidLimitNotObtained,
               PlasticLimitTareWeight, PlasticLimitWetWeight, PlasticLimitDryWeight,
               PlasticLimitNotObtained
        FROM Atterberg
        WHERE SampleID = ?
        """
        cursor.execute(query, (sample_id,))
        row = cursor.fetchone()
    
        if row:
            try:
                # Convert values to the appropriate types
                data = {
                    'SampleID': row[0],
                    'LiquidLimitTareWeight': float(row[1]),
                    'LiquidLimitWeight': float(row[2]),
                    'LiquidLimitDryWeight': float(row[3]),
                    'LiquidLimitNumberOfBlows': int(row[4]),
                    'LiquidLimitNotObtained': str(row[5]).strip().upper() if row[5] is not None else None,
                    'PlasticLimitTareWeight': float(row[6]),
                    'PlasticLimitWetWeight': float(row[7]),
                    'PlasticLimitDryWeight': float(row[8]),
                    'PlasticLimitNotObtained': str(row[9]).strip().upper() if row[9] is not None else None,
                }
                print(f"Fetched and processed data: {data}")
                return data
            except (TypeError, ValueError) as e:
                print(f"Skipping row for SampleID {sample_id} due to invalid data: {e}")
                return None
        else:
            print(f"No valid data found for SampleID {sample_id}.")
            return None


    def validate_atterberg_data(self, data):
        """ Validates input data for Atterberg limits testing. """
        if not data.get('LiquidLimitNotObtained'):
            required_fields = ['LiquidLimitTareWeight', 'LiquidLimitWeight', 'LiquidLimitDryWeight', 'LiquidLimitNumberOfBlows']
            for field in required_fields:
                if field not in data or data[field] is None:
                    return False, f"{field} is required for Liquid Limit."
            if data['LiquidLimitWeight'] <= data['LiquidLimitDryWeight']:
                return False, "Liquid Limit Wet Weight must be greater than Dry Weight."
        
        if not data.get('PlasticLimitNotObtained'):
            required_fields = ['PlasticLimitTareWeight', 'PlasticLimitWetWeight', 'PlasticLimitDryWeight']
            for field in required_fields:
                if field not in data or data[field] is None:
                    return False, f"{field} is required for Plastic Limit."
            if data['PlasticLimitWetWeight'] <= data['PlasticLimitDryWeight']:
                return False, "Plastic Limit Wet Weight must be greater than Dry Weight."
        
        return True, ""

    def calculate_percent_moisture(self, tare_weight, wet_weight, dry_weight):
        if tare_weight is None or wet_weight is None or dry_weight is None:
            print("Invalid input for percent moisture calculation.")
            return None
        water_weight = wet_weight - dry_weight
        dry_soil_weight = dry_weight - tare_weight
        if dry_soil_weight == 0:
            print("Error: Dry soil weight is zero.")
            return None
        percent_moisture = round((water_weight / dry_soil_weight) * 100, 2)
        print(f"Percent Moisture: {percent_moisture}%")
        return percent_moisture

    def calculate_liquid_limit(self, percent_moisture, blows):
        if blows is None or blows <= 0 or percent_moisture is None:
            print("Invalid input for liquid limit calculation.")
            return None
        correction_factor = (blows / 25) ** 0.121
        liquid_limit = round(percent_moisture * correction_factor, 2)
        print(f"Liquid Limit: {liquid_limit}")
        return liquid_limit

    def calculate_plastic_limit(self, percent_moisture):
        if percent_moisture is None:
            print("Invalid input for plastic limit calculation.")
            return None
        print(f"Plastic Limit: {percent_moisture}")
        return percent_moisture

    def calculate_plasticity_index(self, liquid_limit, plastic_limit):
        print(f"Calculating Plasticity Index: LiquidLimit={liquid_limit}, PlasticLimit={plastic_limit}")
        if liquid_limit is None or plastic_limit is None:
            print("Invalid input for plasticity index calculation.")
            return None
        plasticity_index = round(liquid_limit - plastic_limit, 2)
        print(f"Plasticity Index: {plasticity_index}")
        return plasticity_index      

    def store_atterberg_results(self, data):
        """ Updates the Atterberg Limits results in the SQLite database. """
        cursor = self.conn.cursor()
        query = """
        UPDATE Atterberg
        SET LiquidLimit = ?, PlasticLimit = ?, PlasticityIndex = ?
        WHERE SampleID = ?
        """
        values = (
            data.get('LiquidLimit'),
            data.get('PlasticLimit'),
            data.get('PlasticityIndex'),
            data.get('SampleID'),
        )
        print(f"Executing SQL: {query} with values {values}")  # Debug log
        cursor.execute(query, values)
        self.conn.commit()
        print("Database updated successfully.")

    def process_atterberg_data(self, data):
        is_valid, error_message = self.validate_atterberg_data(data)
        if not is_valid:
            print(f"Validation failed: {error_message}")
            return {"success": False, "message": error_message}
        print("Validation passed.")
        print(f"LiquidLimitNotObtained: {data.get('LiquidLimitNotObtained')}")
        print(f"PlasticLimitNotObtained: {data.get('PlasticLimitNotObtained')}")
    
        liquid_limit = None
        plastic_limit = None
        plasticity_index = None
    
        # Calculate Liquid Limit
        if data.get('LiquidLimitNotObtained') == 'FALSE':  # Explicitly check string value
            percent_moisture_liquid = self.calculate_percent_moisture(
                data['LiquidLimitTareWeight'],
                data['LiquidLimitWeight'],
                data['LiquidLimitDryWeight']
            )
            print(f"Percent Moisture for Liquid Limit: {percent_moisture_liquid}")
            liquid_limit = self.calculate_liquid_limit(percent_moisture_liquid, data['LiquidLimitNumberOfBlows'])
            print(f"Calculated Liquid Limit: {liquid_limit}")
    
        # Calculate Plastic Limit
        if data.get('PlasticLimitNotObtained') == 'FALSE':  # Explicitly check string value
            print("Calculating Plastic Limit...")
            percent_moisture_plastic = self.calculate_percent_moisture(
                data['PlasticLimitTareWeight'],
                data['PlasticLimitWetWeight'],
                data['PlasticLimitDryWeight']
            )
            print(f"Percent Moisture for Plastic Limit: {percent_moisture_plastic}")
            plastic_limit = self.calculate_plastic_limit(percent_moisture_plastic)
            print(f"Calculated Plastic Limit: {plastic_limit}")
    
        # Calculate Plasticity Index
        if liquid_limit is not None and plastic_limit is not None:
            plasticity_index = self.calculate_plasticity_index(liquid_limit, plastic_limit)
            print(f"Calculated Plasticity Index: {plasticity_index}")
    
        try:
            self.store_atterberg_results({
                'SampleID': data.get('SampleID'),
                'LiquidLimit': liquid_limit,
                'PlasticLimit': plastic_limit,
                'PlasticityIndex': plasticity_index
            })
            return {"success": True, "message": "Data processed successfully"}
        except Exception as e:
            print(f"Error storing results: {e}")
            return {"success": False, "message": str(e)}
db_path = 'Soil_framework.sqlite'

with AtterbergLimitsModule(db_path) as atterberg_module:
    sample_ids = atterberg_module.fetch_all_sample_ids()
    for sample_id in sample_ids:
        print(f"Processing SampleID {sample_id}...")
        data = atterberg_module.fetch_data(sample_id)
        if data:
            result = atterberg_module.process_atterberg_data(data)
            print(f"Result for SampleID {sample_id}: {result}")
        else:
            print(f"No data found for SampleID {sample_id}")