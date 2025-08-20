class GarageMonitor:
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