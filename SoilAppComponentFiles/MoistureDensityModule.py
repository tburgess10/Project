import sqlite3
import numpy as np

class MoistureDensityModule:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.results = []

    def fetch_test_data(self, test_id):
        """ Fetches test data from the database based on a test ID. """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM MoistureDensityResult WHERE MoistureDensityTestID = ?", (test_id,))
        test_data = cursor.fetchone()
        return test_data

    def fetch_test_points(self, test_id):
        """ Fetches test point data associated with a given test ID. """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Proctor WHERE MoistureDensityTestID = ?", (test_id,))
        test_points = cursor.fetchall()
        return test_points

    def calculate_percent_moisture(self, tare_weight, tare_and_wet_soil_weight, tare_and_dry_soil_weight):
        """ Calculate the percent moisture of the soil. """
        water_weight = tare_and_wet_soil_weight - tare_and_dry_soil_weight
        dry_soil_weight = tare_and_dry_soil_weight - tare_weight
        percent_moisture = (water_weight / dry_soil_weight) * 100
        return round(percent_moisture, 2)

    def calculate_wet_density(self, compacted_sample_weight, mold_weight, mold_volume):
        """ Calculate the wet density (lbs./cu.ft.). """
        wet_density = (compacted_sample_weight - mold_weight) / mold_volume
        return round(wet_density, 2)

    def calculate_dry_density(self, wet_density, percent_moisture):
        """ Calculate the dry density (lbs./cu.ft.). """
        dry_density = wet_density / (1 + (percent_moisture / 100))
        return round(dry_density, 2)

    def fit_quadratic_curve(self, moisture_contents, dry_densities):
        """ Fit a quadratic curve (y = ax^2 + bx + c) to the data points. """
        coefficients = np.polyfit(moisture_contents, dry_densities, 2)
        a, b, c = coefficients
        return a, b, c

    def find_optimum_moisture_and_max_density(self, a, b, c):
        """ Find the optimum moisture content and maximum dry density. """
        optimum_moisture = -b / (2 * a)
        max_dry_density = a * optimum_moisture**2 + b * optimum_moisture + c
        return round(optimum_moisture, 2), round(max_dry_density, 2)

    def process_moisture_density_test(self, test_id):
        """ Process moisture density data for a given test ID. """
        # Fetch test data and test points from the database
        test_data = self.fetch_test_data(test_id)
        if not test_data:
            return {"success": False, "message": "Test data not found"}
    
        try:
            mold_weight = float(test_data['MoldWeight'])
            mold_volume = float(test_data['MoldNumber'])
        except (ValueError, KeyError) as e:
            return {"success": False, "message": f"Invalid or missing mold data: {e}"}
    
        test_points = self.fetch_test_points(test_id)
        if not test_points:
            return {"success": False, "message": "No test points found for the given test ID"}
    
        moisture_contents = []
        dry_densities = []
    
        # Process each test point
        for point in test_points:
            try:
                compacted_sample_weight = float(point['MoldWeight'])
                tare_weight = float(point['DishWeight'])
                tare_and_wet_soil_weight = float(point['DishAndWetSoilWeight'])
                tare_and_dry_soil_weight = float(point['DishAndDrySoilWeight'])
    
                if None in (compacted_sample_weight, tare_weight, tare_and_wet_soil_weight, tare_and_dry_soil_weight):
                    raise ValueError("Missing data for calculations")
    
                # Calculate percent moisture
                percent_moisture = self.calculate_percent_moisture(
                    tare_weight, tare_and_wet_soil_weight, tare_and_dry_soil_weight)
                moisture_contents.append(percent_moisture)
    
                # Calculate wet density
                wet_density = self.calculate_wet_density(compacted_sample_weight, mold_weight, mold_volume)
    
                # Calculate dry density
                dry_density = self.calculate_dry_density(wet_density, percent_moisture)
                dry_densities.append(dry_density)
    
                # Store results for this point
                self.results.append({
                    "Compacted Sample Weight": compacted_sample_weight,
                    "Tare Weight": tare_weight,
                    "Tare and Wet Soil Weight": tare_and_wet_soil_weight,
                    "Tare and Dry Soil Weight": tare_and_dry_soil_weight,
                    "Percent Moisture": percent_moisture,
                    "Wet Density": wet_density,
                    "Dry Density": dry_density
                })
            except (ValueError, ZeroDivisionError) as e:
                print(f"Skipping point due to error: {e}")
                continue
    
        if not moisture_contents or not dry_densities:
            return {"success": False, "message": "Insufficient valid data points for calculations"}
    
        try:
            a, b, c = self.fit_quadratic_curve(moisture_contents, dry_densities)
            optimum_moisture, max_dry_density = self.find_optimum_moisture_and_max_density(a, b, c)
        except Exception as e:
            return {"success": False, "message": f"Error in fitting curve or calculations: {e}"}
    
        self.store_results_in_database(test_id, max_dry_density, optimum_moisture)
    
        return {
            "success": True,
            "Max Dry Density": max_dry_density,
            "Optimum Moisture Content": optimum_moisture,
            "Results": self.results
        }



    def store_results_in_database(self, test_id, max_dry_density, optimum_moisture_content):
        """ Stores the processed results in the database. """
        cursor = self.db_connection.cursor()
        query = """
        UPDATE MoistureDensityResult
        SET MaxDryDensity = ?, OptimumMoisture = ?
        WHERE MoistureDensityTestID = ?
        """
        cursor.execute(query, (max_dry_density, optimum_moisture_content, test_id))
        self.db_connection.commit()
    def call_moisture_density(self, process_moisture_density_test):
        if __name__ == "__main__":
            db_connection = sqlite3.connect('Soil_framework.sqlite')
            db_connection.row_factory = sqlite3.Row
            moisture_density_module = MoistureDensityModule(db_connection)
        
            # Fetch all test IDs from the database
            cursor = db_connection.cursor()
            cursor.execute("SELECT DISTINCT MoistureDensityTestID FROM MoistureDensityResult")
            test_ids = [row['MoistureDensityTestID'] for row in cursor.fetchall()]
        
            # Process each test ID
            for test_id in test_ids:
                print(f"Processing Test ID: {test_id}")
                results = moisture_density_module.process_moisture_density_test(test_id)
                
                if results["success"]:
                    print(f"Test ID {test_id} - Max Dry Density: {results['Max Dry Density']}")
                    print(f"Test ID {test_id} - Optimum Moisture Content: {results['Optimum Moisture Content']}")
                else:
                    print(f"Test ID {test_id} - Error: {results['message']}")
        
                for point_result in results.get("Results", []):
                    print(point_result)
        
            # Close the database connection
            db_connection.close()
