

class GarageMonitor:
    """
    @file garage_monitor.py
    @brief Monitors the health and diagnostics of cars in a garage.

    @class GarageMonitor
    @brief A class to manage and monitor a collection of cars for engine health and driver abuse.

    @fn __init__(self)
    @brief Initializes the GarageMonitor with an empty list of cars.

    @fn add_car(self, car)
    @param car The car object to be added to the monitor.
    @brief Adds a car to the garage monitor.

    @fn check_driver_abuse(self)
    @return list of str Alerts for cars experiencing severe engine stress.
    @brief Checks all cars for signs of driver abuse based on performance score.

    @fn check_engine_issues(self)
    @return list of str Alerts for cars with sensor failures.
    @brief Checks all cars for engine diagnostic issues.

    @fn assess_health(self)
    @return list of str Combined alerts for driver abuse and engine issues.
    @brief Assesses the overall health of all cars in the garage.
    """
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def check_driver_abuse(self):
        abuse_alerts = []
        for car in self.cars:
            if car.compute_performance_score() < 40:
                abuse_alerts.append(f"Severe Engine Stress detected in car with ID: {car.id}")
        return abuse_alerts

    def check_engine_issues(self):
        engine_issue_alerts = []
        for car in self.cars:
            if not car.diagnostics:
                engine_issue_alerts.append(f"Sensor Failure Detected in car with ID: {car.id}")
        return engine_issue_alerts

    def assess_health(self):
        alerts = self.check_driver_abuse() + self.check_engine_issues()
        return alerts