import sqlite3

class GradationModule:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def calculate_cumulative_retain(self, weights):
        cumulative_retain = []
        total = 0
        for weight in weights:
            total += weight
            cumulative_retain.append(total)
        return cumulative_retain

    def calculate_percent_passing(self, cumulative_retain, total_sample_weight):
        return [
            round((total_sample_weight - retain) / total_sample_weight * 100, 2)
            for retain in cumulative_retain
        ]

    def retrieve_and_process_gradation(self, sample_id):
        try:
            cursor = self.db_connection.cursor()

            # Retrieve test information
            cursor.execute(
                "SELECT GradationTestID, TotalSampleWeight, FinesTotalWeight FROM GradationTest WHERE SampleID = ?",
                (sample_id,)
            )
            test_info = cursor.fetchone()

            if not test_info:
                return {"success": False, "message": f"No gradation test found for SampleID {sample_id}"}

            test_id = test_info[0]
            total_sample_weight = self.clean_and_convert(test_info[1])
            fines_total_weight = self.clean_and_convert(test_info[2])

            # Check for invalid TotalSampleWeight or FinesTotalWeight
            invalid_fields = []
            if total_sample_weight is None:
                invalid_fields.append("TotalSampleWeight")
            if fines_total_weight is None:
                invalid_fields.append("FinesTotalWeight")
    
            if invalid_fields:
                return {
                    "success": False,
                    "message": f"Invalid data found for {', '.join(invalid_fields)} in database. Please check SampleID {sample_id}."
                }

            # Retrieve sieve data
            cursor.execute(
                "SELECT SieveID, WeightRetained FROM GradationResults WHERE GradationTestID = ?",
                (test_id,)
            )
            sieve_data = cursor.fetchall()

            if not sieve_data:
                print(f"Warning: No sieve data found for GradationTestID {test_id}. Skipping this record.")
                return {"success": False, "message": f"No sieve data found for GradationTestID {test_id}. Skipping."}

            sieve_order = [{"SieveID": sieve[0]} for sieve in sieve_data]
            weights_retained = [self.clean_and_convert(sieve[1]) for sieve in sieve_data]

            if any(weight is None for weight in weights_retained):
                return {"success": False, "message": f"Invalid weight data found for GradationTestID {test_id}"}


            cumulative_retain = self.calculate_cumulative_retain(weights_retained)
            percent_passing = self.calculate_percent_passing(cumulative_retain, total_sample_weight)


            self.store_gradation_results(test_id, sieve_order, weights_retained, cumulative_retain, percent_passing)
            return {"success": True, "message": f"Gradation test for SampleID {sample_id} processed successfully."}

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return {"success": False, "message": f"Database error: {e}"}
        except ValueError as e:
            print(f"Value conversion error: {e}")
            return {"success": False, "message": f"Value error: {e}"}

    def clean_and_convert(self, value):
        """
        Cleans and converts a value to float. Returns None if the value is invalid.
        """
        if value is None or value == '':
            return None
        try:
            return float(value)
        except ValueError:
            return None

    def store_gradation_results(self, test_id, sieve_order, weights_retained, cumulative_retain, percent_passing):
        cursor = self.db_connection.cursor()
    
        try:
            for i, sieve in enumerate(sieve_order):
                query = """
                UPDATE GradationResults
                SET CumulativeRetained = ?, PercentPassing = ?
                WHERE GradationTestID = ?
                """
                values = (
                    cumulative_retain[i],
                    percent_passing[i],
                    sieve['SieveID']  
                )
                cursor.execute(query, values)
    
            self.db_connection.commit()
            print("Gradation results updated successfully.")
        except sqlite3.Error as e:
            print(f"Error storing gradation results: {e}")
            self.db_connection.rollback()
if __name__ == "__main__":
    db_connection = sqlite3.connect('Soil_framework.sqlite')
    db_connection.row_factory = sqlite3.Row
    gradation_module = GradationModule(db_connection)

    # Fetch all test IDs from the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT DISTINCT SampleID FROM GradationTest;")
    test_ids = [row['SampleID'] for row in cursor.fetchall()]

    # Process each test ID
    for test_id in test_ids:
        print(f"Processing Test ID: {test_id}")
        results = gradation_module.retrieve_and_process_gradation(test_id)
