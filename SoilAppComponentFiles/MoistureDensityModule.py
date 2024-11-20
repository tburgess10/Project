import sqlite3
import numpy as np

class MoistureDensityModule:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.results = []

    def fetch_test_data(self, test_id):
        """ Fetches test data from the database based on a test ID. """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM MoistureDensityTests WHERE TestID = ?", (test_id,))
        test_data = cursor.fetchone()
        return test_data

    def fetch_test_points(self, test_id):
        """ Fetches test point data associated with a given test ID. """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM MoistureDensityTestPoints WHERE TestID = ?", (test_id,))
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
        # Fit a quadratic curve using numpy's polyfit function
        coefficients = np.polyfit(moisture_contents, dry_densities, 2)
        a, b, c = coefficients
        return a, b, c

    def find_optimum_moisture_and_max_density(self, a, b, c):
        """ Find the optimum moisture content and maximum dry density. """
        # Calculate the moisture content at maximum dry density (vertex of the parabola)
        optimum_moisture = -b / (2 * a)
        # Calculate the corresponding maximum dry density
        max_dry_density = a * optimum_moisture**2 + b * optimum_moisture + c
        return round(optimum_moisture, 2), round(max_dry_density, 2)

    def process_moisture_density_test(self, test_id):
        """ Process moisture density data for a given test ID. """
        # Fetch test data and test points from the database
        test_data = self.fetch_test_data(test_id)
        if not test_data:
            return {"success": False, "message": "Test data not found"}

        mold_weight = test_data['MoldWeight']
        mold_volume = test_data['MoldVolume']

        test_points = self.fetch_test_points(test_id)
        if not test_points:
            return {"success": False, "message": "No test points found for the given test ID"}

        moisture_contents = []
        dry_densities = []

        # Process each test point
        for point in test_points:
            compacted_sample_weight = point['CompactedSampleWeight']
            tare_weight = point['TareWeight']
            tare_and_wet_soil_weight = point['TareAndWetSoilWeight']
            tare_and_dry_soil_weight = point['TareAndDrySoilWeight']

            # Calculate percent moisture
            percent_moisture = self.calculate_percent_moisture(tare_weight, tare_and_wet_soil_weight, tare_and_dry_soil_weight)
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

        # Fit a quadratic curve to find the optimum moisture content and max dry density
        a, b, c = self.fit_quadratic_curve(moisture_contents, dry_densities)
        optimum_moisture, max_dry_density = self.find_optimum_moisture_and_max_density(a, b, c)

        # Save results to the database (if required)
        self.store_results_in_database(test_id, max_dry_density, optimum_moisture)

        return {
            "Max Dry Density": max_dry_density,
            "Optimum Moisture Content": optimum_moisture,
            "Results": self.results
        }

    def store_results_in_database(self, test_id, max_dry_density, optimum_moisture_content):
        """ Stores the processed results in the database. """
        cursor = self.db_connection.cursor()
        query = """
        UPDATE MoistureDensityTests
        SET MaxDryDensity = ?, OptimumMoistureContent = ?
        WHERE TestID = ?
        """
        cursor.execute(query, (max_dry_density, optimum_moisture_content, test_id))
        self.db_connection.commit()

# Example usage
if __name__ == "__main__":
    # Connect to the database
    db_connection = sqlite3.connect('your_database_name.db')
    db_connection.row_factory = sqlite3.Row  # Access rows as dictionaries
    moisture_density_module = MoistureDensityModule(db_connection)

    # Process data for a given test ID (replace with an actual test ID from your database)
    test_id = 1  # Example test ID
    results = moisture_density_module.process_moisture_density_test(test_id)
    print("Max Dry Density:", results["Max Dry Density"])
    print("Optimum Moisture Content:", results["Optimum Moisture Content"])
    print("Detailed Results:", results["Results"])
