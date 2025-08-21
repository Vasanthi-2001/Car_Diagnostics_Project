

import unittest
"""
@file testcases.py
@brief Unit tests for car diagnostics project components.
This module contains unit tests for the Diagnostic, Car, and GarageMonitor classes.
It verifies correct behavior for diagnostic representation, car performance scoring,
diagnostic completeness, alert generation, and garage-level monitoring features.
Classes:
    TestDiagnostic: Tests for the Diagnostic class.
        - test_repr: Checks string representation of Diagnostic objects.
    TestCar: Tests for the Car class.
        - setUp: Initializes a Car instance with sample diagnostics.
        - test_compute_performance_score: Verifies performance score calculation.
        - test_has_all_diagnostics: Checks if all required diagnostics are present.
        - test_get_alerts: Ensures alerts are generated for severe engine stress.
        - test_missing_diagnostic: Tests behavior when diagnostics are missing.
    TestGarageMonitor: Tests for the GarageMonitor class.
        - setUp: Initializes GarageMonitor with two Car instances.
        - test_check_driver_abuse: Checks detection of driver abuse alerts.
        - test_check_engine_issues: Verifies engine issue detection.
        - test_assess_health: Assesses overall health and alert generation.
@date 2024-06
@copyright Copyright (c) 2024
"""
from diagnostic import Diagnostic
from car import Car
from garage_monitor import GarageMonitor

class TestDiagnostic(unittest.TestCase):
    def test_repr(self):
        diag = Diagnostic("1", "RPM", 3000)
        self.assertEqual(repr(diag), "Diagnostic(id=1, type=RPM, value=3000)")

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("1")
        self.car.add_diagnostic({'id': '1', 'type': 'RPM', 'value': 3200})
        self.car.add_diagnostic({'id': '1', 'type': 'EngineLoad', 'value': 85})
        self.car.add_diagnostic({'id': '1', 'type': 'CoolantTemp', 'value': 95})

    def test_compute_performance_score(self):
        score = self.car.compute_performance_score()
        self.assertEqual(score, 100 - 20 - 30 - 25)

    def test_has_all_diagnostics(self):
        self.assertTrue(self.car.has_all_diagnostics())

    def test_get_alerts(self):
        alerts = self.car.get_alerts()
        self.assertIn("Severe Engine Stress", alerts)

    def test_missing_diagnostic(self):
        car2 = Car("2")
        car2.add_diagnostic({'id': '2', 'type': 'RPM', 'value': 2500})
        self.assertFalse(car2.has_all_diagnostics())

class TestGarageMonitor(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("1")
        self.car1.add_diagnostic({'id': '1', 'type': 'RPM', 'value': 3200})
        self.car1.add_diagnostic({'id': '1', 'type': 'EngineLoad', 'value': 85})
        self.car1.add_diagnostic({'id': '1', 'type': 'CoolantTemp', 'value': 95})

        self.car2 = Car("2")
        self.car2.add_diagnostic({'id': '2', 'type': 'RPM', 'value': 2500})

        self.monitor = GarageMonitor()
        self.monitor.add_car(self.car1)
        self.monitor.add_car(self.car2)

    def test_check_driver_abuse(self):
        abuse_alerts = self.monitor.check_driver_abuse()
        self.assertTrue(any("Severe Engine Stress" in alert for alert in abuse_alerts))

    def test_check_engine_issues(self):
        engine_alerts = self.monitor.check_engine_issues()
        self.assertFalse(engine_alerts)  # Both cars have diagnostics

    def test_assess_health(self):
        alerts = self.monitor.assess_health()
        self.assertTrue(any("Severe Engine Stress" in alert for alert in alerts))

if __name__ == "__main__":
    unittest.main()