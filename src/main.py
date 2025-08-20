import csv
from car import Car

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

def main():
    diagnostics_file = '../data/diagnostics.csv'
    diagnostics = load_diagnostics_from_csv(diagnostics_file)

    cars = {}
    for diag in diagnostics:
        car_id = diag['id']
        if car_id not in cars:
            cars[car_id] = Car(car_id)
        cars[car_id].add_diagnostic(diag)

    for car in cars.values():
        performance_score = car.compute_performance_score()
        print(f'Car ID: {car.id}, Performance Score: {performance_score}')
        if performance_score < 40:
            print("Severe Engine Stress")
        if not car.has_all_diagnostics():
            print("Sensor Failure Detected")

if __name__ == "__main__":
    main()