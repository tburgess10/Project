import sqlite3

class AtterbergLimitsModule:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def validate_atterberg_data(self, data):
        """ Validates input data for Atterberg limits testing. """
        # Check for required fields when limits are not marked as 'Not Obtained'
        if not data.get('LiquidLimitNotObtained'):
            required_fields = ['LiquidLimitTareWeight', 'LiquidLimitWetSampleWeight', 'LiquidLimitDrySampleWeight', 'LiquidLimitNumberOfBlows']
            for field in required_fields:
                if field not in data or data[field] is None:
                    return False, f"{field} is required for Liquid Limit."
            if data['LiquidLimitWetSampleWeight'] <= data['LiquidLimitDrySampleWeight']:
                return False, "Liquid Limit Wet Weight must be greater than Dry Weight."
        
        if not data.get('PlasticLimitNotObtained'):
            required_fields = ['PlasticLimitTareWeight', 'PlasticLimitWetSampleWeight', 'PlasticLimitDrySampleWeight']
            for field in required_fields:
                if field not in data or data[field] is None:
                    return False, f"{field} is required for Plastic Limit."
            if data['PlasticLimitWetSampleWeight'] <= data['PlasticLimitDrySampleWeight']:
                return False, "Plastic Limit Wet Weight must be greater than Dry Weight."
        
        return True, ""

    def calculate_percent_moisture(self, tare_weight, wet_weight, dry_weight):
        """ Calculates the percent moisture of a soil sample. """
        water_weight = wet_weight - dry_weight
        dry_soil_weight = dry_weight - tare_weight
        return round((water_weight / dry_soil_weight) * 100, 2)

    def calculate_liquid_limit(self, percent_moisture, blows):
        """ Calculates the Liquid Limit based on percent moisture and number of blows. """
        if blows is None or blows <= 0:
            return None  # Handle cases where the Liquid Limit cannot be determined
        correction_factor = (blows / 25) ** 0.121
        return round(percent_moisture * correction_factor, 2)

    def calculate_plastic_limit(self, percent_moisture):
        """ Calculates the Plastic Limit as the moisture content. """
        return percent_moisture  # Directly using the calculated moisture content for Plastic Limit

    def calculate_plasticity_index(self, liquid_limit, plastic_limit):
        """ Calculates the Plasticity Index. """
        if liquid_limit is None or plastic_limit is None:
            return None
        return round(liquid_limit - plastic_limit, 2)

    def store_atterberg_results(self, data):
        """ Stores the Atterberg Limits results in the SQLite database. """
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO AtterbergLimits (SampleID, LiquidLimit, PlasticLimit, PlasticityIndex, Remarks)
        VALUES (?, ?, ?, ?, ?)
        """
        values = (
            data['SampleID'],
            data.get('LiquidLimit'),
            data.get('PlasticLimit'),
            data.get('PlasticityIndex'),
            data.get('Remarks')
        )
        cursor.execute(query, values)
        self.db_connection.commit()

    def process_atterberg_data(self, data):
        """ Main function to process Atterberg Limits data. """
        # Step 1: Validate input data
        is_valid, error_message = self.validate_atterberg_data(data)
        if not is_valid:
            return {"success": False, "message": error_message}

        # Step 2: Perform calculations
        liquid_limit = None
        plastic_limit = None
        plasticity_index = None

        # Calculate Liquid Limit if not marked as 'Not Obtained'
        if not data.get('LiquidLimitNotObtained'):
            percent_moisture_liquid = self.calculate_percent_moisture(
                data['LiquidLimitTareWeight'],
                data['LiquidLimitWetSampleWeight'],
                data['LiquidLimitDrySampleWeight']
            )
            liquid_limit = self.calculate_liquid_limit(percent_moisture_liquid, data['LiquidLimitNumberOfBlows'])

        # Calculate Plastic Limit if not marked as 'Not Obtained'
        if not data.get('PlasticLimitNotObtained'):
            percent_moisture_plastic = self.calculate_percent_moisture(
                data['PlasticLimitTareWeight'],
                data['PlasticLimitWetSampleWeight'],
                data['PlasticLimitDrySampleWeight']
            )
            plastic_limit = self.calculate_plastic_limit(percent_moisture_plastic)

        # Calculate Plasticity Index if both limits are obtained
        if liquid_limit is not None and plastic_limit is not None:
            plasticity_index = self.calculate_plasticity_index(liquid_limit, plastic_limit)

        # Step 3: Store results in the database
        try:
            self.store_atterberg_results({
                'SampleID': data['SampleID'],
                'LiquidLimit': liquid_limit,
                'PlasticLimit': plastic_limit,
                'PlasticityIndex': plasticity_index,
                'Remarks': data.get('Remarks')
            })
            return {"success": True, "message": "Data processed successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
