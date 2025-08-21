

class Car:
    """
    @file car.py
    @brief Defines the Car class for managing car diagnostics and performance evaluation.

    @class Car
    @brief Represents a car with diagnostic data and performance scoring.

    @fn __init__(self, car_id)
    @brief Initializes a Car instance.
    @param car_id Unique identifier for the car.

    @fn add_diagnostic(self, diag)
    @brief Adds a diagnostic entry to the car.
    @param diag Dictionary containing diagnostic data ('id', 'type', 'value').

    @fn compute_performance_score(self)
    @brief Computes the car's performance score based on diagnostic values.
    @return int Performance score (out of 100).

    @fn has_all_diagnostics(self)
    @brief Checks if all required diagnostic types are present.
    @return bool True if all required types are present, False otherwise.

    @fn get_alerts(self)
    @brief Generates alerts based on diagnostic values and performance score.
    @return list List of alert messages.

    @import Diagnostic
    @brief Imports the Diagnostic class for use in Car.
    """
    def __init__(self, car_id):
        self.id = car_id
        self.diagnostics = []

    def add_diagnostic(self, diag):
        # diag is a dict from main.py
        self.diagnostics.append(Diagnostic(diag['id'], diag['type'], diag['value']))

    def compute_performance_score(self):
        score = 100  # Start with a perfect score
        for diagnostic in self.diagnostics:
            if diagnostic.type == "RPM" and diagnostic.value > 3000:
                score -= 20  # Penalty for high RPM
            elif diagnostic.type == "EngineLoad" and diagnostic.value > 80:
                score -= 30  # Penalty for high engine load
            elif diagnostic.type == "CoolantTemp" and diagnostic.value > 90:
                score -= 25  # Penalty for high coolant temperature
        return score

    def has_all_diagnostics(self):
        # Check if all three types are present
        types_present = {d.type for d in self.diagnostics}
        required_types = {"RPM", "EngineLoad", "CoolantTemp"}
        return required_types.issubset(types_present)

    def get_alerts(self):
        alerts = []
        for diagnostic in self.diagnostics:
            if diagnostic.value is None:
                alerts.append("Sensor Failure Detected")
        if self.compute_performance_score() < 40:
            alerts.append("Severe Engine Stress")
        return alerts

# Import Diagnostic for use in Car
from diagnostic import Diagnostic