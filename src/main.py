import csv
from car import Car

## @file main.py
#  @brief Entry point for the car diagnostics project.
#  Handles loading diagnostic data, processing, and printing results.

## @brief Loads diagnostic data from a CSV file.
#  @param file_path Path to the CSV file.
#  @return List of diagnostic dictionaries with keys 'id', 'type', and 'value'.
#  @details
#  Reads each row, skips header if present, validates row length and value type.
def load_diagnostics_from_csv(file_path):
    diagnostics = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header_skipped = False
        for row in reader:
            # Skip header row if present
            if not header_skipped and (row[0].lower() == 'car1' or row[0].lower() == 'id' or row[0].lower().startswith('car')):
                if not row[0].replace(' ', '').isnumeric():
                    header_skipped = True
                    continue
            if len(row) != 3:
                continue
            car_id, diag_type, value = row
            try:
                diagnostics.append({
                    'id': car_id.strip(),
                    'type': diag_type.strip(),
                    'value': float(value.strip())
                })
            except ValueError:
                # Skip rows with non-numeric value
                continue
    return diagnostics

## @brief Main entry point for the car diagnostics program.
#  Loads diagnostics, groups by car, computes scores, and prints alerts.
#  @details
#  - Loads diagnostic data from CSV file.
#  - Groups diagnostics by car ID.
#  - Computes performance score for each car.
#  - Prints alerts for severe engine stress and sensor failure.
def main():
    diagnostics_file = '../data/diagnostics.csv'
    diagnostics = load_diagnostics_from_csv(diagnostics_file)

    cars = {}
    # Group diagnostics by car ID and create Car objects
    for diag in diagnostics:
        car_id = diag['id']
        if car_id not in cars:
            cars[car_id] = Car(car_id)
        cars[car_id].add_diagnostic(diag)

    # Compute and print performance score and alerts for each car
    for car in cars.values():
        performance_score = car.compute_performance_score()
        print(f'Car ID: {car.id}, Performance Score: {performance_score}')
        if performance_score < 40:
            print("Severe Engine Stress")
        if not car.has_all_diagnostics():
            print("Sensor Failure Detected")

## @brief Program entry point.
#  Executes main function if run as a script.
if __name__ == "__main__":
    main()