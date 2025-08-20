class Car:
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