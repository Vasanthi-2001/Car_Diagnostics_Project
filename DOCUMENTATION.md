# Car Diagnostics Project

## Introduction
This Python project analyzes car diagnostic data to assess vehicle health and detect engine stress or sensor failures. It loads diagnostic data from a CSV file, computes performance scores for each car, and prints alerts for severe engine stress or missing sensor data.

## Classes & Functions

### Diagnostic
Represents a single diagnostic reading for a car.
- **Attributes:** `car_id`, `type` (e.g., RPM, EngineLoad, CoolantTemp), `value`

### Car
Represents a car and its diagnostics.
- **Attributes:** `id`, `diagnostics` (list of Diagnostic objects)
- **Methods:**
  - `add_diagnostic(diag)`: Adds a diagnostic to the car.
  - `compute_performance_score()`: Calculates the car’s performance score using the formula:
    ```
    score = 100 - (rpm/100 + engineLoad*0.5 + (coolantTemp - 90) * 2)
    ```
  - `has_all_diagnostics()`: Checks if all required diagnostic types are present.

### GarageMonitor
Manages multiple cars and checks for alerts.
- **Attributes:** `cars` (list of Car objects)
- **Methods:**
  - `add_car(car)`: Adds a car to the monitor.
  - `check_driver_abuse()`: Alerts if a car’s score is below 40.
  - `check_engine_issues()`: Alerts if any diagnostic is missing.
  - `assess_health()`: Returns all alerts.

### main.py
- Loads diagnostics from CSV.
- Groups diagnostics by car.
- Prints each car’s score and alerts.

## Sample Input

**CSV File (`data/diagnostics.csv`):**
```
Car1,RPM,6500
Car1,CoolantTemp,120
Car2,EngineLoad,95
```

## Sample Output

```
Car ID: Car1, Performance Score: 0.0
Severe Engine Stress
Sensor Failure Detected
Car ID: Car2, Performance Score: 52.5
Sensor Failure Detected
```

## How to Run

1. Place your diagnostic data in `data/diagnostics.csv` (see format above).
2. Run the project:
   ```
   python src/main.py
   ```

## License
MIT License
