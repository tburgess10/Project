import sqlite3

class GradationModule:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def validate_gradation_data(self, data):
        """ Validates input data for a gradation test. """
        required_fields = ['SampleID', 'TotalSampleWeight', 'SieveData']
        for field in required_fields:
            if field not in data or data[field] is None:
                return False, f"{field} is required."
        if not isinstance(data['SieveData'], list) or not data['SieveData']:
            return False, "Sieve data must be provided as a non-empty list."
        return True, ""

    def calculate_cumulative_retain(self, weights):
        """ Calculates the cumulative weight retained for each sieve size. """
        cumulative_retain = []
        total = 0
        for weight in weights:
            total += weight
            cumulative_retain.append(total)
        return cumulative_retain

    def calculate_percent_passing(self, cumulative_retain, total_sample_weight):
        """ Calculates the percent passing for each sieve size. """
        percent_passing = [
            round((total_sample_weight - retain) / total_sample_weight * 100, 2)
            for retain in cumulative_retain
        ]
        return percent_passing

    def store_gradation_results(self, test_id, sieve_order, weights_retained, cumulative_retain, percent_passing):
        """ Stores gradation results in the database. """
        cursor = self.db_connection.cursor()
        for i, sieve in enumerate(sieve_order):
            query = """
            INSERT INTO GradationResults (GradationTestID, SieveID, WeightRetained, CumulativeRetain, PercentPassing)
            VALUES (?, ?, ?, ?, ?)
            """
            values = (
                test_id,
                sieve['SieveID'],
                weights_retained[i],
                cumulative_retain[i],
                percent_passing[i]
            )
            cursor.execute(query, values)
        self.db_connection.commit()

    def process_gradation_test(self, data):
        """ Main function to process gradation test data. """
        # Step 1: Validate input data
        is_valid, error_message = self.validate_gradation_data(data)
        if not is_valid:
            return {"success": False, "message": error_message}

        # Preset sieve order (including Total Sample Weight and Fines Total Weight)
        sieve_order = [
            {"SieveID": "Total Sample Weight", "Label": "Total Sample Weight"},
            {"SieveID": "2-inch", "Label": "2\""},
            {"SieveID": "1-1/2-inch", "Label": "1-1/2\""},
            {"SieveID": "1-inch", "Label": "1\""},
            {"SieveID": "3/4-inch", "Label": "3/4\""},
            {"SieveID": "3/8-inch", "Label": "3/8\""},
            {"SieveID": "#4", "Label": "#4"},
            {"SieveID": "#10", "Label": "#10"},
            {"SieveID": "Fines Total Weight", "Label": "Fines Total Weight"},
            {"SieveID": "#20", "Label": "#20"},
            {"SieveID": "#40", "Label": "#40"},
            {"SieveID": "#60", "Label": "#60"},
            {"SieveID": "#80", "Label": "#80"},
            {"SieveID": "#100", "Label": "#100"},
            {"SieveID": "#200", "Label": "#200"}
        ]

        # Step 2: Extract weights from SieveData
        weights_retained = [sieve['WeightRetained'] for sieve in data['SieveData']]
        if len(weights_retained) != len(sieve_order):
            return {"success": False, "message": "Mismatch between expected and provided sieve data"}

        # Step 3: Calculate results
        cumulative_retain = self.calculate_cumulative_retain(weights_retained)
        percent_passing = self.calculate_percent_passing(cumulative_retain, data['TotalSampleWeight'])

        # Step 4: Store results in the database
        try:
            cursor = self.db_connection.cursor()
            # Insert a new gradation test record
            cursor.execute(
                "INSERT INTO GradationTests (SampleID, TotalSampleWeight, FinesTotalWeight) VALUES (?, ?, ?)",
                (data['SampleID'], data['TotalSampleWeight'], data.get('FinesTotalWeight', 0))
            )
            test_id = cursor.lastrowid  # Get the ID of the inserted gradation test

            # Store gradation results
            self.store_gradation_results(test_id, sieve_order, weights_retained, cumulative_retain, percent_passing)
            return {"success": True, "message": "Gradation test processed successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
